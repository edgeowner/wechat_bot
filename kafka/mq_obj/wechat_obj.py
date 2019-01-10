#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-26 16:08
# @Author  : sunny.zhang
# @Site    :
# @File    : wechat_obj.py
# @Software: PyCharm


class WechatText:
    sid = ''  # 发送者唯一标识（必要字段)
    nm = ''  # 群成员昵称(必要字段)
    head = ''  # 群成员头像(必要字段）
    sex = 0  # 群成员性别：0:未知， 1:男 2:女(必要字段)
    prov = ''  # 群成员所在省份(可空)
    city = ''  # 群成员所在城市(可空)
    sig = ''  # 群成员个人签名(可空)
    pno = ''  # 群成员电话号吗(可空 多个以英文逗号分隔 eg.: 12323123,3123231,131232）
    gn = ''  # 消息群成员所在群昵称(必要字段)
    tp = ''  # 消息类型0:Text,1:Picture(必要字段)
    text = ''  # 消息发送文本内容(若type=0 text非空 ，type=1，text为空)
    img = ''  # 消息发送图片文件名（type=0 url为空，type=1，text非空）
    st = ''  # 消息发送时间（必要字段）

    # "gg":0  tags标签 国股 1:是 0:否
    # "cs":0  tags标签 城商 1:是 0:否
    # "wz":0  tags标签 外资 1:是 0:否
    # "sn":0  tags标签 三农 1:是 0:否
    # "cz":0  tags标签 村镇 1:是 0:否
    # "cw":0  tags标签 财务 1:是 0:否
    # "sp":0  tags标签 商票 1:是 0:否

    tags = dict(gg=0, cd=0, wz=0, sn=0, cz=0, cw=0, sp=0)

    '''
    :param sid: 发送者唯一标识（必要字段)
    :param nm: 发送者唯一标识（必要字段)
    :param head: 发送者唯一标识（必要字段)
    :param sex: 发送者唯一标识（必要字段)
    :param prov: 发送者唯一标识（必要字段)
    :param city: 发送者唯一标识（必要字段)
    :param sig: 发送者唯一标识（必要字段)
    :param pn: 发送者唯一标识（必要字段)
    :param gn: 发送者唯一标识（必要字段)
    :param tp: 发送者唯一标识（必要字段)
    :param text: 发送者唯一标识（必要字段)
    :param img: 发送者唯一标识（必要字段)
    :param st: 发送者唯一标识（必要字段)
    '''
    def __init__(self, sid, nm, head, sex, prov, city, sig, pn, gn, tp, text, img, st):
        self.sid = sid
        self.nm = nm
        self.head = head
        self.sex = sex
        self.prov = prov
        self.city = city
        self.sig = sig
        self.pno = pn
        self.gn = gn
        self.tp = tp
        self.text = text
        self.img = img
        self.st = st

    # def __repr__(self):
    #     return self.__str__()
