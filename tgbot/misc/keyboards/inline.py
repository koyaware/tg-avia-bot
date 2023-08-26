from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

cancel_inline = InlineKeyboardMarkup()

btnCancel = InlineKeyboardButton(text='❌ Отмена', callback_data='cancelbutton')

cancel_inline.insert(btnCancel)

mailing_inline = InlineKeyboardMarkup(row_width=1)

btnSendAll = InlineKeyboardButton(text="📟 Отправить всем пользователям", callback_data='send_all')

mailing_inline.insert(btnSendAll)