from ejemplo_monolito_modular.products import services as product_service

ORDERS_DB = []

def create_order(product_id: int, quantity: int):
    # 1. Comunicación inter-módulo (en memoria, llamadas a funciones de Python)
    product = product_service.get_product(product_id)
    if not product:
        return {"error": "El producto no existe"}
    
    # 2. Verificar y descontar stock usando la interfaz del otro módulo
    success = product_service.decrease_stock(product_id, quantity)
    if not success:
        return {"error": "No hay stock suficiente"}
    
    # 3. Crear la orden si todo está bien
    new_order = {
        "order_id": len(ORDERS_DB) + 1,
        "product_id": product_id,
        "quantity": quantity,
        "total": product["price"] * quantity
    }
    ORDERS_DB.append(new_order)
    return new_order
