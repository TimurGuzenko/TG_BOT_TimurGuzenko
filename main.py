import requests
import datetime
from config import weather_tbot


def get_weather(city, weather_tbot):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Ливень \U000026C6",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F328",
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_tbot}&units=metric"
        )
        data = r.json()

        city = data['name']
        cur_weather = data['main']['temp']

        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окноь, не пойму что там!"

        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        lenght_of_the_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(data['sys']['sunrise'])

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n" \
        f"Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\n" \
        f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n" \
        f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {lenght_of_the_day}\n" \
        f"Хорошего дня!")

    except Exception as ex:
        print(ex)
        print('Проверьте название города')

def main():
    city = input("Введите город: ")
    get_weather(city, weather_tbot)

if __name__=='__main__':
    main()