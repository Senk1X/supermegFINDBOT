
import telebot
import json
import os
from openai import OpenAI
from dotenv import load_dotenv
from telebot import types





load_dotenv()
client = OpenAI(api_key = os.getenv('API'))

bot = telebot.TeleBot(os.getenv('TG'))




@bot.message_handler(commands=["start"])
def engine__up(message): 
    bot.send_message(message.chat.id, "<b>Введите описание:</b>", parse_mode='html') 



    @bot.message_handler(content_types=['text'])
    def get_forgpt_answer(message):
        response = client.chat.completions.create(
            model='gpt-4',
            messages=[{"role": "user", "content": f"Найди 10 фильмов/аниме/сериалов по описанию: {message.text} и выведи ТОЛЬКО их НАЗВАНИЯ в нумерации без лишнего текста"}],
            temperature=0.1,
            max_tokens=3000,
            frequency_penalty=0
        )
        
        anfilser = (response.choices[0].message.content)
        list_anfilser = anfilser.split('\n')
       
        markup = types.InlineKeyboardMarkup()
        dd = (types.InlineKeyboardButton(list_anfilser[0], callback_data='btn4descrpt01'))
        markup.add(dd)
        dd1 = (types.InlineKeyboardButton(list_anfilser[1], callback_data='btn4descrpt02'))
        markup.add(dd1)
        dd2 = (types.InlineKeyboardButton(list_anfilser[2], callback_data='btn4descrpt03'))
        markup.add(dd2)
        dd3 = (types.InlineKeyboardButton(list_anfilser[3], callback_data='btn4descrpt04'))
        markup.add(dd3)
        dd4 = (types.InlineKeyboardButton(list_anfilser[4], callback_data='btn4descrpt05'))
        markup.add(dd4)
        dd5 = (types.InlineKeyboardButton(list_anfilser[5], callback_data='btn4descrpt06'))
        markup.add(dd5)
        dd6 = (types.InlineKeyboardButton(list_anfilser[6], callback_data='btn4descrpt07'))
        markup.add(dd6)
        dd7 = (types.InlineKeyboardButton(list_anfilser[7], callback_data='btn4descrpt08'))
        markup.add(dd7)
        dd8 = (types.InlineKeyboardButton(list_anfilser[8], callback_data='btn4descrpt09'))
        markup.add(dd8)
        dd9 = (types.InlineKeyboardButton(list_anfilser[9], callback_data='btn4descrpt10'))
        markup.add(dd9)
        bot.send_message(message.chat.id, 'Результаты поиска🔎:', reply_markup=markup)
        
    
    # @bot.callback_query_handler(func=lambda callback: True)
    # def descript_of_anfilser(callback):
    #     if callback.data == "btn4descrpt01":
    #         response = client.chat.completions.create(
    #         model='gpt-4',
    #         messages=[{"role": "user", "content": f"Найди описание для "}],
    #         temperature=0.3,
    #         max_tokens=3000,
    #         frequency_penalty=0
    #     )
    #     print(response.choices[0].message.content)   
            
    # В РАЗРАБОТКЕ
        
    
    
    
        
bot.polling(none_stop=True)