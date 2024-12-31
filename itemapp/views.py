from fastapi import APIRouter 


router = APIRouter(tags=["Items"], prefix="/items")


@router.get("/list")
async def list():
    return {}


@router.get("/{item_id}")
async def get_item(item_id: int):
    return {}

