from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
btnProf = KeyboardButton('Профиль🎟')
mainMenu.add(btnProf)