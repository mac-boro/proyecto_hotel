from sqlalchemy import Column, Integer, ForeignKey
from .base import Base

class Factura(Base):
    __tablename__ = "factura"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_reserva = Column(Integer, ForeignKey("reserva.id"), nullable=False)
