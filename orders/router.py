from fastapi import APIRouter, HTTPException
from ..orders import services as order_service

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/")
def place_order(product_id: int, quantity: int):
    result = order_service.create_order(product_id, quantity)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result
