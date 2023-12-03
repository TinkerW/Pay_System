from fastapi import APIRouter

from database.userservice import register_user_db, delete_user_db, edit_user_db, get_exact_user_db, check_user_email_db

from user import UserRegisterValidator, EditUserValidator

user_router = APIRouter(prefix='/user', tags=['Работа с пользователями'])


# Регистрация
@user_router.post('/register')
async def register_user(data: UserRegisterValidator):
    # Переводим pydantic в обычный словарь
    new_user_data = data.model_dump()
    # {'name':'asd'}

    # вызов функции для проверки почты в базе
    checker = check_user_email_db(data.email)
    if not checker:
        result = register_user_db(**new_user_data)
        return {'message': result}

    return {'message': 'Пользователь с такой почтой уже есть в БД'}


# Получения инфо о пользователя
@user_router.get('/info')
async def get_user(user_id: int):
    result = get_exact_user_db(user_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Такого пользователя нету'}


# Изменить данные о пользователе
@user_router.put('/edit-data')
async def edit_user(data: EditUserValidator):
    change_data = data.model_dump()

    result = edit_user_db(**change_data)

    if result:
        return {'message': result}
    else:
        return {'message': 'Нету пользователя что бы изменить'}


# Удаления пользователя
@user_router.delete('/delete-user')
async def delete_user(user_id: int):
    result = delete_user_db(user_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Нету пользователя что бы удалить бля'}
