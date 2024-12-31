import uuid
from datetime import datetime
from decimal import Decimal

from pydantic.types import UUID4
from sqlmodel import Field, SQLModel

from orderapp.enums import OrderStatusEnum


class SubOrder(SQLModel, table=True):
    id: int = Field(primary_key=True)

    item_id: int | None = Field(default=None, foreign_key="item.id")
    order_id: int | None = Field(default=None, foreign_key="order.id")


class Order(SQLModel, table=True):
    id: int = Field(primary_key=True)
    uuid: UUID4 = Field(default_factory=uuid.uuid4)

    price: Decimal = Field(decimal_places=2, default=Decimal(0))
    status: OrderStatusEnum = Field(default=OrderStatusEnum.CREATED)

    date_created: datetime = Field(default_factory=datetime.now)
    date_accepted: datetime | None = Field(default=None)
