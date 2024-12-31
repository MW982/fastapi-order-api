from enum import StrEnum


class OrderStatusEnum(StrEnum):
    CREATED = "Created"
    PROCESSING = "Processing"
    CANCELLED = "Cancelled"
    ACCEPTED = "Accepted"
