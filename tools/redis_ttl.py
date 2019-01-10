#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis
from redis_lru import RedisLRUCacheDict
from hashlib import md5


'''
文本hash过滤 utf-8编码
'''


class TTLFilter:
    def __init__(self, host='localhost', port=6379, db=1, _cap=1024000, _ttl=5*60):
        client = redis.StrictRedis()
        self.cache = RedisLRUCacheDict(
            max_size=_cap, expiration=_ttl, node=client)

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
    # i = 0
    # while True:
    #     tf = TTLFilter(_cap=1024000000, _ttl=5*60)
    #     tf.insert(str(i))
    #     i += 1
    def display_cached_value():
        if tf.isContains('http://www.baidu.com'):  # 判断字符串是否存在
            print('exists!')
        else:
            print('not exists!')

    import time
    tf = TTLFilter(_cap=128, _ttl=3)
    tf.insert('http://www.baidu.com')
    display_cached_value()

    time.sleep(4)
    display_cached_value()
