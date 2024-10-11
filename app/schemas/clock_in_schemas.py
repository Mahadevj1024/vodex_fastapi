from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ClockInBase(BaseModel):
    email: str
    location: str

class ClockInCreate(ClockInBase):
    pass

class ClockInUpdate(ClockInBase):
    pass

class ClockInResponse(ClockInBase):
    id: str
    insert_datetime: datetime
