from sqlalchemy.orm import Session
from app.models.key_value import KeyValue
from app.schemas.key_value import KeyValueCreate

class KeyValueRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, key_value: KeyValueCreate):
        db_key_value = KeyValue(**key_value.dict())
        self.db.add(db_key_value)
        self.db.commit()
        self.db.refresh(db_key_value)
        return db_key_value

    def get(self, key: str):
        return self.db.query(KeyValue).filter(KeyValue.key == key).first()
