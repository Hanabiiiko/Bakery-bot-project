from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

TEXT_GREETING = "Добро пожаловать в домашнюю кондитерскую «Светлана»!\nЧто вы бы хотели заказать?"
TEXT_COMMENT = "Пожалуйста, оставьте краткий комментарий по заказу (пожелания по начинке, декору и т.д.):"
TEXT_CONTACT_TIME = "Укажите удобную дату и время для связи с вами:"
TEXT_DEADLINE = "На какую дату нужен готовый заказ?"
TEXT_THANKS = "Спасибо за вашу заявку! С вами свяжется кондитер для уточнения деталей."

def get_baker_notification(order_id: int, username: str, category: str, contact_time: str, deadline: str, comment: str) -> str:
    return (
        f"Заявка #{order_id}\n"
        f"Заказчик: @{username}\n"
        f"Хочет заказать: {category}\n"
        f"Когда хочет связаться: {contact_time}\n"
        f"Когда нужен заказ: {deadline}\n"
        f"Комментарий по заказу: {comment}"
    )

def get_category_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    categories = ["Торт", "Выпечка", "Конфеты", "Пирожные", "Крупный заказ"]
    
    for cat in categories:
        builder.add(KeyboardButton(text=cat))
        

    builder.adjust(2) 
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
