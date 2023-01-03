from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime


class Transaction(BaseModel):
    id_transaction: Optional[str]
    amount: float
    id_customer: int
    date: str
    
    class Config:
        orm_mode = True

