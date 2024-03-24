from fastapi import FastAPI

from users.user_api import user_router
from cars.car_api import car_router
from motorbikes.motorbike_api import bike_router
from buses.bus_api import bus_router
from database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

app.include_router(user_router)
app.include_router(car_router)
app.include_router(bike_router)
app.include_router(bus_router)

