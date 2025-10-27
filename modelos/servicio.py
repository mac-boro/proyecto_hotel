from sqlalchemy import Column, Integer, String
from .base import Base

class Servicio(Base):
    __tablename__ = "servicio"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(150), nullable=False)
    precio = Column(Integer, nullable=False)   
