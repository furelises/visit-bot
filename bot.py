import telebot
import info
from dotenv import dotenv_values

config = dotenv_values(".env")
token = config['token']
bot = telebot.TeleBot(token=token)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, 'Hi there this bot sends you the description of one chraracter.')
    bot.send_message(message.chat.id, "check out the list of the commands:/help")
    bot.send_message(message.chat.id, info.project_to_str())


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, 'This bot sends you the description of one chraracter.')
    bot.send_message(message.chat.id, """/showthedescription - shows the description of the chater.
/showcontacts - shows character`s skills
/getphoto - bot sends a photo to you.""")


@bot.message_handler(commands=['showthedescription'])
def descrip_command(message):
    bot.send_message(message.chat.id, info.character_description_str())


@bot.message_handler(commands=['showcontacts'])
def descrip_command(message):
    bot.send_message(message.chat.id, info.contacts_to_str())


@bot.message_handler(commands=['getphoto'])
def photo_command(message):
    bot.send_photo(message.chat.id, info.get_photo())


@bot.message_handler(content_types=['text'])
def hello_saying(message):
    if "hello" in message.text.lower():
        bot.send_message(message.chat.id, "hello")
    elif "bye" in message.text.lower():
        bot.send_message(message.chat.id, "bye")
    else:
        bot.send_message(message.chat.id, "i will think about it... :)")


bot.polling()
# @bot.message_handler(commands=['help'])
