import os
import requests
from dotenv import load_dotenv
load_dotenv()
import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN =os.getenv('API_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    username=message.from_user.username
    await message.reply(f""")
        Hi@ {username}
        Commands:
            1. /artist
            2. /albom
            3. /songs
    """)

@dp.message_handler(commands=['artist',])
async def send_artists(message: types.Message):
    artists_data=requests.get('http://127.0.0.1:8002/tg_api/artists_tg/').json()
    for artist in artists_data:
        await message.reply(f"""
            First Name: {artist['first_name']}
            Last Name: {artist['last_name']}
            Nick Name: {artist['nick_name']}
        """)

@dp.message_handler(commands=['albom',])
async def send_albom(message: types.Message):
    albom_data=requests.get('http://127.0.0.1:8002/tg_api/albom_tg/').json()
    for albom in albom_data:
        await message.reply(f"""
            Artist: {albom['artist']}
            Title: {albom['title']}
        """)

@dp.message_handler(commands=['songs',])
async def send_song(message: types.Message):
    song_data=requests.get('http://127.0.0.1:8002/tg_api/songs_tg/').json()
    for song in song_data:
        await message.reply(f"""
            Artist: {song['artist']}
            Title: {song['title']}
        """)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)