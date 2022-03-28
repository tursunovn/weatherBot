import requests
import datetime
from configs import open_weather_token, tg_bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши названия города для отображения погоды в нем!")


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data['name']
        cur_weather = data['main']['temp']
        wind = data['wind']['speed']
        hum = data['main']['humidity']
        pressure = data['main']['pressure']
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.date.fromtimestamp(data['sys']['sunset'])

        await message.reply(f"---> {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} <---\n"
              f"Погода в городе: {city}\nТемпература: {cur_weather}℃\n"
              f"Влажность:{hum}%\nДавление: {pressure}\nСкорость ветра: {wind} м/с\n"
              f"Восход солнца:{sunrise}\nЗакат:{sunset}"
              )



    except:
        await message.reply('Проверьте название города')



if __name__ == '__main__':
    executor.start_polling(dp)