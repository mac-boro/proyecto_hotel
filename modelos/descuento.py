from sqlalchemy import Column, Integer, String, Boolean
from .base import Base

class Descuento(Base):
    __tablename__ = "descuento"

    id = Column(Integer, primary_key=True, autoincrement=True)
    porcentaje = Column(Integer, nullable=False)
    descripcion = Column(String(250), nullable=False)
    habilitado = Column(Boolean, nullable=False)