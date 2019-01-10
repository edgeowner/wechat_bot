#!/usr/bin/env python
# -*- coding: utf-8 -*-

import oss2


class OSS2(object):
    def __init__(self, access_key_id, access_key_secret):
        bucket_name = 'draftelf'
        endpoint = 'https://oss-cn-hangzhou.aliyuncs.com'
        self.bucket = oss2.Bucket(
            oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)

    def upload(self, key, path):
        self.bucket.put_object_from_file(key, path)


if __name__ == '__main__':
    access_key_id = ''
    access_key_secret = ''
    oss2 = OSS2(access_key_id, access_key_secret)
    oss2.upload('example.jpg', 'example.jpg')
