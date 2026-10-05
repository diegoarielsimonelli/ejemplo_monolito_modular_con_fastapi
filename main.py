from fastapi import FastAPI
from .products.router import router as products_router
from ejemplo_monolito_modular.orders.router import router as orders_router

app = FastAPI(title="Monolito Modular de E-Commerce")

# Registramos los módulos de forma independiente
app.include_router(products_router)
app.include_router(orders_router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido al Monolito Modular"}
