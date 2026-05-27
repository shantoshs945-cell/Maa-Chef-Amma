from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import products, orders, admin

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products.router, prefix="/api/products")
app.include_router(orders.router, prefix="/api/orders")
app.include_router(admin.router, prefix="/api/admin")

@app.get("/")
def root():
    return {"status": "Maa Chef Amma API is running!"}