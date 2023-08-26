from enum import Enum


class Commands(Enum):
    avia_schedule = 'Аэропорт ✈️'
    train_schedule = 'ЖД 🚆'
    avia_timetable = 'Расписание ✈️'
    train_arrival = 'Прибытие 🚉'
    come_back = '🔙 Вернуться в главное меню'
    update_parser = '🔄 Обновить расписания'
    mailing = '📻 Рассылка'
    admin_menu = '⚙ Админ меню'