from datetime import datetime

from aiogram import Dispatcher
from aiogram.types import Message

from source.main import collect_all_data
from tgbot.config import db, ADMIN_IDS
from tgbot.filters import AdminFilter
from tgbot.misc.commands import Commands
from tgbot.misc.keyboards.inline import mailing_inline
from tgbot.misc.keyboards.reply import adminMainMenu, adminMenu


async def admin_start(message: Message):
    if (not db.user_exists(message.from_user.id)):
        db.add_user(message.from_user.id, message.from_user.username, message.from_user.full_name, datetime.now())
        for admin in ADMIN_IDS:
            await message.bot.send_message(admin, f"🆕 Новый пользователь:"
                                                  f"\n\nПользователь: @{message.from_user.username}, <b>{message.from_user.first_name}</b>\n"
                                                  f"[ID:{message.from_user.id}] только что зарегестрировался в боте.")
        await message.bot.send_message(message.from_user.id,
                                       f"Приветсвуем тебя {message.from_user.first_name}, на проекте АЭРО ЖД ИЖЕВСК.\n"
                                       f"Бот умееет мониторить расписание  Аэропорт и РЖД Ижевск",
                                       reply_markup=adminMainMenu)
    else:
        await message.bot.send_message(message.from_user.id,
                                       f"Приветсвуем тебя {message.from_user.first_name}, на проекте АЭРО ЖД ИЖЕВСК.\n"
                                       f"Бот умееет мониторить расписание  Аэропорт и РЖД Ижевск",
                                       reply_markup=adminMainMenu)


async def admin_menu(message: Message):
    await message.bot.send_message(message.from_user.id,
                                   'Добро пожаловать в админ панель!\n\nДля перехода в главное меню, отправьте боту команду - /start.',
                                   reply_markup=adminMenu)


async def mailing_menu(message: Message):
    await message.bot.send_message(message.from_user.id, 'Выберите группу пользователей для рассылки: ',
                                   reply_markup=mailing_inline)


async def update_parser(message: Message):
    await message.bot.send_message(message.from_user.id, '⏳ Пожалуйста ожидайте...')
    collect_all_data()
    await message.bot.send_message(message.from_user.id, '✅ Расписания успешно обновилось!')


def register_admin(dp: Dispatcher):
    dp.register_message_handler(
        admin_start, AdminFilter(),
        text=['/start', '!start', 'start', Commands.come_back.value],
        state="*"
    )
    dp.register_message_handler(
        admin_menu, AdminFilter(),
        text=Commands.admin_menu.value,
        state='*'
    )
    dp.register_message_handler(
        update_parser, AdminFilter(),
        text=Commands.update_parser.value,
        state='*'
    )
    dp.register_message_handler(
        mailing_menu, AdminFilter(),
        text=Commands.mailing.value,
        state='*'
    )