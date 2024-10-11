from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class ItemBase(BaseModel):
    name: str
    email: str
    item_name: str
    quantity: int
    expiry_date: date

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: str
    insert_date: date
