from fastapi import APIRouter, HTTPException, status
from app.enrutadores.clientes import lista_clientes
from modelos.facturas import Factura, FacturaCrear, FacturaEditar

rutas_facturas = APIRouter()
lista_facturas: list[Factura] = []

# facturas

@rutas_facturas.get("/facturas", response_model=list[Factura])
async def lista_facturas():
    return lista_facturas

@rutas_facturas.get("/facturas/{factura_id}", response_model=Factura)
async def obtener_factura(factura_id: int):
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == factura_id:
            return obj_factura
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Factura con id {factura_id} no existe")

@rutas_facturas.post("/facturas", response_model=Factura)
async def crear_factura(datos_factura: FacturaCrear):
    for cliente in lista_clientes:
        if cliente.id == cliente.id:
            cliente_encontrado = cliente

    if not cliente_encontrado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Cliente con id {datos_factura.cliente.id} no existe")
    

    factura_val = Factura.model_validate(datos_factura.model_dump())
    factura_val.cliente = cliente_encontrado
    factura_val.id = len(lista_facturas)+1
    lista_facturas.append(factura_val)
    return factura_val

@rutas_facturas.patch("/facturas/{factura_id}", response_model=Factura)
async def editar_factura(factura_id: int, datos_factura: FacturaEditar):
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == factura_id:
            factura_val = Factura.model_validate(datos_factura.model_dump())
            factura_val.id = factura_id
            lista_facturas[i] = factura_val
            return factura_val
    raise HTTPException(status_code=400, detail=f"Factura con id {factura_id} no existe")

@rutas_facturas.delete("/facturas/{factura_id}", response_model=Factura)
async def eliminar_factura(factura_id: int):
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == factura_id:
            factura_eliminada = lista_facturas.pop(i)
            return factura_eliminada
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Factura con id {factura_id} no existe")


