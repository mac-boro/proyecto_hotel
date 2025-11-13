from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from .base import Base

class Pago(Base):
    __tablename__ = "pago"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_factura = Column(Integer, ForeignKey("factura.id"), nullable=False)
    metodo_pago = Column(String(50), nullable=False)
    fecha_pago = Column(DateTime, nullable=False)
    pendiente = Column(Boolean, nullable=False)
    habilitado = Column(Boolean, nullable=False)
