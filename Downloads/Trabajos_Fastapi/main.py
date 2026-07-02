from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

lista_clientes: list[Cliente] = []

class Cliente(BaseModel):
    id: int
    nombre: str
    email: str
    descripcion: str


@app.get("/clientes")
def lista_clientes():
    return lista_clientes

@app.get("/clientes/{cliente_id}")
def lista_cliente(cliente_id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.get("id") == cliente_id:
            return obj_cliente

@app.post("/clientes")
def crear_cliente(datos_cliente: Cliente):
    lista_clientes.append(datos_cliente)
    return datos_cliente
    