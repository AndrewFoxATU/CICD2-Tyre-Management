from fastapi import FastAPI

app = FastAPI(title="Orders Service API")

orders = []

@app.get("/api/orders")
def get_orders():
    return orders

@app.post("/api/orders")
def create_order(order: dict):
    orders.append(order)
    return {"message": "Order created", "order": order}

@app.get("/health")
def health_check():
    return {"status": "ok"}
