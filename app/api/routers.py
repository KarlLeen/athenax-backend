from fastapi import APIRouter
from app.api.v1.endpoints import (
    # Original endpoints
    user,
    email,
    storj,
    article,
    wishlist,
    # HackX Buildathon endpoints
    hackathons,
    projects,
    teams,
    auth,
    ipfs,
    health
)
from app.api.v1.endpoints.submit import audit, research

api_router = APIRouter()

api_router.include_router(
    audit.router,
    prefix="/audit",
    tags=["Audit"]
)

api_router.include_router(
    research.router,
    prefix="/research",
    tags=["Research"]
)

api_router.include_router(
    article.router,
    prefix="/article",
    tags=["Article"]
)

api_router.include_router(
    user.router,
    prefix="/users",
    tags=["users"]
)

api_router.include_router(
    email.router,
    prefix="/email",
    tags=["Email"]
)

api_router.include_router(
    storj.router,
    prefix="/s3",
    tags=["Data storage"]
)

api_router.include_router(
    wishlist.router,
    prefix="/wishlist",
    tags=["Wishlist"]
)

# HackX Buildathon API Routes
api_router.include_router(
    auth.router,
    prefix="/auth",
    tags=["Authentication"]
)

api_router.include_router(
    hackathons.router,
    prefix="/hackathons",
    tags=["Hackathons"]
)

api_router.include_router(
    projects.router,
    prefix="/projects",
    tags=["Projects"]
)

api_router.include_router(
    teams.router,
    prefix="/teams",
    tags=["Teams"]
)

api_router.include_router(
    ipfs.router,
    prefix="/ipfs",
    tags=["IPFS Storage"]
)

# System Routes
api_router.include_router(
    health.router,
    prefix="/health",
    tags=["System"]
)
