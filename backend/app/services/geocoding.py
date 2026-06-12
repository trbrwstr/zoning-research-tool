from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import asyncio
from typing import Optional, Tuple
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class GeocodingService:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="zoning_research_tool")
    
    async def geocode_address(self, address: str) -> Optional[Tuple[float, float, dict]]:
        """
        Convert an address to latitude, longitude, and additional location data.
        
        Args:
            address: The address string to geocode
            
        Returns:
            Tuple of (latitude, longitude, location_data) or None if geocoding fails
        """
        try:
            # Run geocoding in thread pool to avoid blocking
            loop = asyncio.get_event_loop()
            location = await loop.run_in_executor(
                None, 
                lambda: self.geolocator.geocode(address, exactly_one=True)
            )
            
            if location:
                logger.info(f"Successfully geocoded address: {address}")
                return (
                    location.latitude,
                    location.longitude,
                    {
                        "address": location.address,
                        "raw": location.raw
                    }
                )
            else:
                logger.warning(f"Geocoding failed for address: {address}")
                return None
                
        except GeocoderTimedOut:
            logger.error(f"Geocoding timed out for address: {address}")
            return None
        except GeocoderServiceError as e:
            logger.error(f"Geocoding service error for address {address}: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error geocoding address {address}: {e}")
            return None
    
    async def reverse_geocode(self, lat: float, lon: float) -> Optional[str]:
        """
        Convert coordinates back to an address.
        
        Args:
            lat: Latitude
            lon: Longitude
            
        Returns:
            Address string or None if reverse geocoding fails
        """
        try:
            loop = asyncio.get_event_loop()
            location = await loop.run_in_executor(
                None,
                lambda: self.geolocator.reverse((lat, lon), exactly_one=True)
            )
            
            if location:
                return location.address
            return None
            
        except Exception as e:
            logger.error(f"Error reverse geocoding ({lat}, {lon}): {e}")
            return None
