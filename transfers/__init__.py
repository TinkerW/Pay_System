from pydantic import BaseModel


# Класс для создания перевода
class CreateTransferValidator(BaseModel):
    card_from: int
    card_to: int
    amount: float


# Класс для валидации отмены
class CancelTransferValidator(BaseModel):
    card_from: int
    card_to: int
    amount: float
    transfer_id: int
