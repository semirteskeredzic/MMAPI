from fastapi import FastAPI, HTTPException
from .database.bicycle_database import get_bicycles, get_bicycles_by_id, update_bicycle_price
from .schemas.bicycle_schema import BicycleBase, BicycleDetail, PriceUpdate

app = FastAPI()

# This endpoint returns all bicycles with three properties of the bicycles model in response

@app.get("/", response_model=list[BicycleBase])
async def getcycles():
    bicycles = get_bicycles()
    return [{"id": b.id, "name": b.name, "description": b.description} for b in bicycles]

# This endpoint returns specific bicycle with all properties of the bicycle model in response

@app.get("/bicycle/{id}", response_model=BicycleDetail)
async def getcycledetail(id: int):
    bicycle = get_bicycles_by_id(id)
    if not bicycle:
        raise HTTPException(status_code=404, detail="Bicycle not found")
    return bicycle

# This endpoint returns the updated price in response

@app.post("/bicycle/update_price/{id}", response_model=PriceUpdate)
async def updatecycleprice(id: int, newprice: PriceUpdate):
    bicycle = update_bicycle_price(id, newprice.price)
    if not bicycle:
        raise HTTPException(status_code=404, detail="Bicycle not found")
    return bicycle
