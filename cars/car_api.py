from fastapi import APIRouter
from database.carservice import *
from cars import CarValidator


# Создаем компонент
car_router = APIRouter(prefix='/cars', tags=['Управление с Машинами'])


# Получить все Машины
@car_router.get('/all-cars')
async def get_all_cars():
    return get_all_cars_db()


# Получить определенную машину
@car_router.get('/get-car')
async def get_exact_car(car_id):
    result = get_exact_car_db(car_id=car_id)

    return result


# Добавить новую машину
@car_router.post('/add-new-car')
async def add_new_car(car_price: float, car_name: str, car_company: str, car_mileage: int, car_color: str, car_year: int):
    new_car = add_new_car_db(car_price=car_price, car_name=car_name, car_company=car_company, car_mileage=car_mileage, car_color=car_color, car_year=car_year)
    return {'message': f'Успешно добавлен {new_car}'}


# Удалить машину
@car_router.delete('/delete-car')
async def delete_car(car_id):
    result = delete_car_db(car_id=car_id)

    if result:
        return 'Машина удалена успешно!'
    else:
        return 'Машина с такой айди не найдена!'


# Редактирование машины
@car_router.put('/edit-car/{car_id}')
async def edit_car(car_id: int, data: CarValidator):
    result = edit_car_db(car_id, data)

    return {'message': result}


# Добавить тачку к юзеру
@car_router.post('/add-car')
def add_car_to_user(user_id, car_id):

    result = add_car_to_user_db(user_id=user_id, car_id=car_id)

    return result