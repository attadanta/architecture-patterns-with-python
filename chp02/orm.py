from sqlalchemy import Column, Integer, String, MetaData, Table
from sqlalchemy.orm import mapper
import model

metadata = MetaData()

order_lines = Table(
    "order_lines",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("sku", String(255)),
    Column("qty", Integer, nullable=False),
    Column("orderid", String(255)),
)


def start_mappers():
    lines_mapper = mapper(model.OrderLine, order_lines)
