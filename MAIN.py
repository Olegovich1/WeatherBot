import json
import os
import telebot
import requests

token = str(os.environ.get('BOT_TOKEN'))
weatherKey = "0889d5c8d18829e4bbe61e9496387549"
bot = telebot.TeleBot(token)
def getweather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weatherKey}&units=metric&lang=ru "
    recponce = requests.get(url)
    if recponce.status_code == 200:
        data = recponce.json()
        cityNAME = data["name"]
        weatherDescription = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        windSpeed = data["wind"]["speed"]
        return (f"Погода в городе: {cityNAME}:\n"
                f"Описание: {weatherDescription}:\n"
                f"температура: {temp}\n"
                f"Влажность: {humidity}\n"
                f"скорость ветра: {windSpeed}\n")
    else:
        return "Город не найден,попробуйте снова "
@bot.message_handler(commands=["start"])
def defStart(message):
    bot.send_message(message.chat.id,"Привет,это бот для отпределения погоды by olegovich")
@bot.message_handler(func=lambda message:True)
def send_weather(message):
    city = message.text
    weather_info = getweather(city)
    bot.reply_to(message,weather_info)

































bot.polling()



































