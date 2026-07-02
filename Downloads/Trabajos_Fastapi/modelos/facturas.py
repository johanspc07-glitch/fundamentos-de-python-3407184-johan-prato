from pydantic import BaseModel
from clientes import Cliente

class FacturaBase(BaseModel):
    vr_total: float
    fecha: str
    cliente: Cliente

class FacturaCrear(FacturaBase):
    pass

class FacturaEditar(FacturaBase):
    pass

class Factura(FacturaBase):
    id: int | None = None
