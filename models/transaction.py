from datetime import datetime
from sqlalchemy import Table, Column
from sqlalchemy.types import Integer, String, Float, DateTime
from sqlalchemy.sql import func
from config.db import meta, engine

transactions_table = Table('transactions', meta,
                Column('id_transaction', Integer, primary_key=True), 
                Column('id_customer', Integer),
                Column('amount', Float),
                Column('date',String(255))
            )

meta.create_all(engine)