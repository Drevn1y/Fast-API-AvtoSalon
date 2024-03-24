from pydantic import BaseModel


# Схема данных для добавления новой машины
class BikeValidator(BaseModel):
    bike_price: float
    bike_name: str
    bike_company: str
    bike_mileage: int
    bike_color: str
    bike_year: int

