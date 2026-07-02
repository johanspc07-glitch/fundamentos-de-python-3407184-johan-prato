from fastapi import FastAPI, HTTPException
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
def lista_facturas():
    return lista_facturas

@app.get("/facturas/{factura_id}", response_model=Factura)
def obtener_factura(factura_id: int):
    for obj_factura in lista_facturas:
        if obj_factura.id == factura_id:
            return obj_factura

@app.post("/facturas", response_model=Factura)
def crear_factura(datos_factura: FacturaCrear):
    factura_val = Factura.model_validate(datos_factura.model_dump())
    lista_facturas.append(factura_val)
    return factura_val

@app.patch("/facturas/{factura_id}", response_model=Factura)
def editar_factura(factura_id: int, datos_factura: FacturaEditar):
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == factura_id:
            factura_val = Factura.model_validate(datos_factura.model_dump())
            factura_val.id = factura_id
            lista_facturas[i] = factura_val
            return factura_val
    raise HTTPException(status_code=400, detail=f"Factura con id {factura_id} no existe")

# transsaciones
@app.get("/transsaciones", response_model=list[Transsacion])
def lista_transsaciones():
    return lista_transsaciones

@app.get("/transsaciones/{transsacion_id}", response_model=Transsacion)
def obtener_transsacion(transsacion_id: int):
    for obj_transsacion in lista_transsaciones:
        if obj_transsacion.id == transsacion_id:
            return obj_transsacion

@app.post("/transsaciones", response_model=Transsacion)
def crear_transsacion(datos_transsacion: TranssacionCrear):
    transsacion_val = Transsacion.model_validate(datos_transsacion.model_dump())
    lista_transsaciones.append(transsacion_val)
    return transsacion_val

@app.patch("/transsaciones/{transsacion_id}", response_model=Transsacion)
def editar_transsacion(transsacion_id: int, datos_transsacion: TranssacionEditar):
    for i, obj_transsacion in enumerate(lista_transsaciones):
        if obj_transsacion.id == transsacion_id:
            transsacion_val = Transsacion.model_validate(datos_transsacion.model_dump())
            transsacion_val.id = transsacion_id
            lista_transsaciones[i] = transsacion_val
            return transsacion_val
    raise HTTPException(status_code=400, detail=f"Transsacion con id {transsacion_id} no existe")