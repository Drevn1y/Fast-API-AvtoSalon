from fastapi import APIRouter
from database.busservice import *
from buses import BusValidator


# Создаем компонент
bus_router = APIRouter(prefix='/buses', tags=['Управление с Автобусами'])


# Получить все автобусы
@bus_router.get('/all-buses')
async def get_all_buses():
    return get_all_bus_db()


# Получить определенный автобус
@bus_router.get('/get-bus')
async def get_exact_bus(bus_id):
    result = get_exact_bus_db(bus_id=bus_id)

    return result


# Добавить новый автобус
@bus_router.post('/add-new-bus')
async def add_new_bus(bus_price: float, bus_name: str, bus_company: str, bus_mileage: int, bus_color: str, bus_year: int):
    new_bus = add_new_bus_db(bus_price=bus_price, bus_name=bus_name, bus_company=bus_company, bus_mileage=bus_mileage, bus_color=bus_color, bus_year=bus_year)
    return new_bus


# Удалить автобус
@bus_router.delete('/delete-bus')
async def delete_bus(bus_id):
    result = delete_bus_db(bus_id=bus_id)

    if result:
        return 'Автобус удален успешно!'
    else:
        return 'Автобус с такой айди не найден!'


# Редактирование автобус
@bus_router.put('/edit-bus/{bus_id}')
async def edit_bus(bus_id: int, data: BusValidator):
    result = edit_bus_db(bus_id, data)

    return {'message': result}


# Добавить автобус к юзеру
@bus_router.post('/add-bus')
def add_bus_to_user(user_id, bus_id):

    result = add_bus_to_user_db(user_id=user_id, bus_id=bus_id)

    return result