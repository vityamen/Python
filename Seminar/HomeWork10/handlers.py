from bot import dp
from aiogram import types
from keyb import kb_candy
import random

candy = 121

def win(candy):
    if candy <= 0:
        return True
    else:
        return False

def comp_take():
    return random.randint(1, 29)

# Хэндлер на команду /start
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("For play type /game")

@dp.message_handler(commands=["new_game"])
async def newgame(message:types.Message):
    global candy
    candy = 121
    await message.answer(
        'Поиграем. Правила:\n Ходим по очереди, за один ход можно снять от 1 до 28 конфет. Стартовое количество 121 конфет.\n '
        'Кто оставит после своего хода пустой стол, тот и победил. Ваш ход', reply_markup=kb_candy)


@dp.message_handler(commands=["game"])
async def cmd_game_start(message: types.Message):
    await message.answer('Поиграем. Правила:\n Ходим по очереди, за один ход снять можно от 1 до 28 конфет. Стартовое количество 121 конфет.\n '
                         'Кто оставит после своего хода пустой стол, тот и победил. Ваш ход', reply_markup=kb_candy)

@dp.callback_query_handler()
async def process_callback(callback: types.CallbackQuery):
    global candy
    data = callback.data
    if win(candy):
        await callback.answer('Я победил\nЗахочешь заново набери /new_game')
        return 1
    await callback.answer(f'вы забрали {data} конфет')
    candy = candy - int(data)
    if candy <= 0 :
        await callback.message.answer(f'ты победил \nЗахочешь заново набери /new_game')
        return 1
    else:
        await callback.message.answer(f'осталось {candy} конфет')
    candy = candy - comp_take()
    if win(candy):
        await callback.message.answer('я победил !!! \nЗахочешь заново набери /new_game')
    else:
        await callback.message.answer(f'я забрал {comp_take()}, осталось {candy} конфет')