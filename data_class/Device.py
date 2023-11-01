from dataclasses import dataclass, field
from datetime import datetime


class DeviceClass:

    def __init__(self, model: str, manufacturer: str, price: int, release_date: datetime):
        self.model = model
        self.manufacturer = manufacturer
        self.price = price
        self.model_year = release_date


@dataclass(order=True, frozen=False)
class DeviceDataClass:
    sort_index: int = field(init=False, repr=False)
    model: str
    manufacturer: str
    price: int
    model_year: int
    inventory: bool = True

    def __post_init__(self):
        """
        Initializes after init
        """
        self.sort_index = self.price
