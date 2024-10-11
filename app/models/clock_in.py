from pydantic import BaseModel
from datetime import datetime

class ClockInCreate(BaseModel):
    email: str
    location: str

class ClockInResponse(ClockInCreate):
    id: str
    insert_datetime: datetime
