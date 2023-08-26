from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from tgbot.misc.commands import Commands

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)

btnAviaSchedule = KeyboardButton(Commands.avia_schedule.value)
btnTrainSchedule = KeyboardButton(Commands.train_schedule.value)

mainMenu.add(btnAviaSchedule, btnTrainSchedule)

adminMainMenu = ReplyKeyboardMarkup(resize_keyboard=True)

btnAdmin = KeyboardButton(Commands.admin_menu.value)

adminMainMenu.add(btnAviaSchedule, btnTrainSchedule)
adminMainMenu.add(btnAdmin)

adminMenu = ReplyKeyboardMarkup(resize_keyboard=True)

btnSpeaker = KeyboardButton(Commands.mailing.value)
btnComeBack = KeyboardButton(Commands.come_back.value)
btnUpdateParser = KeyboardButton(Commands.update_parser.value)

adminMenu.add(btnSpeaker)
adminMenu.add(btnUpdateParser)
adminMenu.add(btnComeBack)

aviaMenu = ReplyKeyboardMarkup(resize_keyboard=True)

btnAviaTimetable = KeyboardButton(Commands.avia_timetable.value)
btnComeBack = KeyboardButton(Commands.come_back.value)

aviaMenu.add(btnAviaTimetable)
aviaMenu.add(btnComeBack)

trainMenu = ReplyKeyboardMarkup(resize_keyboard=True)

btnTrainArrival = KeyboardButton(Commands.train_arrival.value)

trainMenu.add(btnTrainArrival)
trainMenu.add(btnComeBack)