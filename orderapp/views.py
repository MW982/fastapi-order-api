from fastapi import APIRouter 


router = APIRouter(tags=["Orders"], prefix="/order")


@router.post("/process")
async def process_order():
    return {}


@router.get("/details")
async def get_details():
    return {}


@router.get("/list")
async def list():
    return {}

