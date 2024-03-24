from fastapi import APIRouter
from database.motorbikeservice import *
from motorbikes import BikeValidator

# создаем компонент
bike_router = APIRouter(prefix='/motorbikes', tags=['Управление с Мотоциклами'])


# Получить все мотоциклы
@bike_router.get('/all-bikes')
async def get_all_bikes():
    return get_all_motorbike_db()


# Получить определенный мотоцикл
@bike_router.get('/get-bike')
async def get_exact_bike(bike_id):
    result = get_exact_motorbike_db(bike_id=bike_id)

    return result


# Добавить новый мотоцикл
@bike_router.post('/add-new-bike')
async def add_new_bike(bike_price: float, bike_name: str, bike_company: str, bike_mileage: int, bike_color: str, bike_year: int):
    new_bike = add_new_motorbike_db(bike_price=bike_price, bike_name=bike_name, bike_company=bike_company, bike_mileage=bike_mileage, bike_color=bike_color, bike_year=bike_year)

    return {'message': f'Успешно добавлен {new_bike}'}


# Удалить мотоцикл
@bike_router.delete('/delete-bike')
async def delete_bike(bike_id):
    result = delete_motorbike_db(bike_id=bike_id)

    if result:
        return 'Мотоцикл удален успешно!'
    else:
        return 'Мотоцикл с такой айди не найден!'


# Редактирование мотоцикла
@bike_router.put('/edit-bike')
async def edit_motorbike(bike_id, data: BikeValidator):
    result = edit_motorbike_db(bike_id, data)

    return {'message': result}


# Добавление мотоцикла к юзеру
@bike_router.post('/add-bike')
async def add_motorbike_to_user(user_id, bike_id):
    result = add_motorbike_to_user_db(user_id=user_id, bike_id=bike_id)

    return result
