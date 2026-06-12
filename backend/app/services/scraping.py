import asyncio
import aiohttp
from bs4 import BeautifulSoup
from typing import Optional, Dict, List
import logging
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MunicipalDataScraper:
    """
    Scrapes municipal zoning data from various sources including:
    - County assessor websites
    - Municipal zoning portals
    - GIS data portals
    """
    
    def __init__(self):
        self.session = None
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    async def __aenter__(self):
        self.session = aiohttp.ClientSession(headers=self.headers)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    async def scrape_county_assessor(self, county: str, state: str, address: str) -> Optional[Dict]:
        """
        Scrape county assessor data for a property.
        This is a template method that would need to be customized per county.
        """
        try:
            # Example: Generic assessor URL pattern
            # This would need to be customized for each county's specific system
            url = f"https://assessor.{county.lower()}.{state.lower()}.gov/property"
            
            async with self.session.get(url, params={"address": address}) as response:
                if response.status == 200:
                    html = await response.text()
                    soup = BeautifulSoup(html, 'lxml')
                    
                    # Extract property data (this is a template)
                    data = {
                        "parcel_id": self._extract_text(soup, "parcel-id"),
                        "zoning_code": self._extract_text(soup, "zoning"),
                        "lot_size": self._extract_text(soup, "lot-size"),
                        "building_area": self._extract_text(soup, "building-area"),
                        "year_built": self._extract_text(soup, "year-built"),
                    }
                    
                    logger.info(f"Successfully scraped assessor data for {address}")
                    return data
            
            return None
            
        except Exception as e:
            logger.error(f"Error scraping assessor data: {e}")
            return None
    
    async def scrape_zoning_code(self, municipality: str, state: str, lat: float, lon: float) -> Optional[Dict]:
        """
        Scrape zoning codes from municipal portals.
        """
        try:
            # This would connect to municipal GIS APIs or web portals
            # Example implementation for a generic system
            
            # Try to find zoning via GIS API first
            gis_data = await self._query_gis_api(municipality, state, lat, lon)
            if gis_data:
                return gis_data
            
            # Fallback to web scraping
            url = f"https://www.{municipality.lower()}.{state.lower()}.gov/zoning"
            async with self.session.get(url) as response:
                if response.status == 200:
                    html = await response.text()
                    soup = BeautifulSoup(html, 'lxml')
                    
                    zoning_data = {
                        "zoning_code": self._extract_zoning_code(soup),
                        "description": self._extract_zoning_description(soup),
                        "setbacks": self._extract_setbacks(soup),
                        "height_limits": self._extract_height_limits(soup),
                        "coverage": self._extract_coverage(soup),
                    }
                    
                    return zoning_data
            
            return None
            
        except Exception as e:
            logger.error(f"Error scraping zoning code: {e}")
            return None
    
    async def scrape_permit_requirements(self, municipality: str, state: str) -> Optional[Dict]:
        """
        Scrape permit process and requirements from municipal websites.
        """
        try:
            url = f"https://www.{municipality.lower()}.{state.lower()}.gov/permits"
            async with self.session.get(url) as response:
                if response.status == 200:
                    html = await response.text()
                    soup = BeautifulSoup(html, 'lxml')
                    
                    permit_data = {
                        "process_steps": self._extract_permit_process(soup),
                        "required_documents": self._extract_required_docs(soup),
                        "fees": self._extract_fees(soup),
                        "timeline": self._extract_timeline(soup),
                    }
                    
                    return permit_data
            
            return None
            
        except Exception as e:
            logger.error(f"Error scraping permit requirements: {e}")
            return None
    
    async def _query_gis_api(self, municipality: str, state: str, lat: float, lon: float) -> Optional[Dict]:
        """
        Query municipal GIS APIs for zoning information.
        Many counties have ArcGIS REST APIs or similar.
        """
        try:
            # Example ArcGIS REST API query
            # This would need to be customized per municipality
            gis_url = f"https://gis.{municipality.lower()}.{state.lower()}.gov/arcgis/rest/services/Zoning/MapServer/0/query"
            
            params = {
                "geometry": f"{lon},{lat}",
                "geometryType": "esriGeometryPoint",
                "inSR": "4326",
                "spatialReference": {"wkid": 4326},
                "outFields": "*",
                "returnGeometry": "true",
                "f": "json"
            }
            
            async with self.session.get(gis_url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    if data.get("features"):
                        return self._parse_gis_response(data)
            
            return None
            
        except Exception as e:
            logger.error(f"Error querying GIS API: {e}")
            return None
    
    def _parse_gis_response(self, data: Dict) -> Dict:
        """Parse GIS API response into standardized format."""
        feature = data["features"][0]
        attributes = feature.get("attributes", {})
        geometry = feature.get("geometry", {})
        
        return {
            "zoning_code": attributes.get("ZONE_CODE", ""),
            "description": attributes.get("ZONE_DESC", ""),
            "setbacks": attributes.get("SETBACK", ""),
            "height_limits": attributes.get("HEIGHT_LIM", ""),
            "coverage": attributes.get("LOT_COVER", ""),
            "geometry": geometry,
            "raw_gis_data": data
        }
    
    def _extract_text(self, soup, class_name: str) -> str:
        """Helper to extract text by class name."""
        element = soup.find(class_=class_name)
        return element.get_text(strip=True) if element else ""
    
    def _extract_zoning_code(self, soup) -> str:
        """Extract zoning code from page."""
        # This would need customization per site
        zoning_section = soup.find("div", {"id": "zoning-code"})
        return zoning_section.get_text(strip=True) if zoning_section else ""
    
    def _extract_zoning_description(self, soup) -> str:
        """Extract zoning description."""
        desc_section = soup.find("div", {"id": "zoning-description"})
        return desc_section.get_text(strip=True) if desc_section else ""
    
    def _extract_setbacks(self, soup) -> str:
        """Extract setback requirements."""
        setback_section = soup.find("div", {"id": "setbacks"})
        return setback_section.get_text(strip=True) if setback_section else ""
    
    def _extract_height_limits(self, soup) -> str:
        """Extract height limits."""
        height_section = soup.find("div", {"id": "height-limits"})
        return height_section.get_text(strip=True) if height_section else ""
    
    def _extract_coverage(self, soup) -> str:
        """Extract lot coverage requirements."""
        coverage_section = soup.find("div", {"id": "lot-coverage"})
        return coverage_section.get_text(strip=True) if coverage_section else ""
    
    def _extract_permit_process(self, soup) -> List[str]:
        """Extract permit process steps."""
        steps = []
        process_section = soup.find("div", {"id": "permit-process"})
        if process_section:
            for li in process_section.find_all("li"):
                steps.append(li.get_text(strip=True))
        return steps
    
    def _extract_required_docs(self, soup) -> List[str]:
        """Extract required documents."""
        docs = []
        docs_section = soup.find("div", {"id": "required-documents"})
        if docs_section:
            for li in docs_section.find_all("li"):
                docs.append(li.get_text(strip=True))
        return docs
    
    def _extract_fees(self, soup) -> str:
        """Extract fee information."""
        fee_section = soup.find("div", {"id": "fees"})
        return fee_section.get_text(strip=True) if fee_section else ""
    
    def _extract_timeline(self, soup) -> str:
        """Extract timeline information."""
        timeline_section = soup.find("div", {"id": "timeline"})
        return timeline_section.get_text(strip=True) if timeline_section else ""
