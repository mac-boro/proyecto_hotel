from sqlalchemy import Column, Integer, String
from .base import Base

class Hotel(Base):
    __tablename__ = "hotel"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(250), nullable=False)
    direccion = Column(String(250), nullable=False)

