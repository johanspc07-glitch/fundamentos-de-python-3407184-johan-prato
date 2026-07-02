from fastapi import FastAPI
from modelos.clientes import Cliente


app = FastAPI()

lista_clientes: list[Cliente] = []



@app.get("/clientes", response_model=list[Cliente])
def lista_clientes():
    return lista_clientes

@app.get("/clientes/{cliente_id}", response_model=Cliente)
def lista_cliente(cliente_id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.get("id") == cliente_id:
            return obj_cliente

@app.post("/clientes", response_model=Cliente)
def crear_cliente(datos_cliente: ClienteCrear):
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    lista_clientes.append(cliente_val)
    return cliente_val
    