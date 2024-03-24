from pydantic import BaseModel


# Схема данных для добавления новой машины
class CarValidator(BaseModel):
    car_price: float
    car_name: str
    car_company: str
    car_mileage: int
    car_color: str
    car_year: int

