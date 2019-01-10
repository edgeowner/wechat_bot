#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-26 15:34
# @Author  : sunny.zhang
# @Site    :
# @File    : kafka_adapter.py
# @Software: PyCharm

import time
from wxpy import *
from apscheduler.schedulers.blocking import BlockingScheduler
from config.config import cfg
# from group_member import GroupMember
from msg_drop_duplicates import Dropduplicates

sched = BlockingScheduler()
# robot = Bot(cache_path=True, console_qr=cfg.getint('CONSOLE_QR'), logout_callback=sys.exit)
# itchat = robot.core


# @sched.scheduled_job('interval', hours=24, start_date='2018-12-21 12:01:00',id='manage_member_job')
# def manage_member_job_function():
#     print("***************************** START Manage_member_job_function ******************************")
#     groupmember = GroupMember()
#     groupmember.manager_group_member()
#     print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
#     print("***************************** END Manage_member_job_function ******************************")


def distinct_text_job_function():
    print("***************************** START Distinct_text_job_function ******************************")
    dropduplicates = Dropduplicates()
    dropduplicates.drop_dulicates()
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
    print("***************************** END Distinct_text_job_function ******************************")


if __name__ == '__main__':
    log = logging.getLogger('apscheduler.executors.default')
    log.setLevel(logging.INFO)  # DEBUG
    fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
    h = logging.StreamHandler()
    h.setFormatter(fmt)
    log.addHandler(h)
    print('start to do it')
    # Schedules job_function to be run on the third Friday
    #  of June, July, August, November and December at 00:00, 01:00, 02:00 and 03:00
    # sched.add_job(job_function, 'cron', day_of_week='0-6', hour='0-9', minute="*", second="*/4")
    # sched.add_job(manage_member_job_function, 'interval', hours=12, start_date='2018-12-26 14:50:00',
    #               id='manage_member_job')
    sched.add_job(distinct_text_job_function, 'interval', hours=24, start_date='2019-01-09 11:07:00',
                  id='distinct_text_job')
    # sched.add_job(job_function())
    # sched.add_job(job_function,'interval',)
    sched.start()
