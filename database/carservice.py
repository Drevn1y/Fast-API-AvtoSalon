from database.models import Car, User
from database import get_db


# Получить все Машины
def get_all_cars_db():
    db = next(get_db())
    all_cars = db.query(Car).all()
    return all_cars


# Получить определенную машину
def get_exact_car_db(car_id):
    db = next(get_db())

    exact_post = db.query(Car).filter_by(car_id=car_id).first()

    if exact_post:
        return exact_post
    else:
        return 'Такая машина не найдена'


# Добавить новую машину
def add_new_car_db(car_price, car_name, car_company, car_mileage, car_color, car_year):
    db = next(get_db())

    new_car = Car(car_price=car_price, car_name=car_name, car_company=car_company, car_mileage=car_mileage, car_color=car_color, car_year=car_year)
    db.add(new_car)
    db.commit()
    return f'Успешно добавлен {new_car.car_id}'


# Удалить машину
def delete_car_db(car_id):
    db = next(get_db())

    delete_car = db.query(Car).filter_by(car_id=car_id).first()
    if delete_car:
        db.delete(delete_car)
        db.commit()
        return 'Машина успешно удалена!'
    else:
        return 'Машина не найдена!'


# Редактирование машины
def edit_car_db(car_id, new_data):
    db = next(get_db())

    edit_car = db.query(Car).filter_by(car_id=car_id).first()

    if edit_car:
        for field, value in new_data.dict().items():
            if value is not None and hasattr(edit_car, field):
                setattr(edit_car, field, value)

        db.commit()
        return f'Машина с ID {car_id} успешно отредактирована'
    else:
        return 'Машина с таким ID не найдена'


# Добавить машину к пользователю
def add_car_to_user_db(user_id, car_id):
    db = next(get_db())

    user = db.query(User).filter_by(user_id=user_id).first()
    car = db.query(Car).filter_by(car_id=car_id).first()

    if user and car:
        user.cars.append(car)
        db.commit()
        return f'Машина успешно добавлена к пользователю {user_id}'
    else:
        return 'Пользователь или машина не найдена'
