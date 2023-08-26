import typing

from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from tgbot.config import ADMIN_IDS


class AdminFilter(BoundFilter):
    key = 'is_superuser'

    def __init__(self, is_superuser: typing.Optional[bool] = None):
        self.is_superuser = is_superuser

    async def check(self, obj):
        if obj.from_user.id in ADMIN_IDS:
            return True
        else:
            return False


class UserFilter(BoundFilter):
    async def check(self, message: Message):
        inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton('Подписаться 🔴', callback_data='follow', url='https://t.me/+quwO9x0iV8s5NmQy')],
            [InlineKeyboardButton('Подписался ✅', callback_data='subscribed', url='https://t.me/aerojdbot?start=start')]
        ])
        user_channel_status = await message.bot.get_chat_member(chat_id='-1001917757220', user_id=message.from_user.id)
        if user_channel_status["status"] != 'left':
            return True
        else:
            await message.bot.send_message(message.from_user.id, '‼ Необходимо подписаться на канал ‼', reply_markup=inline_keyboard)
