from pydantic import BaseModel

class KeyValue(BaseModel):
    id: int
    key: str
    value: str
    title: str


