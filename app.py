from fastapi import FastAPI
from routes.transaction import transaction

app = FastAPI(
    title="API Data Transactions", 
    description="My first API",
    version="0.0.1", 
    openapi_tags=[{
        "name" : "transactions", 
        "description" : "transaction routes"
    }]
)

app.include_router(transaction)