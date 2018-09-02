import re
import random

import requests
from lxml import html
from telegram.ext import Updater, CommandHandler

DEBUG = 1

def __debug(msg):
    if DEBUG:
        print("\033[94m[DEBUG]\033[0m", msg)

def start(bot, update):
    __debug("CALL start")

    update.message.reply_text(
        "Selam! Sana nasıl yardım edebileceğimi öğrenmek için /help yazabilirsin.")

def help(bot, update):
    __debug("CALL help")

    update.message.reply_text(
        "/video_at - sana Youtube’da şu an trend olan videolardan birini atarım.\n"
		"/haber_at - sana BBC’de en çok okunan haberlerden birini atarım.\n\n"
        "/help - bu yardım mesajını gösterir")

def video_at(bot, update):
    __debug("CALL video_at")

    __debug(
        "video_at: Sending request to https://www.youtube.com/feed/trending")

    pg = requests.get("https://www.youtube.com/feed/trending")

    __debug("video_at: Got response: %d" % pg.status_code)

    if pg.status_code != 200:
        update.message.reply_text("Aman! Bir hata oldu :(")
        return

    video_list = re.findall('href="/watch\?v=\w{11}"', pg.text)

    if len(video_list) == 0:
        update.message.reply_text("Aman! Bir hata oldu! Hiç video bulamadım :(")
        return

    update.message.reply_text("https://youtube.com" + random.choice(video_list)[6:-1])

def haber_at(bot, update):
    __debug("CALL haber_at")

    __debug("haber_at: Sending request to https://www.bbc.com/news")

    pg = requests.get("https://www.bbc.com/news")

    __debug("haber_at: Got response: %d" % pg.status_code)

    if pg.status_code != 200:
        update.message.reply_text("Aman! Bir hata oldu :(")
        return

    tree = html.fromstring(pg.text)

    news_list = list()
    for i in range(1, 11):
        elem = tree.xpath("//li[@data-entityid='most-popular-read-{}']//a".format(i))

        if elem != []:
            news_list.append(elem[0])

    if len(news_list) == 0:
        update.message.reply_text("Aman! Bir hata oldu! Hiç haber bulamadım :(")
        return

    update.message.reply_text("https://www.bbc.com" + random.choice(news_list).attrib["href"])

def main():
    __debug("CALL main")

    __debug("main: Initializing updater")
    updater = Updater("BOT TOKEN")
    dp = updater.dispatcher

    __debug("main: Configuring handlers")
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("video_at", video_at))
    dp.add_handler(CommandHandler("haber_at", haber_at))

    __debug("main: Starting idle process")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
