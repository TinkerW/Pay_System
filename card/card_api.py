# DZ v githube
# Запрос на добавления карта add_new_card
# Запрос на получении информацииоб определенной карте определенного пользователя get_card_info
# Запрос на получения всех карт пользователя get_all_user_card
# Запрос на удаления карты delete_card


from database.cardservice import add_card_db, get_exact_user_cards_db, check_card_db, delete_card_db
from fastapi import APIRouter

card_router = APIRouter(prefix='/card', tags=['Работа с картами'])


@card_router.post('/add-card')
async def add_card(user_id: int, card_number: int, balance: int, card_name: str):
    cheker = check_card_db(card_number)

    if cheker:
        return {'status': 1, 'message': 'Такая карта уже есть'}
    else:
        result = add_card_db(user_id, card_number, balance, card_name)

        if result:
            return result
        else:
            return {'status': 0, 'message': 'Error: Failed to add card'}


@card_router.get('/get-exact-user-cards')
async def get_exact_user_cards(user_id: int):
    result = get_exact_user_cards_db(user_id)

    if result:
        return result

    return {'status': 1, 'message': 'Карт нету !'}


@card_router.delete('/delete-card')
async def delete_card(card_id: int):
    return delete_card_db(card_id)

