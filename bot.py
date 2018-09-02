import re
import random

import requests
from lxml import html
from telegram.ext import Updater, CommandHandler

def start(bot, update):
    update.message.reply_text(
        "Selam! Sana nasıl yardım edebileceğimi öğrenmek için /help yazabilirsin.")

def help(bot, update):
	update.message.reply_text(
        "/video_at - sana Youtube’da şu an trend olan videolardan birini atarım.\n"
		"/haber_at - sana BBC’de en çok okunan haberlerden birini atarım.\n\n"
        "/help - bu yardım mesajını gösterir")

def video_at(bot, update):
    pg = requests.get("https://www.youtube.com/feed/trending")

    if pg.status_code != 200:
        update.message.reply_text("Aman! Bir hata oldu :(")
        return

    video_list = re.findall('href="/watch\?v=\w{11}"', pg.text)

    if len(video_list) == 0:
        update.message.reply_text("Aman! Bir hata oldu! Hiç video bulamadım :(")
        return

    update.message.reply_text("https://youtube.com" + random.choice(video_list)[6:-1])

def haber_at(bot, update):
    pg = requests.get("https://www.bbc.com/news")
    print("+get", flush=True)
    if pg.status_code != 200:
        update.message.reply_text("Aman! Bir hata oldu :(")
        return

    tree = html.fromstring(pg.text)

    news_list = list()
    print("-for", flush=True)
    for i in range(1, 11):
        elem = tree.xpath("//li[@data-entityid='most-popular-read-{}']//a".format(i))
        print("  ~for elem:", elem, flush=True)
        if elem != []:
            news_list.append(elem[0])
    print("+for news_list:", news_list)
    if len(news_list) == 0:
        update.message.reply_text("Aman! Bir hata oldu! Hiç haber bulamadım :(")
        return

    update.message.reply_text("https://www.bbc.com" + random.choice(news_list).attrib["href"])

def main():
    updater = Updater("BOT TOKEN")
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("video_at", video_at))
    dp.add_handler(CommandHandler("haber_at", haber_at))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
