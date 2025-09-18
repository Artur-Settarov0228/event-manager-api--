from fastapi import APIRouter


router = APIRouter(
    prefix="/events",
    tags=["events"]
)

@router.get("/")
async def read_users():
    return []