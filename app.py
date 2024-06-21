import telebot
from PIL import Image
bot = telebot.TeleBot("6566449159:AAFJ40vTajw1SVmBcZuuhFgkly6rVTFRkz0")

@bot.message_handler(content_types=['photo'])
def file_handler(msg):
    print(msg)
    raw = msg.photo[2].file_id
    path = raw + ".jpg"
    file_info = bot.get_file(raw)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(path, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.send_message(msg.chat.id, text="Rasm qabul qilindi.Kuting...")
    with open(path, 'rb') as files:
        i = Image.open(files)
        i.resize((222, 333))
        i.save(path)
        bot.send_photo(msg.chat.id, i)
@bot.message_handler(content_types=['text'])
def text_handler(msg):
    print(msg)



bot.polling(none_stop=True)

