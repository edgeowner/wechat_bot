#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-26 15:34
# @Author  : sunny.zhang
# @Site    :
# @File    : kafka_adapter.py
# @Software: PyCharm

import io
import re
import os
import sys
import base64
import datetime

from hashlib import md5
from PIL import Image
from filecmp import cmp
from time import *
from wxpy import *

from kafka_adapter import KafkaAdapter
from send_message import SendTool
from tools.hash_tools import hash_tool
from database import Database
from config.config import cfg
from tools.filter import Filter
from tools.regex_tools import regex_tool
from tools.oss2 import OSS2
from kafka_adapter import kafka_adapter

bot = Bot(cache_path=True, console_qr=cfg.getint(
    'CONSOLE_QR'), logout_callback=sys.exit)
map = bot.enable_puid()
itchat = bot.core
bot.groups(update=False, contact_only=False)
# groups = bot.groups()
# for group_tmp in groups:
#     group_tmp.update_group(True)

oss2 = OSS2(cfg['ACCESS_KEY_ID'], cfg['ACCESS_KEY_SECRET'])

filter = Filter()


@bot.register(except_self=False)
def save_messages(msg):
    # 获取城市、签名、省份需 以下两行代码
    # msg.chat.update_group(True)

    send_time = msg.create_time  # 消息发送时间
    send_timestamp = int(send_time.timestamp() * 1000)

    print(msg)
    if msg is None or msg.type is None or msg.member is None:
        return
    member = msg.member
    print(msg)

    ######################### 获取头像 START ###########################
    # 文本信息处理,将包含有关键字信息的内容保存

    sender_name = member.name
    group_name = member.group.name
    user_name = member.user_name
    # itchat.get_head_img获取头像user_name
    # itchat.get_head_img获取头像chatroomUserName
    group_user_name = member._group_user_name

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))  # 图片文件存放工程目录
    ######################### 获取头像 START ###########################
    HEAD_STATIC_FOLDER = os.path.join(PROJECT_ROOT, 'static/head/')
    head_file_name = ''
    try:
        image_base64_data = itchat.get_head_img(userName=user_name, chatroomUserName=group_user_name)
        print(msg.raw['Content'])
        hash_base64 = hash_tool.get_base64_hash(image_base64_data)
        print('hash_base64 :{0}'.format(hash_base64))
        if not filter.isContains(1, image_base64_data):
            head_file_name = hash_base64 + '.jpg'
            save_path = HEAD_STATIC_FOLDER + head_file_name
            with open(save_path, 'wb') as f:
                f.write(image_base64_data)
            oss2.upload(head_file_name, save_path)
            filter.insert(1, image_base64_data)
            print('upload filepath head_file_name:', head_file_name)
        print()
    except Exception as e:
        print(e)
    ######################### 获取头像 END ###########################

    sender_id = 0
    group_sender_name_str = str(group_name).join(sender_name)
    try:
        sender_id = hash_tool.get_str_hash(group_sender_name_str)
        print('sender_id:{0}'.format(sender_id))
    except Exception as e:
        print(e)
    if sender_id is 0:
        raise RuntimeError('sender_id init error')

    msg_type = None
    file_name = ''
    sender_picture_url = None
    send_mq_flag = False  # 判断消息是否重复标记

    if ((msg.text is not None) and len(msg.text)) > 0:
        print("***************************** START Text ******************************")
        msg_type = 0
        if not filter.isContains(msg_type, msg.text):
            send_mq_flag = True
    ######################### 群消息 文本处理 END ###########################
    elif str(msg.type) is 'Picture':
        msg_type = 1
        try:
            MSG_STATIC_FOLDER = os.path.join(PROJECT_ROOT, 'static/')
            msg_image_data = msg.get_file()
            hash_base64 = hash_tool.get_base64_hash(msg_image_data)
            print('hash_base64 :{0}'.format(hash_base64))
            sender_picture_url = hash_base64 + '.jpg'
            msg_save_path = MSG_STATIC_FOLDER + sender_picture_url
            if not filter.isContains(1, msg_image_data):
                with open(msg_save_path, 'wb') as f:
                    f.write(msg_image_data)
                filter.insert(1, msg_image_data)
                oss2.upload(sender_picture_url, msg_save_path)
                print('upload filepath:', file_name)
                send_mq_flag = True
            else:
                print('Same Msg Picture:{0}'.format(sender_picture_url))
            print("***************************** End  Picture ******************************")
        except Exception as e:
            print(e)
            raise RuntimeError(str())

    msg_create_time = datetime.datetime.now()
    msg_create_timestamp = int(msg_create_time.timestamp() * 1000)

    db = Database()
    # 组装message数据并存入DB
    message_obj = {
        'sender_id': sender_id,
        'sender_name': sender_name,
        'sender_img': file_name,
        'group_name': group_name,
        'type': msg_type,
        'text': msg.text,
        'url': sender_picture_url,
        'msg_id': msg.id,
        'bot_name': msg.bot.self.name,
        'send_time': send_time,
        'create_time': msg_create_time
    }
    msg_return = db.insert_message(message_obj)
    print('msg : {0}'.format(message_obj['text']))
    print('insert message success ! message_obj_return : {0}'.format(msg_return))

    phone_name = sender_name
    phone_signature = member.signature
    phones = ''
    phones_name = ''
    phones_signature = ''

    if phone_name is not None:
        phones_name = regex_tool.get_phone_number(phone_name)
    if phone_signature is not None and len(phone_signature) > 0:
        phones_signature = regex_tool.get_phone_number(phone_signature)

    if len(phones_signature) > 0:
        phones = phones_name + ',' + phones_signature
    if not len(phones_signature) == 0:
        phones = phones_name

    # 组装sender数据并存入DB
    sender_obj = {
        'name': sender_name,
        'sender_id': sender_id,
        'head_url': head_file_name,
        'sex': member.sex,
        'province': member.province,
        'city': member.city,
        'signature': member.signature,
        'phones': phones,
    }

    sender_return = db.insert_sender(sender_obj)
    print('insert sender success ! message_obj_return : {0}'.format(sender_return))
    # 组装MQ消息
    wechat_text = {
        'sid': sender_id,
        'nm': sender_name,
        'head': head_file_name,
        'sex': member.sex,
        'prov': member.province,
        'city': member.city,
        'sig': member.signature,
        'pno': phones,
        'gn': group_name,
        'tp': msg_type,
        'text': msg.text,
        'img': sender_picture_url,
        'st': send_timestamp,
        'ts': msg_create_timestamp,
        'src': '1',
        'tags': ''
    }

    # 如果消息未重复则发
    if send_mq_flag:
        print('send_mq_flag True:{0}'.format(send_mq_flag))
        # kafka_adapter.sender_wechat_msg(wechat_text)
    else:
        print('send_mq_flag False:{0}'.format(send_mq_flag))
    print("***************************** END Text ******************************")

    print("***************************** END Picture ******************************")


msg = bot.messages

embed()

