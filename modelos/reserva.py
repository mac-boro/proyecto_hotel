from sqlalchemy import Column, Integer, DateTime, ForeignKey
from .base import Base

class Reserva(Base):
    __tablename__ = "reserva"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_huesped = Column(Integer, ForeignKey("huesped.id"), nullable=False)
    id_habitacion = Column(Integer, ForeignKey("habitacion.id"), nullable=False)
    id_descuento = Column(Integer, ForeignKey("descuento.id"), nullable=False)  
    id_servicio = Column(Integer, ForeignKey("servicio.id"), nullable=False)   
    fecha_entrada = Column(DateTime, nullable=False)
    fecha_salida = Column(DateTime, nullable=False)
    total = Column(Integer, nullable=False)
