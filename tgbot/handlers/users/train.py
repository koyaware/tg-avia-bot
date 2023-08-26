import json

from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.config import SOURCE_DIR
from tgbot.filters.admin import UserFilter
from tgbot.misc.commands import Commands


async def train_arrival(message: Message):
    with open(SOURCE_DIR / 'train_arrival.json', encoding='utf-8') as file:
        train_dict = json.load(file)

    added_times = {}
    train_arrival_list = []
    for k, v in sorted(train_dict.items(), key=lambda item: item[1]["card_time"]):
        train_title = v["card_title"]
        train_time = v["card_time"]

        if "Нет данных" not in train_title and "Нет данных" not in train_time:
            if train_time in added_times:
                if train_title != added_times[train_time]:
                    avia = f'\n📍 {train_title}\n' \
                           f'🕜 {train_time}\n'
                    train_arrival_list.append(avia)
                    added_times[train_time] = train_title
            else:
                avia = f'\n📍 {train_title}\n' \
                       f'🕜 {train_time}\n'
                train_arrival_list.append(avia)
                added_times[train_time] = train_title

    train_arrival_str = '\n'.join(train_arrival_list)
    await message.bot.send_message(message.from_user.id, f'📊 Расписание на сегодня \n<code>Прибытие ЖД</code>'
                                                         f'\n{train_arrival_str}'
                                                         f'\n\nℹ️ <b>Проект бота:</b> @vtaxiizh')


def register_train(dp: Dispatcher):
    dp.register_message_handler(
        train_arrival, UserFilter(),
        text=Commands.train_arrival.value,
        state="*"
    )