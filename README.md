# simple-telegram-bot
A simple Telegram bot example using python-telegram-bot library

## Usage
First, clone this repo:

```shell
git clone https://github.com/ozansz/simple-telegram-bot
cd simple-telegram-bot
```

To run the bot, change the `"BOT TOKEN"` string in the line <a href="https://github.com/ozansz/simple-telegram-bot/blob/master/bot.py#L57">#57</a> with the token of your bot. Then just run the `deploy.sh` script. The script will install all dependencies and then start the bot.

```shell
chmod +x deploy.sh
./deploy.sh
```

Or you can just run the `bot.py` script itself:

```shell
python3 bot.py
```

### Debug

You can toggle extra debug messages through the `DEBUG` variable in `bot.py` file.

`DEBUG = 0` means no extra debug messages will be printed.

## Bot Commands

### /start

Starts the initial dialog with the bot.

### /help

Shows help message which contains information about bot commands.

### /video_at

Sends the user a video from Youtube's trend videos randomly.

### /haber_at

Send user a news from BBC's most read news
