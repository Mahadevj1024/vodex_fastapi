from fastapi import APIRouter, HTTPException
from models.items import ItemCreate, ItemResponse
from database import MongoDB
from datetime import datetime
from bson import ObjectId

router = APIRouter()
db = MongoDB().get_items_collection()

@router.post("/items", response_model=ItemResponse)
async def create_item(item: ItemCreate):
    item_dict = item.model_dump()
    item_dict["insert_date"] = datetime.now()
    result = db.insert_one(item_dict)
    return {**item_dict, "id": str(result.inserted_id)}

@router.get("/items/{item_id}", response_model=ItemResponse)
async def read_item(item_id: str):
    item = db.find_one({"_id": ObjectId(item_id)})
    if item:
        return {**item, "id": str(item["_id"])}
    raise HTTPException(status_code=404, detail="Item not found")

@router.get("/items/filter")
async def filter_items(email: str = None, expiry_date: str = None, insert_date: str = None, quantity: int = None):
    query = {}
    if email:
        query["email"] = email
    if expiry_date:
        query["expiry_date"] = {"$gt": datetime.fromisoformat(expiry_date)}
    if insert_date:
        query["insert_date"] = {"$gt": datetime.fromisoformat(insert_date)}
    if quantity is not None:
        query["quantity"] = {"$gte": quantity}

    items = list(db.find(query))
    return [{"id": str(item["_id"]), **item} for item in items]

@router.delete("/items/{item_id}")
async def delete_item(item_id: str):
    result = db.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count == 1:
        return {"detail": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")

@router.put("/items/{item_id}", response_model=ItemResponse)
async def update_item(item_id: str, item: ItemCreate):
    update_data = item.model_dump(exclude={"insert_date"})
    result = db.update_one({"_id": ObjectId(item_id)}, {"$set": update_data})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    updated_item = db.find_one({"_id": ObjectId(item_id)})
    return {**updated_item, "id": str(updated_item["_id"])}
