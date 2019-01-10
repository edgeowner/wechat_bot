#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tools.redis_filter import BloomFilter
from tools.redis_ttl import TTLFilter


class Filter(object):
    def __init__(self):
        self.tf = TTLFilter()
        self.bf = BloomFilter()

    def isContains(self, ftype, str_input):
        if ftype == 0:
            return self.tf.isContains(str_input)  # 文本hash过滤
        elif ftype == 1:
            return self.bf.isContains(str_input)  # 图片hash过滤
        else:
            raise Exception('unknow msg.type')

    def insert(self, ftype, str_input):
        if ftype == 0:
            return self.tf.insert(str_input)
        elif ftype == 1:
            return self.bf.insert(str_input)
        else:
            raise Exception('unknow msg.type')
