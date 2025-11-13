from sqlalchemy import Column, Integer, String, Boolean
from .base import Base

class Empleado(Base):
    __tablename__ = "empleado"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(150), nullable=False)
    apellido = Column(String(150), nullable=False)
    telefono = Column(Integer, nullable=False)
    puesto = Column(String(50), nullable=False)
    salario = Column(Integer, nullable=False)
    habilitado = Column(Boolean, nullable=False)