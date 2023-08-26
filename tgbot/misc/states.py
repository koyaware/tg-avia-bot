from aiogram.dispatcher.filters.state import StatesGroup, State


class MailingState(StatesGroup):
    send_all = State()
    send_sub = State()
    send_not_sub = State()