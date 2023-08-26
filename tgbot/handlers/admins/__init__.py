from aiogram import Dispatcher

from tgbot.handlers.admins.admin import register_admin
from tgbot.handlers.admins.mailing import register_mailings


def register_all_admin_handlers(dp: Dispatcher):
    register_admin(dp)
    register_mailings(dp)