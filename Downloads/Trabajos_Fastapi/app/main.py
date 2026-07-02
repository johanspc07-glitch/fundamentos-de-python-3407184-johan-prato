from fastapi import FastAPI, HTTPException, status
from app.modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from app.modelos.facturas import Factura, FacturaCrear, FacturaEditar
from app.modelos.transsacion import Transsacion, TranssacionCrear, TranssacionEditar
from enrutadores import clientes

app = FastAPI()

lista_clientes: list[Cliente] = []
lista_facturas: list[Factura] = []
lista_transsaciones: list[Transsacion] = []

app.include_router(clientes.rutas_clientes, tags=["Clientes"])
app.include_router(clientes.rutas_facturas, tags=["Facturas"])


