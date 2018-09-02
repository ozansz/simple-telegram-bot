#!/bin/bash
set -e

echo -e "[+] Installing dependencies ...\n"

sudo apt-get install python3-pip
pip3 install -r requirements.txt

echo -e "\n[+] Running bot ...\n"

python3 bot.py
