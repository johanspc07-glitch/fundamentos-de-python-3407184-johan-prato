from pydantic import BaseModel, computed_field
from .transsacion import Transsacion
from .clientes import Cliente
from datetime import datetime

class FacturaBase(BaseModel):
    fecha: str = datetime.now()
    cliente: Cliente
    transsaciones: list[Transsacion] = []

    @computed_field
    @property
    def vr_total(self) -> float:
        factura_id_actual = getattr(self, 'id', None)
        total_factura = 0.0
        if not factura_id_actual or not self.transsaciones: 
            return total_factura


        for transsacion in self.transsaciones:
            if transsacion.factura_id == factura_id_actual:
                total_factura += transsacion.vr_unitario * transsacion.cantidad
                
        return total_factura

class FacturaCrear(FacturaBase):
    pass

class FacturaEditar(FacturaBase):
    pass

class Factura(FacturaBase):
    id: int | None = None
