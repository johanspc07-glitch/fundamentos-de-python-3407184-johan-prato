from fastapi import FastAPI, HTTPException
from modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from modelos.facturas import Factura, FacturaCrear
from modelos.transsacion import Transsacion, TranssacionCrear

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
