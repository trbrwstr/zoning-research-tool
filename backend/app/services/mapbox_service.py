import requests
from typing import Dict, Optional, List
import logging
from app.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MapboxService:
    """
    Handles Mapbox integration for property visualization and mapping.
    """
    
    def __init__(self):
        self.access_token = settings.MAPBOX_ACCESS_TOKEN
        self.base_url = "https://api.mapbox.com"
    
    def generate_static_map(
        self, 
        lat: float, 
        lon: float, 
        zoom: int = 15,
        width: int = 800,
        height: int = 600,
        style: str = "mapbox/streets-v12"
    ) -> Optional[str]:
        """
        Generate a static map image for the property location.
        
        Args:
            lat: Latitude
            lon: Longitude
            zoom: Zoom level (1-22)
            width: Image width in pixels
            height: Image height in pixels
            style: Map style
            
        Returns:
            URL to the static map image
        """
        try:
            url = f"{self.base_url}/styles/v1/{style}/static/{lon},{lat},{zoom}/{width}x{height}"
            params = {
                "access_token": self.access_token,
                "markers": f"pin-l-circle+285A98({lon},{lat})"
            }
            
            response = requests.get(url, params=params)
            if response.status_code == 200:
                map_url = response.url
                logger.info(f"Generated static map for ({lat}, {lon})")
                return map_url
            else:
                logger.error(f"Failed to generate static map: {response.status_code}")
                return None
                
        except Exception as e:
            logger.error(f"Error generating static map: {e}")
            return None
    
    def generate_geojson_property_boundary(
        self, 
        lat: float, 
        lon: float,
        radius: float = 0.0005
    ) -> Dict:
        """
        Generate a simplified GeoJSON property boundary.
        In production, this would query actual parcel boundaries from GIS data.
        
        Args:
            lat: Center latitude
            lon: Center longitude
            radius: Radius in degrees (approximate)
            
        Returns:
            GeoJSON FeatureCollection
        """
        try:
            # Simplified square boundary (in production, use actual parcel data)
            coordinates = [
                [
                    [lon - radius, lat + radius],
                    [lon + radius, lat + radius],
                    [lon + radius, lat - radius],
                    [lon - radius, lat - radius],
                    [lon - radius, lat + radius]
                ]
            ]
            
            geojson = {
                "type": "FeatureCollection",
                "features": [
                    {
                        "type": "Feature",
                        "properties": {
                            "name": "Property Boundary",
                            "description": "Approximate property boundary"
                        },
                        "geometry": {
                            "type": "Polygon",
                            "coordinates": coordinates
                        }
                    }
                ]
            }
            
            logger.info(f"Generated GeoJSON boundary for ({lat}, {lon})")
            return geojson
            
        except Exception as e:
            logger.error(f"Error generating GeoJSON boundary: {e}")
            return {"type": "FeatureCollection", "features": []}
    
    def generate_map_style_url(self, style: str = "mapbox/streets-v12") -> str:
        """
        Generate a Mapbox style URL for use in web applications.
        
        Args:
            style: Map style identifier
            
        Returns:
            Full style URL with access token
        """
        return f"https://api.mapbox.com/styles/v1/{style}?access_token={self.access_token}"
    
    def geocode_with_mapbox(self, address: str) -> Optional[Dict]:
        """
        Geocode an address using Mapbox Geocoding API.
        
        Args:
            address: Address string
            
        Returns:
            Dictionary with coordinates and place data
        """
        try:
            url = f"{self.base_url}/geocoding/v5/mapbox.places/{address}.json"
            params = {
                "access_token": self.access_token,
                "limit": 1
            }
            
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                if data.get("features"):
                    feature = data["features"][0]
                    center = feature.get("center", [])
                    if len(center) == 2:
                        return {
                            "longitude": center[0],
                            "latitude": center[1],
                            "place_name": feature.get("place_name", ""),
                            "context": feature.get("context", [])
                        }
            
            return None
            
        except Exception as e:
            logger.error(f"Error geocoding with Mapbox: {e}")
            return None
    
    def generate_directions(
        self, 
        origin: tuple, 
        destination: tuple,
        profile: str = "driving"
    ) -> Optional[Dict]:
        """
        Generate directions between two points.
        
        Args:
            origin: (longitude, latitude) of origin
            destination: (longitude, latitude) of destination
            profile: Route profile (driving, walking, cycling)
            
        Returns:
            Directions data
        """
        try:
            url = f"{self.base_url}/directions/v5/mapbox/{profile}/{origin[0]},{origin[1]};{destination[0]},{destination[1]}"
            params = {
                "access_token": self.access_token,
                "geometries": "geojson"
            }
            
            response = requests.get(url, params=params)
            if response.status_code == 200:
                return response.json()
            
            return None
            
        except Exception as e:
            logger.error(f"Error generating directions: {e}")
            return None
