from database.models import Motorbike, User
from database import get_db


# Получить все Мотоциклы
def get_all_motorbike_db():
    db = next(get_db())
    all_motorbike = db.query(Motorbike).all()
    return all_motorbike


# Получить определенную мотоцикл
def get_exact_motorbike_db(bike_id):
    db = next(get_db())

    exact_post = db.query(Motorbike).filter_by(bike_id=bike_id).first()

    if exact_post:
        return exact_post
    else:
        return 'Такой мотоцикл не найден'


# Добавить новый мотоцикл
def add_new_motorbike_db(bike_price, bike_name, bike_company, bike_mileage, bike_color, bike_year):
    db = next(get_db())

    new_motorbike = Motorbike(bike_price=bike_price, bike_name=bike_name, bike_company=bike_company, bike_mileage=bike_mileage, bike_color=bike_color, bike_year=bike_year)
    db.add(new_motorbike)
    db.commit()
    return f'Успешно добавлен {new_motorbike.bike_id}'


# Удалить мотоцикл
def delete_motorbike_db(bike_id):
    db = next(get_db())

    delete_motorbike = db.query(Motorbike).filter_by(bike_id=bike_id).first()
    if delete_motorbike:
        db.delete(delete_motorbike)
        db.commit()
        return 'Мотоцикл успешно удален!'
    else:
        return 'Мотоцикл не найден!'


# Редактирование мотоцикла
def edit_motorbike_db(bike_id, new_data):
    db = next(get_db())

    edit_motorbike = db.query(Motorbike).filter_by(bike_id=bike_id).first()

    if edit_motorbike:
        for field, value in new_data.dict().items():
            if value is not None and hasattr(edit_motorbike, field):
                setattr(edit_motorbike, field, value)

        db.commit()
        return f'Мотоцикл с ID {bike_id} успешно отредактирована'
    else:
        return 'Машина с таким ID не найдена'


# Добавить мотоцикл к пользователю
def add_motorbike_to_user_db(user_id, bike_id):
    db = next(get_db())

    user = db.query(User).filter_by(user_id=user_id).first()
    bike = db.query(Motorbike).filter_by(bike_id=bike_id).first()

    if user and bike:
        user.motorbikes.append(bike)
        db.commit()
        return f'Мотоцикл успешно добавлен к пользователю {bike_id}'
    else:
        return 'Мотоцикл или юзер не найден'

