#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-26 15:34
# @Author  : sunny.zhang
# @Site    :
# @File    : kafka_adapter.py
# @Software: PyCharm

import time
import logging
import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from config.config import cfg
from database import Database
from kafka_adapter import kafka_adapter
from tools.hash_tools import hash_tool

sched = BlockingScheduler()


# @sched.scheduled_job('interval', hours=24, start_date='2018-12-21 12:01:00',id='manage_member_job')
def batch_send_job_function():
    print("***************************** START Manage_member_job_function ******************************")
    db = Database()

    resource = db.get_page_all_msg()

    for i in range(11):
        data = resource[i * 500: (i + 1) * 500]
        print("resource :{0}".format(resource))
        print("resource size :{0}".format(len(resource)))
        for da in data:
            sender_id = 0
            group_sender_name_str = str(da[4]).join(da[1])
            try:
                sender_id = hash_tool.get_str_hash(group_sender_name_str)
                print('sender_id:{0}'.format(sender_id))
            except Exception as e:
                print(e)
            if sender_id is 0:
                raise RuntimeError('sender_id init error')
            msg_create_time = datetime.datetime.now()
            msg_create_timestamp = int(msg_create_time.timestamp() * 1000)
            wechat_text = {
                'sid': sender_id,
                'nm': da[1],
                'head': "",
                'sex': 1,
                'prov': "上海",
                'city': "上海",
                'sig': "上海",
                'pno': "",
                'gn': da[4],
                'tp': 1,
                'text': da[3],
                'img': '',
                'st': int(da[7].timestamp() * 1000),
                'ts': msg_create_timestamp,
                'src': '1',
                'tags': ''
            }
            kafka_adapter.sender_wechat_msg(wechat_text)

    print("***************************** END Manage_member_job_function ******************************")


if __name__ == '__main__':
    log = logging.getLogger('apscheduler.executors.default')
    log.setLevel(logging.INFO)  # DEBUG
    fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
    h = logging.StreamHandler()
    h.setFormatter(fmt)
    log.addHandler(h)
    print('start to do it')
    batch_send_job_function()
    # Schedules job_function to be run on the third Friday
    #  of June, July, August, November and December at 00:00, 01:00, 02:00 and 03:00
    # sched.add_job(job_function, 'cron', day_of_week='0-6', hour='0-9', minute="*", second="*/4")
    # sched.add_job(batch_send_job_function, 'interval', hours=12, start_date='2019-01-02 18:59:00',
    #               id='manage_member_job')

    sched.add_job(batch_send_job_function, 'interval', minute=10, start_date='2019-01-02 20:21:00',
                  id='manage_member_job')
    # sched.add_job(job_function())
    # sched.add_job(job_function,'interval',)
    sched.start()
