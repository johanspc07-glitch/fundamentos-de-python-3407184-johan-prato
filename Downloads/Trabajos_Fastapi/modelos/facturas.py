from pydantic import BaseModel

class FacturaBase(BaseModel):
    vr_total: float
    fecha: str
    cliente: Cliente

class FacturaCrear(FacturaBase):
    pass

class Factura(FacturaBase):
    id: int | None = None
