from sqlalchemy import Column, Integer, String
from app.db.base_class import Base


class KeyValue(Base):
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String)
    value = Column(String)
    title = Column(String)
