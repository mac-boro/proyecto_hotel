from sqlalchemy import Column, Integer, String, Boolean
from .base import Base

class Habitacion(Base):
    __tablename__ = "habitacion"

    id = Column(Integer, primary_key=True, autoincrement=True)
    numero = Column(Integer, nullable=False)
    tipo = Column(String(50), nullable=False)
    precio = Column(Integer, nullable=False)
    disponibilidad = Column(Boolean, nullable=False)
