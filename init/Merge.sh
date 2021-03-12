#!/bin/bash

export SEMAPHORE_PROJECT_DIR=`pwd`
. "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")"/telegram
TELEGRAM_TOKEN=${BOT_API_KEY}
export BOT_API_KEY TELEGRAM_TOKEN
tg_sendinfo "<code>I am gonna merge staging into Decha-Userbot</code>"
cd
git clone https://github.com/ayay182/Decha-Userbot.git
cd oub-remix
git remote set-url origin https://${GH_USERNAME}:${GH_PERSONAL_TOKEN}@github.com/ayay182/Decha-Userbot.git
git fetch
git checkout staging
git pull origin staging
git push --force origin staging:sql-extended
tg_sendinfo "<code>I have merged all commits from staging into Decha-Userbot</code>"
