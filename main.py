import requests
import datetime
from pprint import pprint
from configs import open_weather_token

def get_weather(city, open_weather_token):
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()


        city = data['name']
        cur_weather = data['main']['temp']
        wind = data['wind']['speed']
        hum = data['main']['humidity']
        pressure = data['main']['pressure']
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.date.fromtimestamp(data['sys']['sunset'])

        print(f"---> {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} <---\n"
              f"Погода в городе: {city}\nТемпература: {cur_weather}℃\n"
              f"Влажность:{hum}%\nДавление: {pressure}\nСкорость ветра: {wind} м/с\n"
              f"Восход солнца:{sunrise}\nЗакат:{sunset}"
               )



    except Exception as ex:
        print(ex)
        print('Проверьте название города')

def main():
    city = input("Введите название города: ")
    get_weather(city, open_weather_token)

if __name__=="__main__":
    main()