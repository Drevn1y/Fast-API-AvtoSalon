from sqlalchemy import Column, String, Integer, DateTime, Date, Float, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


# Таблица пользователя
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    balance = Column(Float, default=0)
    username = Column(String)
    surname = Column(String)
    phone_number = Column(Integer, unique=True)
    password = Column(String)
    city = Column(String)
    birthday = Column(Date)
    profile_photo = Column(String)
    reg_date = Column(DateTime)

    # Связь с таблицей автомобилей
    cars = relationship("Car", back_populates="user")
    # Связь с таблицей мотоциклов
    motorbikes = relationship("Motorbike", back_populates="user")
    # Связь с таблицей автобусов
    buses = relationship("Bus", back_populates="user")


# Таблица Машин
class Car(Base):
    __tablename__ = 'cars'
    car_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    car_price = Column(Float)
    car_name = Column(String)
    car_company = Column(String)
    car_mileage = Column(Integer)
    car_color = Column(String)
    car_year = Column(Integer)

    user = relationship("User", back_populates="cars")


# Таблица Мотоциклов
class Motorbike(Base):
    __tablename__ = 'motorbikes'
    bike_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    bike_price = Column(Float)
    bike_name = Column(String)
    bike_company = Column(String)
    bike_mileage = Column(Integer)
    bike_color = Column(String)
    bike_year = Column(Integer)

    user = relationship("User", back_populates="motorbikes")


# Таблица автобусов
class Bus(Base):
    __tablename__ = 'buses'
    bus_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    bus_price = Column(Float)
    bus_name = Column(String)
    bus_company = Column(String)
    bus_mileage = Column(Integer)
    bus_color = Column(String)
    bus_year = Column(Integer)

    user = relationship("User", back_populates="buses")
