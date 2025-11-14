from sqlalchemy import Column, Integer, String, Boolean
from .base import Base

class Descuento(Base):
    __tablename__ = "descuento"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(250), nullable=False)
    porcentaje = Column(Integer, nullable=False)
    habilitado = Column(Boolean, nullable=False)