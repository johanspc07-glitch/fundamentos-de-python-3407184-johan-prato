from pydantic import BaseModel

class TranssacionBase(BaseModel):
    cantidad: int
    vr_unitario: float
    factura_id: int | None = None

class TranssacionCrear(TranssacionBase):
    pass

class TranssacionEditar(TranssacionBase):
    pass

class Transsacion(TranssacionBase):
    id: int | None = None
