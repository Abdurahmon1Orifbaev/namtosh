from aiogram.dispatcher.filters.state import StatesGroup, State


class Register(StatesGroup):
    line = State()
    members = State()
    time = State()
    phone_number = State()
