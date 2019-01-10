#!/usr/bin/env bash
docker run -d --restart=always --env env=TEST -v /mnt/data1/echo77/wechat_bot/log:/usr/src/app/log -v /mnt/data1/echo77/wechat_bot/static:/usr/src/app/static --name wechat-bot wechat_bot
