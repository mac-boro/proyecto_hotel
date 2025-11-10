from sqlalchemy import Column, Integer, String, Boolean
from .base import Base

class Huesped(Base):
    __tablename__ = "huesped"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(150), nullable=False)
    apellido = Column(String(150), nullable=False)
    telefono = Column(Integer, nullable=False)   
    email = Column(String(250), nullable=False)
    habilitado = Column(Boolean, nullable=False)