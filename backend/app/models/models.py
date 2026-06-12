from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models.database import Base


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    stripe_customer_id = Column(String, nullable=True)
    
    lookups = relationship("ZoningLookup", back_populates="user")
    subscription = relationship("Subscription", back_populates="user", uselist=False)


class ZoningLookup(Base):
    __tablename__ = "zoning_lookups"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    address = Column(String, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    zoning_code = Column(String)
    zoning_description = Column(Text)
    setback_requirements = Column(Text)
    height_restrictions = Column(Text)
    lot_coverage = Column(Text)
    parking_requirements = Column(Text)
    permit_process = Column(Text)
    additional_restrictions = Column(Text)
    raw_data = Column(Text)
    geojson_data = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="lookups")


class Subscription(Base):
    __tablename__ = "subscriptions"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    stripe_subscription_id = Column(String, nullable=True)
    plan_type = Column(String)  # "monthly" or "per_lookup"
    status = Column(String)  # "active", "cancelled", "past_due"
    lookups_remaining = Column(Integer, default=0)
    current_period_start = Column(DateTime)
    current_period_end = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="subscription")
