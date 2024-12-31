from __future__ import annotations

from customerapp.models import User
from orderapp.models import Order


class OrderService:
    def __init__(self, user: User):
        self.user: User = user

    def validate(self) -> None:
        pass

    def create(self) -> Order:
        pass

    def process(self):
        self.validate()

        order = self.create()

        order.update_status()
        # order.send_notifications()
