from pydantic import BaseModel


# Схема данных для добавления нового автобуса
class BusValidator(BaseModel):
    bus_price: float
    bus_name: str
    bus_company: str
    bus_mileage: int
    bus_color: str
    bus_year: int