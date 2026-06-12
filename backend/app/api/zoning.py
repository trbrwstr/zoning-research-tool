from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from typing import Optional
import json

from app.models.database import get_db
from app.models.models import ZoningLookup
from app.api.schemas import ZoningLookupRequest, ZoningLookupResponse
from app.services.geocoding import GeocodingService
from app.services.scraping import MunicipalDataScraper
from app.services.ai_interpretation import AIInterpretationService
from app.services.mapbox_service import MapboxService

router = APIRouter(prefix="/api/zoning", tags=["zoning"])


@router.post("/lookup", response_model=ZoningLookupResponse)
async def lookup_zoning(
    request: ZoningLookupRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    """
    Perform a comprehensive zoning lookup for a given address.
    """
    # Initialize services
    geocoding_service = GeocodingService()
    mapbox_service = MapboxService()
    
    # Geocode the address
    geocode_result = await geocoding_service.geocode_address(request.address)
    if not geocode_result:
        raise HTTPException(status_code=400, detail="Unable to geocode address")
    
    lat, lon, location_data = geocode_result
    
    # Create lookup record
    lookup = ZoningLookup(
        address=request.address,
        latitude=lat,
        longitude=lon,
        raw_data=json.dumps(location_data)
    )
    db.add(lookup)
    db.commit()
    db.refresh(lookup)
    
    # Perform detailed analysis in background
    background_tasks.add_task(
        perform_detailed_analysis,
        lookup.id,
        request.address,
        lat,
        lon,
        request.municipality,
        request.state
    )
    
    # Generate map URL
    map_url = mapbox_service.generate_static_map(lat, lon)
    geojson = mapbox_service.generate_geojson_property_boundary(lat, lon)
    
    # Update with basic info
    lookup.map_url = map_url
    lookup.geojson_data = json.dumps(geojson)
    db.commit()
    
    return lookup


@router.get("/lookup/{lookup_id}", response_model=ZoningLookupResponse)
async def get_lookup(lookup_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a zoning lookup by ID.
    """
    lookup = db.query(ZoningLookup).filter(ZoningLookup.id == lookup_id).first()
    if not lookup:
        raise HTTPException(status_code=404, detail="Lookup not found")
    
    # Parse geojson if present
    if lookup.geojson_data:
        lookup.geojson_data = json.loads(lookup.geojson_data)
    
    # Parse interpreted data if present
    if lookup.additional_restrictions:
        try:
            lookup.interpreted_data = json.loads(lookup.additional_restrictions)
        except:
            lookup.interpreted_data = None
    
    return lookup


@router.get("/history", response_model=list[ZoningLookupResponse])
async def get_lookup_history(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """
    Get recent zoning lookups.
    """
    lookups = db.query(ZoningLookup).order_by(
        ZoningLookup.created_at.desc()
    ).offset(skip).limit(limit).all()
    
    for lookup in lookups:
        if lookup.geojson_data:
            lookup.geojson_data = json.loads(lookup.geojson_data)
        if lookup.additional_restrictions:
            try:
                lookup.interpreted_data = json.loads(lookup.additional_restrictions)
            except:
                lookup.interpreted_data = None
    
    return lookups


async def perform_detailed_analysis(
    lookup_id: int,
    address: str,
    lat: float,
    lon: float,
    municipality: Optional[str],
    state: Optional[str]
):
    """
    Perform detailed zoning analysis in the background.
    """
    from app.models.database import SessionLocal
    
    db = SessionLocal()
    try:
        lookup = db.query(ZoningLookup).filter(ZoningLookup.id == lookup_id).first()
        if not lookup:
            return
        
        # Use default municipality/state if not provided
        if not municipality or not state:
            # This could be enhanced with reverse geocoding
            municipality = "Unknown"
            state = "Unknown"
        
        # Scrape municipal data
        async with MunicipalDataScraper() as scraper:
            zoning_data = await scraper.scrape_zoning_code(municipality, state, lat, lon)
            permit_data = await scraper.scrape_permit_requirements(municipality, state)
            
            if zoning_data:
                lookup.zoning_code = zoning_data.get("zoning_code")
                lookup.zoning_description = zoning_data.get("description")
                lookup.setback_requirements = zoning_data.get("setbacks")
                lookup.height_restrictions = zoning_data.get("height_limits")
                lookup.lot_coverage = zoning_data.get("coverage")
            
            if permit_data:
                lookup.permit_process = json.dumps(permit_data)
        
        # AI Interpretation
        ai_service = AIInterpretationService()
        raw_data = {
            "zoning_code": lookup.zoning_code,
            "zoning_description": lookup.zoning_description,
            "setbacks": lookup.setback_requirements,
            "height_limits": lookup.height_restrictions,
            "coverage": lookup.lot_coverage,
            "permit_data": permit_data if permit_data else {}
        }
        
        interpreted = await ai_service.interpret_zoning_data(raw_data)
        lookup.additional_restrictions = json.dumps(interpreted)
        
        db.commit()
        
    except Exception as e:
        print(f"Error in detailed analysis: {e}")
    finally:
        db.close()
