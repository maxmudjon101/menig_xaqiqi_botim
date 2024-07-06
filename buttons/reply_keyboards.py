from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def admin_btn():
    btn = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=3)
    statistika = KeyboardButton("Statistika")
    movies = KeyboardButton("Kinolar")
    reklama = KeyboardButton("Reklama")
    add_chanell = KeyboardButton("Kanallar")
    return btn.add(statistika, movies, reklama, add_chanell)


def movies_btn():
    btn = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    statistika = KeyboardButton("Kino Statistikav")
    add_movie = KeyboardButton("Kino qo'shish")
    delete_movie = KeyboardButton("Kino o'chirish")
    exits = KeyboardButton("Chiqish")
    return btn.add(statistika, add_movie, delete_movie, exits)


def channels_btn():
    btn = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    add_channel = KeyboardButton("Kanal qo'shish")
    delete_channel = KeyboardButton("Kanal o'chirish")
    exits = KeyboardButton("Chiqish")
    return btn.add(add_channel, delete_channel, exits)


def exit_btn():
    btn = ReplyKeyboardMarkup(one_time_keyboard=True, row_width=2, resize_keyboard=True)
    return btn.add("Chiqish")
