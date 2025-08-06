from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
    Request
)
from typing import List, Optional

from app.middleware.rate_limiter import limiter
from app.core.dependencies import get_current_user
# TODO: Import appropriate schemas and models

# TODO: Import appropriate services and dependencies

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
@limiter.limit("10/minute")
async def create_hackathon(
    request: Request,
    # TODO: Replace with actual schema
    # data: HackathonCreate,
    # current_user: User = Depends(get_current_user),
    # service: HackathonService = Depends(get_hackathon_service)
):
    """
    Create a new hackathon (Organizer only).
    
    This endpoint allows authorized organizers to create a new hackathon event
    with all necessary details including name, description, timeline, rules, etc.
    """
    # TODO: Implement hackathon creation
    # TODO: Verify user has organizer role
    # TODO: Create new hackathon record
    # TODO: Store relevant data on IPFS if needed
    # TODO: Return created hackathon details
    pass


@router.get("/")
@limiter.limit("60/minute")
async def list_hackathons(
    request: Request,
    # TODO: Add filter parameters 
    # status: Optional[str] = None,
    # page: int = 1,
    # limit: int = 10,
    # service: HackathonService = Depends(get_hackathon_service)
):
    """
    Discover all active and upcoming hackathons.
    
    This endpoint returns a paginated list of hackathons that can be filtered
    by status (upcoming, active, judging, completed, archived).
    """
    # TODO: Implement hackathon listing logic
    # TODO: Apply filters based on query parameters
    # TODO: Return paginated list of hackathons
    pass


@router.get("/{hackathon_id}")
@limiter.limit("60/minute")
async def get_hackathon(
    request: Request,
    hackathon_id: str,
    # service: HackathonService = Depends(get_hackathon_service)
):
    """
    Get detailed information for a single hackathon.
    
    Returns comprehensive details about a specific hackathon including
    description, timeline, rules, prizes, judges, etc.
    """
    # TODO: Implement get hackathon details
    # TODO: Return hackathon details or 404
    pass


@router.patch("/{hackathon_id}")
@limiter.limit("20/minute")
async def update_hackathon(
    request: Request,
    hackathon_id: str,
    # data: HackathonUpdate,
    # current_user: User = Depends(get_current_user),
    # service: HackathonService = Depends(get_hackathon_service)
):
    """
    Update hackathon details (Organizer only).
    
    Allows organizers to modify details of an existing hackathon.
    """
    # TODO: Implement hackathon update logic
    # TODO: Verify user has organizer role and is authorized for this hackathon
    # TODO: Update hackathon details
    # TODO: Return updated hackathon
    pass


@router.get("/{hackathon_id}/projects")
@limiter.limit("60/minute")
async def list_hackathon_projects(
    request: Request,
    hackathon_id: str,
    # page: int = 1,
    # limit: int = 10,
    # service: HackathonService = Depends(get_hackathon_service)
):
    """
    View all projects submitted to a hackathon.
    
    Returns a paginated list of all projects submitted to a specific hackathon.
    """
    # TODO: Implement project listing by hackathon
    # TODO: Return paginated list of projects
    pass
