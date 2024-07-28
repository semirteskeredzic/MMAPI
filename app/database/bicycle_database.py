from ..models import bicycles

def get_bicycles():
    return bicycles.bicycleMockData

def get_bicycles_by_id(bicycle_id: int):
    for bicycle in bicycles.bicycleMockData:
        if bicycle.id == bicycle_id:
            return bicycle
    return None
        
def update_bicycle_price(bicycle_id: int, new_price: float):
    bicycle = get_bicycles_by_id(bicycle_id)
    if bicycle:
        bicycle.price = new_price
        return bicycle
    return None