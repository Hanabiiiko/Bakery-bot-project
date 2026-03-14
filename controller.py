from aiogram import Router, F, Bot
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

import view
import model
from config import BAKER_ID

router = Router()

class OrderFSM(StatesGroup):
    waiting_for_category = State()
    waiting_for_comment = State()
    waiting_for_contact_time = State()
    waiting_for_deadline = State()

@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(view.TEXT_GREETING, reply_markup=view.get_category_keyboard())
    await state.set_state(OrderFSM.waiting_for_category)

@router.message(OrderFSM.waiting_for_category, F.text.in_(["Торт", "Выпечка", "Конфеты", "Пирожные", "Крупный заказ"]))
async def process_category(message: Message, state: FSMContext):
    await state.update_data(category=message.text)
    await message.answer(view.TEXT_COMMENT, reply_markup=ReplyKeyboardRemove())
    await state.set_state(OrderFSM.waiting_for_comment)

@router.message(OrderFSM.waiting_for_category)
async def process_category_invalid(message: Message):
    await message.answer("Пожалуйста, выберите категорию, используя кнопки ниже.", reply_markup=view.get_category_keyboard())

@router.message(OrderFSM.waiting_for_comment)
async def process_comment(message: Message, state: FSMContext):
    await state.update_data(comment=message.text)
    await message.answer(view.TEXT_CONTACT_TIME)
    await state.set_state(OrderFSM.waiting_for_contact_time)

@router.message(OrderFSM.waiting_for_contact_time)
async def process_contact_time(message: Message, state: FSMContext):
    await state.update_data(contact_time=message.text)
    await message.answer(view.TEXT_DEADLINE)
    await state.set_state(OrderFSM.waiting_for_deadline)

@router.message(OrderFSM.waiting_for_deadline)
async def process_deadline(message: Message, state: FSMContext, bot: Bot):
    user_data = await state.get_data()
    deadline = message.text
    
    username = message.from_user.username or message.from_user.first_name

    order_id = await model.save_order(
        username=username,
        category=user_data['category'],
        comment=user_data['comment'],
        contact_time=user_data['contact_time'],
        deadline=deadline
    )

    await message.answer(view.TEXT_THANKS)

    notification_text = view.get_baker_notification(
        order_id=order_id,
        username=username,
        category=user_data['category'],
        contact_time=user_data['contact_time'],
        deadline=deadline,
        comment=user_data['comment']
    )
    
    try:
        await bot.send_message(chat_id=BAKER_ID, text=notification_text)
    except Exception as e:
        print(f"Ошибка отправки сообщения кондитеру (проверьте BAKER_ID): {e}")

    await state.clear()
