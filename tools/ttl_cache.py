#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cachetools import TTLCache
from hashlib import md5


'''
文本hash过滤 utf-8编码
'''


class TTLFilter:
    def __init__(self, _cap=102400, _ttl=300):
        self.cache = TTLCache(maxsize=_cap, ttl=_ttl)

    def isContains(self, str_input):
        if not str_input:
            return False
        m5 = md5()
        m5.update(str_input.encode('utf-8'))
        name = m5.hexdigest()
        return name in self.cache

    def insert(self, str_input):
        if not str_input:
            return
        m5 = md5()
        m5.update(str_input.encode('utf-8'))
        name = m5.hexdigest()
        self.cache[name] = True


ttl_filter = TTLFilter()

if __name__ == '__main__':
    # 339M
    # i = 0
    # while True:
    #     cache[i] = 'asklda;lhioqwhnkasncodihwpoihkndahsodihpihweopqi'
    #     i += 1
    def display_cached_value():
        if tf.isContains('http://www.baidu.com'):  # 判断字符串是否存在
            print('exists!')
        else:
            print('not exists!')

    from apscheduler.schedulers.blocking import BlockingScheduler

    tf = TTLFilter(_cap=128, _ttl=3)
    tf.insert('http://www.baidu.com')
    scheduler = BlockingScheduler()
    scheduler.add_job(display_cached_value, 'interval', seconds=1, args=[])
    scheduler.start()
