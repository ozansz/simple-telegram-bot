#!/bin/bash
set -e

echo -e "\e[0;92m[INFO]\e[0m Installing dependencies ...\n"

sudo apt-get install python3-pip
pip3 install -r requirements.txt

echo -e "\n\e[0;92m[INFO]\e[0m Running bot ...\n"

python3 bot.py
