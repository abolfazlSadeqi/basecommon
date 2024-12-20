from pydantic import BaseModel


class KeyValueCreate(BaseModel):
    key: str
    value: str
    title: str
