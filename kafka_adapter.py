#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-26 15:34
# @Author  : sunny.zhang
# @Site    : 
# @File    : kafka_adapter.py
# @Software: PyCharm

from kafka.kafka_producer import KafkaProduce
from kafka.kafka_consumer import KafkaConsumer


class KafkaAdapter:

    def __init__(self):
        self.producer = KafkaProduce()
        self.consumer = KafkaConsumer()

    def sender_wechat_msg(self, msg):
        self.producer.send_wxchat_msg(msg)

    def consumer_wechat_msg(self):
        self.consumer.get_wechat_msg_topic()


kafka_adapter = KafkaAdapter()

if __name__ == '__main__':
    msg = '我是12345678'
    result = kafka_adapter.sender_wechat_msg(msg)
    print(msg)
