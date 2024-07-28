from pydantic import BaseModel

class BicycleBase(BaseModel):
    id: int
    name: str
    description: str

class BicycleDetail(BaseModel):
    id: int
    name: str
    type: str
    description: str
    brand: str
    price: float

class PriceUpdate(BaseModel):
    price: float