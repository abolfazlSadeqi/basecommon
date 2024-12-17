from pydantic import BaseModel

class KeyValueCreate(BaseModel):
    key: str
    value: str
    title: str

class KeyValue(BaseModel):
    id: int
    key: str
    value: str
    title: str

class Config:
    orm_mode = True
