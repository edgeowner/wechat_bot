#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-26 15:34
# @Author  : sunny.zhang
# @Site    :
# @File    : kafka_adapter.py
# @Software: PyCharm


import os
import time
import logging
from config.config import cfg
from kafkatool.client.producer import Producer
from kafkatool.config.kconf import KProducerConf

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
HEAD_STATIC_FOLDER = os.path.join(PROJECT_ROOT)
from kafkatool.client.sede import json_ser, json_der


class KafkaProduce:

    def __init__(self):
        self.producer_config = KProducerConf({'acks': 'all'},
                                             HEAD_STATIC_FOLDER + '/producer_conf.yaml')
        # './producer_conf.yaml')
        self.producer = Producer(self.producer_config, on_delivery=None, value_ser=json_ser)
        # self.producer = Producer(self.producer_config, on_delivery=None)
        self.topic = 'draftelf.draft.wechat.raw'

    def send_wxchat_msg(self, msg):
        start = time.time()
        try:
            self.producer.produce(topic=self.topic, value=msg)
            end = time.time()
            print(msg)
            print(f"total time: {(end - start)} seconds")
        except Exception as e:
            logging.error("Kafka - [send_wxchat_msg] - execute error: %s", e)
            print(e)
        finally:
            end = time.time()
            print(f"total time: {(end - start)} seconds")
            self.close()

    def close(self):
        self.producer.close()






