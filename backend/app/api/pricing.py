from fastapi import APIRouter
from app.api.schemas import PricingInfo
from app.config import settings

router = APIRouter(prefix="/api/pricing", tags=["pricing"])


@router.get("/info", response_model=PricingInfo)
def get_pricing_info():
    """
    Get current pricing information.
    """
    return PricingInfo(
        price_per_lookup=settings.PRICE_PER_LOOKUP,
        monthly_subscription_price=settings.MONTHLY_SUBSCRIPTION_PRICE,
        monthly_lookups_included=100
    )
