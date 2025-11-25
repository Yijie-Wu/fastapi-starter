from fastapi import APIRouter


router = APIRouter()


@router.get("/health-check",status_code=204, summary="Health Check")
async def health_check():
    return
