# python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

class Producto(BaseModel):
    nombre: str
    cantidad: float
    unidad: str

productos: List[Dict] = []

@app.post("/productos", status_code=201)
def crear_producto(producto: Producto):
    producto_dict = producto.dict()
    productos.append(producto_dict)
    return {"mensaje": "Producto registrado", "producto": producto_dict}

@app.get("/productos")
def listar_productos():
    return productos
