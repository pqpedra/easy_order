from pydantic import BaseModel, Field

#-------- Tables ----------
class TableCreate(BaseModel):
    number: int = Field(gt=0)
    status: str = "Free"

class TableUpdate(BaseModel):
    status: str

class TableOut(BaseModel):
    number: int
    status: str