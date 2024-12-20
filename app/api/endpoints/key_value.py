from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.KeyValueCreate import KeyValueCreate
from app.schemas.key_value import KeyValue
from app.repositories.key_value import KeyValueRepository
from app.db.session import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=KeyValue)
def create_key_value(key_value: KeyValueCreate, db: Session = Depends(get_db)):
    repo = KeyValueRepository(db)
    return repo.create(key_value)


@router.get("/{key}", response_model=KeyValue)
def read_key_value(key: str, db: Session = Depends(get_db)):
    repo = KeyValueRepository(db)
    db_key_value = repo.get(key)
    if db_key_value is None:
        raise HTTPException(status_code=404, detail="Key not found")
    return db_key_value
