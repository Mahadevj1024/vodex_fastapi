from pydantic import BaseModel
from datetime import datetime

class ItemCreate(BaseModel):
    name: str
    email: str
    item_name: str
    quantity: int
    expiry_date: datetime

class ItemResponse(ItemCreate):
    id: str
    insert_date: datetime
