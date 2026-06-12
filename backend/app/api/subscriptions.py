from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from app.models.database import get_db
from app.models.models import User, Subscription
from app.api.schemas import SubscriptionCreate, SubscriptionResponse
from app.config import settings

router = APIRouter(prefix="/api/subscriptions", tags=["subscriptions"])


@router.post("/create", response_model=SubscriptionResponse)
def create_subscription(
    subscription: SubscriptionCreate,
    user_id: int,
    db: Session = Depends(get_db)
):
    """
    Create a new subscription for a user.
    """
    # Check if user exists
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Check if user already has an active subscription
    existing = db.query(Subscription).filter(
        Subscription.user_id == user_id,
        Subscription.status == "active"
    ).first()
    
    if existing:
        raise HTTPException(status_code=400, detail="User already has an active subscription")
    
    # Create subscription
    now = datetime.utcnow()
    period_end = now + timedelta(days=30)
    
    new_subscription = Subscription(
        user_id=user_id,
        plan_type=subscription.plan_type,
        status="active",
        lookups_remaining=100 if subscription.plan_type == "monthly" else 0,
        current_period_start=now,
        current_period_end=period_end
    )
    
    db.add(new_subscription)
    db.commit()
    db.refresh(new_subscription)
    
    return new_subscription


@router.get("/user/{user_id}", response_model=SubscriptionResponse)
def get_user_subscription(user_id: int, db: Session = Depends(get_db)):
    """
    Get a user's subscription.
    """
    subscription = db.query(Subscription).filter(
        Subscription.user_id == user_id,
        Subscription.status == "active"
    ).first()
    
    if not subscription:
        raise HTTPException(status_code=404, detail="No active subscription found")
    
    return subscription
