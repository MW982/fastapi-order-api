from decimal import Decimal

from sqlmodel import Field, SQLModel


class Item(SQLModel, table=True):
    id: int = Field(primary_key=True)

    price: Decimal = Field(decimal_places=2, default=Decimal(0))
