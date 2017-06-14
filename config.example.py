#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Danny0'
import os

IS_DEBUG = False if os.uname()[0] != "Darwin" else True

# min ip num
MIN_IP_NUM = 100
NEW_IP_NUM = 2 if IS_DEBUG else 100
CHECK_THREAD_NUM = 5
CHECK_TIMEOUT = 3

# redis
REDIS_HOST = "YOUR_ONLINE_REDIS_IP" if not IS_DEBUG else "127.0.0.1"
REDIS_PORT = 6379
REDIS_PASS = "YOUR_REDIS_PASS"
REDIS_DB = 6
REDIS_KEY = "proxy_ip"

# http://www.tudoudaili.com 订单号
ORDER_ID_TUDOU = 0
# http://www.kuaidaili.com/usercenter/
ORDER_ID_KUAIDAILI = 0

DEFAULT_PROXY = "kuaidaili"

PROXY_SERVER_MAX_CONNECTION = 1000
