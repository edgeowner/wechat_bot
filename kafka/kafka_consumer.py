#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-26 15:34
# @Author  : sunny.zhang
# @Site    :
# @File    : kafka_adapter.py
# @Software: PyCharm

import os

from kafkatool.client.consumer import Consumer
from kafkatool.config.kconf import KConsumerConf
from kafkatool.client.sede import json_ser,json_der

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
HEAD_STATIC_FOLDER = os.path.join(PROJECT_ROOT)


class KafkaConsumer:

    def __init__(self):
        self.consumer_config = KConsumerConf({'auto.offset.reset': 'latest'},
                                             HEAD_STATIC_FOLDER + '/consumer_conf.yaml')
        # './consumer_conf.yaml')
        self.client = Consumer(self.consumer_config, on_commit=None, value_der=json_der)

    def get_wechat_msg_topic(self):
        client = self.client
        for msg, raw in client:
            # do work here
            print(msg)
            # print(f"{raw.partition()},{raw.offset()},{raw.topic()}")
            client.commit(message=raw, asynchronous=True)
    # client = self.client
    # for msg in client:
    #     print(msg)


kafka_consumer = KafkaConsumer()

if __name__ == '__main__':
    kafka_consumer.get_wechat_msg_topic()
