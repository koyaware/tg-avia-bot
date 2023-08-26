import asyncio
from datetime import datetime

from aiogram import Dispatcher
from aiogram.types import Message

from source.main import collect_all_data
from tgbot.config import db, ADMIN_IDS
from tgbot.filters.admin import UserFilter
from tgbot.misc.commands import Commands
from tgbot.misc.keyboards.reply import mainMenu, aviaMenu, trainMenu


async def user_start(message: Message):
    if (not db.user_exists(message.from_user.id)):
        db.add_user(message.from_user.id, message.from_user.username, message.from_user.full_name, datetime.now())
        for admin in ADMIN_IDS:
            await message.bot.send_message(admin, f"🆕 Новый пользователь:"
                                                  f"\n\nПользователь: @{message.from_user.username}, <b>{message.from_user.first_name}</b>\n"
                                                  f"[ID:{message.from_user.id}] только что зарегестрировался в боте.")
        await message.bot.send_message(message.from_user.id,
                                       f"Приветсвуем тебя {message.from_user.first_name}, на проекте АЭРО ЖД ИЖЕВСК.\n"
                                       f"Бот умееет мониторить расписание  Аэропорт и РЖД Ижевск",
                                       reply_markup=mainMenu)
    else:
        await message.bot.send_message(message.from_user.id,
                                       f"Приветсвуем тебя {message.from_user.first_name}, на проекте АЭРО ЖД ИЖЕВСК.\n"
                                       f"Бот умееет мониторить расписание  Аэропорт и РЖД Ижевск",
                                       reply_markup=mainMenu)


async def avia_schedule(message: Message):
    await message.bot.send_message(message.from_user.id, f'Загрузка прошла успешна ✅', reply_markup=aviaMenu)


async def train_schedule(message: Message):
    await message.bot.send_message(message.from_user.id, f'Загрузка прошла успешна ✅\n', reply_markup=trainMenu)


async def scheduled(wait_for):
    while True:
        await asyncio.sleep(wait_for)
        collect_all_data()


def register_user(dp: Dispatcher):
    dp.register_message_handler(
        user_start, UserFilter(),
        text=['/start', '!start', 'start', Commands.come_back.value],
        state="*"
    )
    dp.register_message_handler(
        avia_schedule, UserFilter(),
        text=Commands.avia_schedule.value,
        state='*'
    )
    dp.register_message_handler(
        train_schedule, UserFilter(),
        text=Commands.train_schedule.value,
        state='*'
    )
