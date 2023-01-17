import openai
import telebot
#можете изменить api ключ, но можете оставить этот просто вставив токен бота.
# openai.api_key = "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"
openai.api_key = "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"
bot = telebot.TeleBot("5977852572:AAHLKt_fFANC__2Wfx1p5tpCxvsyg_5go6E")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Как я могу Вам помочь?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt='Расскажи мне о ' + message.text + '?',
        max_tokens=2048,
        n = 1,
        stop=None,
        temperature=0.5,
    )
    bot.reply_to(message, response["choices"][0]["text"])

bot.polling()