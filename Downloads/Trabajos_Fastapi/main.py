from fastapi import FastAPI, HTTPException, status
from modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from modelos.facturas import Factura, FacturaCrear, FacturaEditar
from modelos.transsacion import Transsacion, TranssacionCrear, TranssacionEditar

app = FastAPI()

lista_clientes: list[Cliente] = []
lista_facturas: list[Factura] = []
lista_transsaciones: list[Transsacion] = []

# clientes

@app.get("/clientes", response_model=list[Cliente])
async def lista_clientes():
    return lista_clientes

@app.get("/clientes/{cliente_id}", response_model=Cliente)
async def lista_cliente(cliente_id: int):
    for obj_cliente in lista_clientes:
        if obj_cliente.id == cliente_id:
            return obj_cliente
    raise HTTPException(status_code=400, detail=f"Cliente con id {cliente_id} no existe")

@app.post("/clientes", response_model=Cliente)
async def crear_cliente(datos_cliente: ClienteCrear):
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    id_cliente = len(lista_clientes)+1
    cliente_val.id = id_cliente
    lista_clientes.append(cliente_val)
    return cliente_val

@app.patch("/clientes/{cliente_id}", response_model=Cliente)
async def editar_cliente(cliente_id: int, datos_cliente: ClienteEditar):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            cliente_val = Cliente.model_validate(datos_cliente.model_dump())
            cliente_val.id = cliente_id
            lista_clientes[i] = cliente_val
            return cliente_val
    raise HTTPException(status_code=400, detail=f"Cliente con id {cliente_id} no existe")

@app.delete("/clientes/{cliente_id}", response_model=Cliente)
async def eliminar_cliente(cliente_id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            cliente_eliminado = lista_clientes.pop(i)
            return cliente_eliminado
    raise HTTPException(status_code=400, detail=f"Cliente con id {cliente_id} no existe")

# facturas

@app.get("/facturas", response_model=list[Factura])
async def lista_facturas():
    return lista_facturas

@app.get("/facturas/{factura_id}", response_model=Factura)
async def obtener_factura(factura_id: int):
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == factura_id:
            return obj_factura
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Factura con id {factura_id} no existe")

@app.post("/facturas", response_model=Factura)
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

@app.patch("/facturas/{factura_id}", response_model=Factura)
async def editar_factura(factura_id: int, datos_factura: FacturaEditar):
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == factura_id:
            factura_val = Factura.model_validate(datos_factura.model_dump())
            factura_val.id = factura_id
            lista_facturas[i] = factura_val
            return factura_val
    raise HTTPException(status_code=400, detail=f"Factura con id {factura_id} no existe")

@app.delete("/facturas/{factura_id}", response_model=Factura)
async def eliminar_factura(factura_id: int):
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == factura_id:
            factura_eliminada = lista_facturas.pop(i)
            return factura_eliminada
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Factura con id {factura_id} no existe")




# transsaciones
@app.get("/transsaciones", response_model=list[Transsacion])
async def lista_transsaciones():
    return lista_transsaciones

@app.get("/transsaciones/{transsacion_id}", response_model=Transsacion)
async def obtener_transsacion(transsacion_id: int):
    for i, obj_transsacion in enumerate(lista_transsaciones):
        if obj_transsacion.id == transsacion_id:
            return obj_transsacion

@app.post("/transsaciones/{factura_id}", response_model=Transsacion)
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
    return transsacion_val


@app.patch("/transsaciones/{transsacion_id}", response_model=Transsacion)
async def editar_transsacion(transsacion_id: int, datos_transsacion: TranssacionEditar):
    for i, obj_transsacion in enumerate(lista_transsaciones):
        if obj_transsacion.id == transsacion_id:
            transsacion_val = Transsacion.model_validate(datos_transsacion.model_dump())
            transsacion_val.id = transsacion_id
            lista_transsaciones[i] = transsacion_val
            return transsacion_val
    raise HTTPException(status_code=400, detail=f"Transsacion con id {transsacion_id} no existe")

@app.delete("/transsaciones/{transsacion_id}", response_model=Transsacion)
async def eliminar_transsacion(transsacion_id: int):
    for i, obj_transsacion in enumerate(lista_transsaciones):
        if obj_transsacion.id == transsacion_id:
            transsacion_eliminada = lista_transsaciones.pop(i)
            return transsacion_eliminada
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Transsacion con id {transsacion_id} no existe")


    
