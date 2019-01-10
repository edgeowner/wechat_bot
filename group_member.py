#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-26 15:34
# @Author  : sunny.zhang
# @Site    :
# @File    : kafka_adapter.py
# @Software: PyCharm

import os
import sys
import time

from wxpy import Bot
from database import db
from tools.hash_tools import hash_tool
from tools.oss2 import OSS2
from config.config import cfg

oss2 = OSS2(cfg['ACCESS_KEY_ID'], cfg['ACCESS_KEY_SECRET'])
oss2_url = cfg['OSS_URL']

robot = Bot(cache_path=True, console_qr=cfg.getint('CONSOLE_QR'), logout_callback=sys.exit)
robot.groups(update=True, contact_only=False)
groups = robot.groups()
itchat = robot.core


class GroupMember:

    def manager_group_member(self):
        print("***************************** MANAGER_GROUP_MEMBER START ******************************")
        if groups is not None and len(groups) > 0:
            # group_data_insert_list = []
            member_data_insert_list = []
            none_name_member_list = []
            for group_tmp in groups:
                print('group_name:{0}'.format(group_tmp.name))
                print('************************* GROUP START *********************************')
                group_tmp.update_group(True)
                members = group_tmp.members
                chatroomUserName = group_tmp.user_name
                member_data_insert_list.clear()
                if members is not None and len(members) > 0:

                    for member in members:
                        member_user_name = member.user_name
                        if member.name is None:
                            none_name_member_list.append(member)
                            continue

                        # 生成sender_id
                        sender_id = 0
                        group_sender_name_str = str(group_tmp.name).join(member.name)
                        try:
                            sender_id = hash_tool.get_str_hash(group_sender_name_str)
                            print('sender_id:{0}'.format(sender_id))
                        except Exception as e:
                            print(e)
                        if sender_id is 0:
                            raise RuntimeError('sender_id init error')
                        # 获取头像图片
                        PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
                        HEAD_STATIC_FOLDER = os.path.join(PROJECT_ROOT, 'static/head/')
                        file_name = ''
                        try:
                            image_base64_data = itchat.get_head_img(userName=member_user_name,
                                                                    chatroomUserName=chatroomUserName)
                            hash_base64 = hash_tool.get_base64_hash(image_base64_data)
                            file_name = oss2_url + hash_base64 + '.jpg'
                            save_path = HEAD_STATIC_FOLDER + file_name
                            with open(save_path, 'wb') as f:
                                f.write(image_base64_data)
                            oss2.upload(file_name, save_path)
                            filter.insert(1, image_base64_data)
                        except Exception as e:
                            print(e)

                        # 插入数据组装
                        tuple_member = (
                            member.name,
                            group_tmp.name,
                            sender_id,
                            member.sex,
                            file_name,
                            member.signature,
                            member.province,
                            member.city,
                            member.raw['PYQuanPin'],
                            member.raw['PYInitial']
                        )
                        # list数组添加群成员元组
                        member_data_insert_list.append(tuple_member)
                    member_count = db.batch_insert_members(member_data_insert_list)
                    print('group:{0}, member_count:{1}'.format(group_tmp.name, member_count))
                print('************************* GROUP END *********************************')
            print('None data:{0}'.format(none_name_member_list))
            # print('group_data_insert_list:{0}'.format(group_data_insert_list))
            # print('member_data_insert_list:{0}'.format(member_data_insert_list))
            # db.batch_insert_group(group_data_insert_list)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
        print("***************************** END Job_function ******************************")


group_member = GroupMember()

if __name__ == '__main__':
    group_member = GroupMember()
    group_member.manager_group_member()
    # strs = '1231231'
    # print(strs)
    # print(hash_tool.get_str_hash(strs))
    # print(len(str(hash_tool.get_str_hash(strs))))
    # print(hash_tool.get_base64_hash())
