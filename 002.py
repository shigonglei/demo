# coding:utf-8

import requests

resp = requests.get('http://www.baidu.com/')


if resp.status_code ==200:
    print('have access to baidu!\n')
