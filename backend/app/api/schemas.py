from pydantic import BaseModel, EmailStr
from typing import Optional, List, Dict
from datetime import datetime


class ZoningLookupRequest(BaseModel):
    address: str
    municipality: Optional[str] = None
    state: Optional[str] = None


class ZoningLookupResponse(BaseModel):
    id: int
    address: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    zoning_code: Optional[str] = None
    zoning_description: Optional[str] = None
    setback_requirements: Optional[str] = None
    height_restrictions: Optional[str] = None
    lot_coverage: Optional[str] = None
    parking_requirements: Optional[str] = None
    permit_process: Optional[str] = None
    additional_restrictions: Optional[str] = None
    map_url: Optional[str] = None
    geojson_data: Optional[Dict] = None
    interpreted_data: Optional[Dict] = None
    created_at: datetime
    
    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    email: str
    full_name: Optional[str] = None
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True


class SubscriptionCreate(BaseModel):
    plan_type: str  # "monthly" or "per_lookup"


class SubscriptionResponse(BaseModel):
    id: int
    plan_type: str
    status: str
    lookups_remaining: int
    current_period_start: Optional[datetime] = None
    current_period_end: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class PricingInfo(BaseModel):
    price_per_lookup: float
    monthly_subscription_price: float
    monthly_lookups_included: int
