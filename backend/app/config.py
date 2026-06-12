from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # API Keys
    OPENAI_API_KEY: str
    MAPBOX_ACCESS_TOKEN: str
    GEOCODING_API_KEY: Optional[str] = None
    
    # Database
    DATABASE_URL: str = "sqlite:///./zoning.db"
    
    # Application
    APP_NAME: str = "Zoning Research Tool"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    
    # Pricing
    PRICE_PER_LOOKUP: float = 9.99
    MONTHLY_SUBSCRIPTION_PRICE: float = 99.00
    
    # Stripe
    STRIPE_API_KEY: Optional[str] = None
    STRIPE_WEBHOOK_SECRET: Optional[str] = None
    
    # CORS
    CORS_ORIGINS: list = ["http://localhost:3000", "http://localhost:8000"]
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
