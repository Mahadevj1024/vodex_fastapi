from fastapi import APIRouter, HTTPException
from app.models.clock_in import ClockInCreate, ClockInResponse
from app.database import MongoDB
from datetime import datetime
from bson import ObjectId

router = APIRouter()
db = MongoDB().get_clock_in_collection()

@router.post("/clock-in", response_model=ClockInResponse)
async def create_clock_in(clock_in: ClockInCreate):
    clock_in_dict = clock_in.model_dump()
    clock_in_dict["insert_datetime"] = datetime.now()
    result = db.insert_one(clock_in_dict)
    return {**clock_in_dict, "id": str(result.inserted_id)}

@router.get("/clock-in/{clock_in_id}", response_model=ClockInResponse)
async def read_clock_in(clock_in_id: str):
    clock_in = db.find_one({"_id": ObjectId(clock_in_id)})
    if clock_in:
        return {**clock_in, "id": str(clock_in["_id"])}
    raise HTTPException(status_code=404, detail="Clock-in record not found")

@router.get("/clock-in/filter")
async def filter_clock_ins(email: str = None, location: str = None, insert_datetime: str = None):
    query = {}
    if email:
        query["email"] = email
    if location:
        query["location"] = location
    if insert_datetime:
        query["insert_datetime"] = {"$gt": datetime.fromisoformat(insert_datetime)}

    clock_ins = list(db.find(query))
    return [{"id": str(clock_in["_id"]), **clock_in} for clock_in in clock_ins]

@router.delete("/clock-in/{clock_in_id}")
async def delete_clock_in(clock_in_id: str):
    result = db.delete_one({"_id": ObjectId(clock_in_id)})
    if result.deleted_count == 1:
        return {"detail": "Clock-in record deleted"}
    raise HTTPException(status_code=404, detail="Clock-in record not found")

@router.put("/clock-in/{clock_in_id}", response_model=ClockInResponse)
async def update_clock_in(clock_in_id: str, clock_in: ClockInCreate):
    update_data = clock_in.model_dump(exclude={"insert_datetime"})
    result = db.update_one({"_id": ObjectId(clock_in_id)}, {"$set": update_data})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Clock-in record not found")
    updated_clock_in = db.find_one({"_id": ObjectId(clock_in_id)})
    return {**updated_clock_in, "id": str(updated_clock_in["_id"])}
