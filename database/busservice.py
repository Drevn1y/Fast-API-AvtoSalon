from database.models import Bus, User
from database import get_db
from datetime import datetime


# Получить все автобусы
def get_all_bus_db():
    db = next(get_db())
    all_bus = db.query(Bus).all()
    return all_bus


# Получить определенную автобус
def get_exact_bus_db(bus_id):
    db = next(get_db())

    exact_post = db.query(Bus).filter_by(bus_id=bus_id).first()

    if exact_post:
        return exact_post
    else:
        return 'Такой автобус не найден'


# Добавить новый автобус
def add_new_bus_db(bus_price, bus_name, bus_company, bus_mileage, bus_color, bus_year):
    db = next(get_db())

    new_bus = Bus(bus_price=bus_price, bus_name=bus_name, bus_company=bus_company, bus_mileage=bus_mileage, bus_color=bus_color, bus_year=bus_year)
    db.add(new_bus)
    db.commit()
    return f'Успешно добавлен {new_bus.bus_id}'


# Удалить автобус
def delete_bus_db(bus_id):
    db = next(get_db())

    delete_bus = db.query(Bus).filter_by(bus_id=bus_id).first()
    if delete_bus:
        db.delete(delete_bus)
        db.commit()
        return 'Автобус успешно удален!'
    else:
        return 'Автобус не найден!'


# Редактирование автобуса
def edit_bus_db(bus_id, new_data):
    db = next(get_db())

    edit_bus = db.query(Bus).filter_by(bus_id=bus_id).first()

    if edit_bus:
        for field, value in new_data.dict().items():
            if value is not None and hasattr(edit_bus, field):
                setattr(edit_bus, field, value)

        db.commit()
        return f'Автобус с ID {bus_id} успешно отредактирована'
    else:
        return 'Автобус с таким ID не найден'


# Добавить автобус к пользователю
def add_bus_to_user_db(user_id, bus_id):
    db = next(get_db())

    user = db.query(User).filter_by(user_id=user_id).first()
    bus = db.query(Bus).filter_by(bus_id=bus_id).first()

    if user and bus:
        user.buses.append(bus)
        db.commit()
        return f'Автобус успешно добавлен к пользователю {user_id}'
    else:
        return 'Пользователь или автобус не найден'
