import json

from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.config import SOURCE_DIR
from tgbot.filters.admin import UserFilter
from tgbot.misc.commands import Commands


async def avia_timetable(message: Message):
    with open(SOURCE_DIR / 'avia.json', encoding='utf-8') as file:
        avia_dict = json.load(file)

    added_times = {}
    avia_list = []
    for k, v in sorted(avia_dict.items(), key=lambda item: item[1]["card_time"]):
        avia_title = v["card_title"]
        avia_time = v["card_time"]

        if "Нет данных" not in avia_title and "Нет данных" not in avia_time:
            if avia_time in added_times:
                if avia_title != added_times[avia_time]:
                    avia = f'\n📍 {avia_title}\n' \
                           f'🕜 {avia_time}\n'
                    avia_list.append(avia)
                    added_times[avia_time] = avia_title
            else:
                avia = f'\n📍 {avia_title}\n' \
                       f'🕜 {avia_time}\n'
                avia_list.append(avia)
                added_times[avia_time] = avia_title

    avia_arrival_str = '\n'.join(avia_list)
    await message.bot.send_message(message.from_user.id, f'📊 Расписание на сегодня \n<code>Аэропорт</code>'
                                                         f'\n{avia_arrival_str}'
                                                         f'\n\nℹ️ <b>Проект бота:</b> @vtaxiizh')


def register_avia(dp: Dispatcher):
    dp.register_message_handler(
        avia_timetable, UserFilter(),
        text=Commands.avia_timetable.value,
        state="*"
    )