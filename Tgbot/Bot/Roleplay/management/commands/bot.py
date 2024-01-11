import asyncio
from aiogram import Bot, Dispatcher, executor, types
from .config import TOKEN
import sqlite3
from django.core.management.base import BaseCommand

bot = Bot(token=TOKEN)
loop = asyncio.get_event_loop()
dp = Dispatcher(bot, loop=loop)

class Command(BaseCommand):
    help = 'Telegram bot'

    def handle(self, *args, **options):
        print("fuck")

@bot.message_handler(commands=['start'])
def main(message):
    msg = bot.send_message(message.chat_id, 'Привет, это ролевая игра *День студента КПК*\nКак тебя зовут?')
    bot.register_next_step_handler(msg, nickname_step)

def nickname_step(message):
    user_info = {}
    user_info['name'] = message.text
    msg = bot.send_message(message.chat.id, 'введите имя')
    bot.register_next_step_handler(msg, user_info)

@dp.message_handler(content_types=['text'])
async def get_text(message: types.Message):
    name = open('replic_player.txt','+w', encoding='utf-8') 
    name.write(message.text)
    name.close()
    await bot.send_message(chat_id=message.chat.id, text='Отлично ваше имя записано')


@dp.message_handler(commands=['users_info'])
def user_info(message):
    database = sqlite3.connect('database_users.sql')
    command = database.cursor()
    command.execute('SELECT * FROM Users')
    users = command.fetchall()
    info=''
    for user in users:
        info += f'Никнейм:@{user[1]} ID:{user[2]}\n'
    command.close()
    database.close()
    bot.send_message(message.chat.id, info)

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)




