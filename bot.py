import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message

bot = Bot('6964152383:AAHHjZuiZFASsuCr8UafFavnq4j5zJ_Pe4Y')
loop = asyncio.get_event_loop()
dp = Dispatcher(bot, loop=loop)


@dp.message_handler(commands=['start'])
async def message(message: types.Message):
    await message.reply('Привет, это ролевая игра *Будний день студента КПК*\nКак тебя зовут?')


@dp.message_handler()
async def messages(message: Message):
    await bot.send_message(
    chat_id=message.from_user.id,
    text=message.text,
    )


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)




