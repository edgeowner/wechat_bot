#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-26 15:34
# @Author  : sunny.zhang
# @Site    :
# @File    : kafka_adapter.py
# @Software: PyCharm


import pandas as pd
from database import db
from send_message import SendTool

'''

执行脚本去重复
'''


class Dropduplicates:

    @classmethod
    def drop_dulicates(self):
        conn = db.get_conn()
        sql = 'select `id`, `sender_id`,`sender_name`,`group_name`,`text` from `message` where `type` = 0 and `is_delete`= 0 order by id desc ;'
        columns = ['id', 'sender_id', 'sender_name', 'group_name', 'text']
        df_mysql = pd.read_sql(sql, conn, None, True, None, None, columns)
        resource_list = df_mysql.values.tolist()

        len("resource_list:{0}".format(resource_list))

        print(resource_list)
        wechat_distinct_text_list = df_mysql.drop_duplicates(['text']).values.tolist()
        print(len(wechat_distinct_text_list))
        if wechat_distinct_text_list is not None and len(wechat_distinct_text_list) > 0:
            print("***************************** Filter Batch Insert START  ******************************")
            id_list = []
            data_insert_list = []
            for wechat_text in wechat_distinct_text_list:
                print('distinct_text :', wechat_text)
                ## 构造批量插入元组
                tup_1 = (wechat_text[0],
                         wechat_text[1],
                         wechat_text[2],
                         wechat_text[3],
                         wechat_text[4])
                data_insert_list.append(tup_1)  ## 去重插入消息元组 list
                id_list.append(wechat_text[0])  ## 更新消息镜像表状态主键ID list
            max_key = max(id_list)
            print("data_insert_list to insert:{0}".format(data_insert_list))
            print(db.batch_insert_msg_distinct_text(data_insert_list))
            print(db.batch_update_message(max_key))
            print("***************************** Filter Batch Insert END  ******************************")

    def chunks(l, n):
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]


drop_duplicates = Dropduplicates()

# if __name__ == '__main__':
# dropduplicates= Dropduplicates()
# drop_duplicates.drop_dulicates()

if __name__ == '__main__':
    msg = '合众票据 \n合众票据'
    group_name ='票据测试'
    sendTool = SendTool()
    sendTool.send_messages(group_name,msg)

