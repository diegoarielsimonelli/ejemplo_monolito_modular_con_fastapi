# Simulación de base de datos interna del módulo
PRODUCTS_DB = {
    1: {"id": 1, "name": "Teclado Mecánico", "price": 85.0, "stock": 10},
    2: {"id": 2, "name": "Mouse Gamer", "price": 45.0, "stock": 5}
}

def get_product(product_id: int) -> dict:
    return PRODUCTS_DB.get(product_id,{})

def decrease_stock(product_id: int, quantity: int) -> bool:
    product = PRODUCTS_DB.get(product_id)
    if product and product["stock"] >= quantity:
        product["stock"] -= quantity
        return True
    return False
