import logging 
from aiogram import Bot, Dispatcher, executor, types
import cfg
import markups as nav
from db import Database

logging.basicConfig(level=logging.INFO)

bot = Bot(token=cfg.TOKEN)
dp=Dispatcher(bot)
db = Database('database.db')

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        if not db.user_exists(message.from_user.id):
            start_command = message.text 
            referrer_id = str(start_command[7:])
            if str(referrer_id) != "":
                if str(referrer_id) != str(message.from_user.id):
                    db.add_user(message.from_user.id, referrer_id)
                    try:
                        await bot.send_message(referrer_id, "По вашей ссылке зарегестрировался новый пользователь!")
                    except:
                        pass
                else:
                    await bot.send_message(message.from_user.id, "Вы уже зарегестрированы по ссылке!")
            else:
                db.add_user(message.from_user.id)
        
        await bot.send_message(message.from_user.id, "Добро пожаловать! Жмякай на кнопку =D", reply_markup=nav.mainMenu)

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'Профиль🎟':
            await bot.send_message(message.from_user.id, f"ID: {message.from_user.id}\nhttps://t.me/{cfg.BOT_NICKNAME}?start={message.from_user.id}\nКол-во рефералов: {db.count_reeferals(message.from_user.id)}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)