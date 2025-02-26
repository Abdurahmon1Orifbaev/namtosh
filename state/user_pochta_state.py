from aiogram.dispatcher.filters.state import StatesGroup, State


class PochtaRegister(StatesGroup):
    line = State()
    phone_number = State()
    information = State()
