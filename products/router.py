from fastapi import APIRouter, HTTPException
from ejemplo_monolito_modular.products import services as product_service

# Instanciamos el enrutador para el módulo de productos
router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/")
def list_products():
    """
    Endpoint para obtener todos los productos disponibles.
    """
    # Devolvemos el diccionario simulación de base de datos
    return product_service.PRODUCTS_DB

@router.get("/{product_id}")
def get_product_by_id(product_id: int):
    """
    Endpoint para buscar un producto por su ID.
    """
    product = product_service.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="El producto no fue encontrado")
    return product
