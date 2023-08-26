from aiogram import Dispatcher

from .avia import register_avia
from .train import register_train
from .user import register_user


def register_all_user_handlers(dp: Dispatcher):
    register_user(dp)
    register_avia(dp)
    register_train(dp)
