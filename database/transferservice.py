from datetime import datetime

from database.models import Transfer, UserCard
from database import get_db


# Проверка карты
def validate_card(card_number, db):
    exact_card = db.query(UserCard).filter_by(card_number=card_number).first()

    return exact_card


# Создания перевода
def create_transaction_db(card_from, card_to, amount):
    db = next(get_db())

    # Проверка на наличии карты в бд обеих карт
    check_card_from = validate_card(card_from, db)
    check_card_to = validate_card(card_to, db)

    # Если обе карты существуют в бд перевод
    if check_card_from and check_card_to:
        # Проверить баланс у отправителя
        if check_card_from.balance >= amount:
            # минусуем у того кто отправил
            check_card_from.balance -= amount
            # Добавляем тому кто получает
            check_card_to.balance += amount

            # Сохраняем платеж в бд
            new_transaction = Transfer(card_from_id=check_card_from.card_id,
                                       card_to_id=check_card_to.card_id,
                                       amount=amount,
                                       transaction_date=datetime.now()
                                       )
            db.add(new_transaction)
            db.commit()

            return {'status': 1, 'message': f'Transaction saccess id_transaction - {new_transaction.transfer_id}'}
        else:
            return "Недостаточно средств на балансе"
    else:
        return "Одна из карт не существует"


# Получить все переводы по карте(card_id)
def get_card_transaction_db(card_from_id):
    db = next(get_db())

    card_transaction = db.query(Transfer).filter_by(card_from_id=card_from_id).all()
    return card_transaction


# Отменить перевод
def cancel_transfer_db(card_from, card_to, amount, transfer_id):
    db = next(get_db())
    # Проверка на наличии карты в бд обеих карт
    check_card_from = validate_card(card_from, db)
    check_card_to = validate_card(card_to, db)
    # Если обе карты существуют в бд перевод
    if check_card_from and check_card_to:
        # Проверить баланс того кто возвращает деньги
        if check_card_to.balance >= amount:
            # Отнимаем тому кто получил до этого
            check_card_to.balance -= amount
            # Добавляем у того кто отправил до этого
            check_card_from.balance += amount

            # Сохраняем в базе
            exact_transaction = db.query(Transfer).filter_by(transfer_id=transfer_id).first()
            exact_transaction.status = False

            db.commit()

            return "Перервод успешно отменен"
        else:
            return "Недостаточно средств на балансе"

    return "Одна из карт не существует"
