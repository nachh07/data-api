from fastapi import APIRouter
from config.db import conn
from typing import List, AnyStr, Dict
from models.transaction import transactions_table
from schemas.transaction import Transaction
from datetime import datetime

transaction = APIRouter()

@transaction.post(
    "/transactions",
    tags=["transactions"],
    response_model=AnyStr,
    description="Inserts a batch of transactions"
)
def insert_transactions(transactions_list: List[Transaction]) -> str:

    for i in range(len(transactions_list)): 
        transaction_table = transactions_list[i]
        new_transactions = {
                'amount' : transaction_table.amount,
                'id_customer' : transaction_table.id_customer, 
                'date' : transaction_table.date
            }
        if not new_transactions['date']:  
            new_transactions['date'] = str(datetime.now().strftime("%m/%d/%Y"))
        conn.execute(transactions_table.insert().values(new_transactions))
        count = i + 1
         
    return f'{count} transactions are inserted in DB at {datetime.now().strftime("%m/%d/%Y")}'

@transaction.get(
    "/transactions",
    tags=["transactions"],
    response_model=List[Transaction],
    description="List of transaction objects"
)
def get_transactions():
    return conn.execute(transactions_table.select()).fetchall()

@transaction.get(
    '/transactions/{id}', 
    tags=["transactions"],
    response_model=Dict,
    description="ID of specific transaction"
)
def get_transactions(id: str) -> dict:
    
    """
    args: ID of specific transaction
    returns: requested transaction
    """
    
    return dict(conn.execute(transactions_table.select().where(transactions_table.c.id_transaction==id)).first())
