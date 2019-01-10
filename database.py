#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-26 15:34
# @Author  : sunny.zhang
# @Site    :
# @File    : kafka_adapter.py
# @Software: PyCharm


import logging
import pymysql
from DBUtils.PooledDB import PooledDB, SharedDBConnection

from config.config import cfg

pool = PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxconnections=20,  # 连接池允许的最大连接数，0和None表示不限制连接数
    mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
    maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
    maxshared=3,
    # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
    blocking=False,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
    maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
    setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
    ping=0,
    # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
    host=cfg['HOST'],
    port=cfg.getint('PORT'),
    user=cfg['USER'],
    passwd=cfg['PASSWD'],
    database=cfg['DB'],
    charset=cfg['CHARSET']
)


class Database:

    def __init__(self):
        self.pool = pool

    def get_conn(self):
        return self.pool.connection()

    def insert_message(self, message):
        conn = pool.connection()
        cursor = conn.cursor()
        try:
            if message is not None:
                sql_insert = "INSERT INTO `message` (`sender_id`,`sender_name`,`sender_img`,`group_name`,`type`,`text`,`url`,`msg_id`,`rebot_name`,`send_time`,`is_delete`,`create_time`,`update_time`)" \
                             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 0, %s, NOW())"

                senderId = message['sender_id']
                senderName = message['sender_name']
                senderImg = message['sender_img']
                groupName = message['group_name']
                msgType = message['type']
                text = message['text']
                url = message['url']
                msgId = message['msg_id']
                rebotName = message['bot_name']
                sendTime = message['send_time']
                createTime = message['create_time']
                insert_tuple = (
                    senderId, senderName, senderImg, groupName, msgType, text, url, msgId, rebotName, sendTime,
                    createTime)
                cursor.execute(sql_insert, insert_tuple)
                conn.commit()
                return message
            else:
                raise RuntimeError('insert_message error, message is None')
        except Exception as e:
            print(e)
            logging.error("Method - [insert_message] - execute error: %s", e)
            conn.rollback()
        finally:
            cursor.close()

    def insert_sender(self, sender):
        conn = pool.connection()
        cursor = conn.cursor()
        try:
            if sender is not None:
                sql_insert = "INSERT INTO `sender` (`name`,`sender_id`,`head_url`,`sex`,`province`,`city`,`signature`,`phones`,`is_delete`,`create_time`,`update_time`)" \
                             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, 0, NOW(), NOW())"
                name = sender['name'],
                senderId = sender['sender_id']
                headUrl = sender['head_url']
                sex = sender['sex']
                province = sender['province']
                city = sender['city']
                signature = sender['signature']
                phones = sender['phones']

                insert_tuple = (name, senderId, headUrl, sex, province, city, signature, phones)
                cursor.execute(sql_insert, insert_tuple)
                conn.commit()
                return sender
            else:
                raise RuntimeError('insert_sender error, sender is None')
        except Exception as e:
            print(e)
            logging.error("Method - [insert_sender] - execute error: %s", e)
            conn.rollback()
        finally:
            cursor.close()

    def batch_insert_msg_distinct_text(self, wechat_distinct_text_tuple_list):
        conn = pool.connection()
        cursor = conn.cursor()
        try:
            if wechat_distinct_text_tuple_list is not None and len(wechat_distinct_text_tuple_list) > 0:
                sql_insert = "INSERT INTO `msg_distinct_text`(`message_id`, `sender_id`, `sender_name`,,`group`,`text`,`is_delete`,`can_use`,`create_time`,`update_time`)" \
                             " VALUES (%s, %s, %s, %s, %s, 0, 0,NOW(),NOW())"
                print(sql_insert)
                total_insert = cursor.executemany(sql_insert, wechat_distinct_text_tuple_list)
                conn.commit()
            print('total_insert :{0}'.format(total_insert))
            return total_insert
        except Exception as e:
            print(e)
            logging.error("Method - [batch_insert_msg_distinct_text] - execute error: %s", e)
            conn.rollback()
        finally:
            cursor.close()

    def batch_update_message(self, max_key):
        conn = pool.connection()
        cursor = conn.cursor()
        try:
            if max_key is not None and max_key > 0:
                sql_update = "UPDATE `message` SET is_delete =1 WHERE id <= %s and is_delete =0"
                print(sql_update)
                total_update = cursor.execute(sql_update, max_key)
                conn.commit()
            return total_update
        except Exception as e:
            print(e)
            logging.error("Method - [batch_update_messsage]: execute error: %s", e)
            conn.rollback()
        finally:
            cursor.close()

    def batch_insert_members(self, member_tuple_list):
        conn = pool.connection()
        cursor = conn.cursor()
        try:
            if member_tuple_list is not None and len(member_tuple_list) > 0:
                sql_insert = "INSERT INTO `group_member`(`name`, `group_name`, `sender_id`," \
                             "`sex`,`head_url`,`signature`,`province`,`city`," \
                             "`py_quan_pin`,`py_initial`,`is_delete`,`create_time`,`update_time`)" \
                             " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,0,NOW(),NOW())"
                print(sql_insert)
                total_insert = cursor.executemany(sql_insert, member_tuple_list)
                conn.commit()
            print('total_insert :{0}'.format(total_insert))
            return total_insert
        except Exception as e:
            print(e)
            logging.error("Method - [batch_insert_members] - execute error: %s", e)
            conn.rollback()
        finally:
            cursor.close()

    def get_page_all_msg(self):
        conn = pool.connection()
        cursor = conn.cursor()
        try:
            query_sql = "select `id`,`sender_name`,`sender_nickname`,`sender_text` ,`wechat_group`,`msg_id`,`msg_type`, `create_time` from `wechat_snapshot` limit 5500"
            print(query_sql)
            count = cursor.execute(query_sql)
            result = cursor.fetchall()
            conn.commit()
            print('get_all_msg :{0}'.format(result))
            return result
        except Exception as e:
            logging.error("Method - [get_page_all_msg] - execute error: %s", e)
            conn.rollback()
        finally:
            cursor.close()

    def __calStartIndex(self, currentPageIndex):
        startIndex = currentPageIndex * self.numPerPage
        return startIndex

    def close(self):
        pool.connection().close()

    def __del__(self):
        pool.close()


db = Database()
