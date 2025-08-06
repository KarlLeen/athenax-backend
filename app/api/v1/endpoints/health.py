from fastapi import APIRouter, Request
from app.middleware.rate_limiter import limiter

router = APIRouter()


@router.get("/")
@limiter.limit("120/minute")
async def health_check(request: Request):
    """
    Health check endpoint for monitoring.
    
    This simple endpoint returns a 200 OK response when the API is running normally.
    Used for monitoring, load balancer checks, and deployment verification.
    """
    return {"status": "ok", "message": "Service is up and running"}
