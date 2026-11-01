from fastapi import FastAPI

app = FastAPI(
    title="inventory-service",
    description="Sample inventory API with stock quantities",
    version="1.0.0",
)

@app.get("/health")
def health():
    return {"status": "UP", "application": "inventory-service"}

@app.get("/api/inventory")
def inventory():
    return [
        {"sku": "LAP-001", "item": "Laptop", "available": 12},
        {"sku": "KEY-001", "item": "Keyboard", "available": 45},
        {"sku": "MOU-001", "item": "Mouse", "available": 80},
    ]

