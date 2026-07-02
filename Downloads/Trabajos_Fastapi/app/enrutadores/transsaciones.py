from fastapi import APIRouter, HTTPException, status
from ..modelos.facturas import Factura
from ..modelos.transsacion import Transsacion, TranssacionCrear, TranssacionEditar
from ..listas import lista_transsaciones, lista_facturas

rutas_transsaciones = APIRouter()

#lista_transsaciones: list[Transsacion] = []


# transsaciones
@rutas_transsaciones.get("/transsaciones", response_model=list[Transsacion])
async def lista_transsaciones():
    return lista_transsaciones

@rutas_transsaciones.get("/transsaciones/{transsacion_id}", response_model=Transsacion)
async def obtener_transsacion(transsacion_id: int):
    for i, obj_transsacion in enumerate(lista_transsaciones):
        if obj_transsacion.id == transsacion_id:
            return obj_transsacion

@rutas_transsaciones.post("/transsaciones/{factura_id}", response_model=Transsacion)
async def crear_transsacion(factura_id: int, datos_transsacion: TranssacionCrear):
    factura_encontrada = None
    for factura in lista_facturas:
        if factura.id == factura_id:
            factura_encontrada = factura

    if not factura_encontrada:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Factura con id {factura_id} no existe")
    

    transsacion_val = Transsacion.model_validate(datos_transsacion.model_dump())
    transsacion_val.factura_id = factura_id
    factura_encontrada.transsaciones.append(transsacion_val)
    transsacion_val.factura = factura_encontrada
    transsacion_val.id = len(lista_transsaciones)+1
    lista_transsaciones.append(transsacion_val)
    return transsacion_val


@rutas_transsaciones.patch("/transsaciones/{transsacion_id}", response_model=Transsacion)
async def editar_transsacion(transsacion_id: int, datos_transsacion: TranssacionEditar):
    for i, obj_transsacion in enumerate(lista_transsaciones):
        if obj_transsacion.id == transsacion_id:
            transsacion_val = Transsacion.model_validate(datos_transsacion.model_dump())
            transsacion_val.id = transsacion_id
            lista_transsaciones[i] = transsacion_val
            return transsacion_val
    raise HTTPException(status_code=400, detail=f"Transsacion con id {transsacion_id} no existe")

@rutas_transsaciones.delete("/transsaciones/{transsacion_id}", response_model=Transsacion)
async def eliminar_transsacion(transsacion_id: int):
    for i, obj_transsacion in enumerate(lista_transsaciones):
        if obj_transsacion.id == transsacion_id:
            transsacion_eliminada = lista_transsaciones.pop(i)
            return transsacion_eliminada
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Transsacion con id {transsacion_id} no existe")


    
