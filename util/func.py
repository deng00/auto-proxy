#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Danny0'
import redis
from config import *
from logger import Logger

redis_instance = None
log_instance = None


def md5(string):
    """
    md5加密
    :param string:
    :return:
    """
    import hashlib
    m = hashlib.md5()
    m.update(string)
    return m.hexdigest()


def get_redis_ins():
    global redis_instance
    if redis_instance:
        return redis_instance
    redis_instance = redis.Redis(REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_PASS)
    return redis_instance


def get_logger():
    global log_instance
    if log_instance:
        return log_instance
    log_instance = Logger('log.txt')

    return log_instance


def get_local_ip():
    """
    获取本机IP
    :return:
    """
    import socket
    my_name = socket.getfqdn(socket.gethostname())
    return socket.gethostbyname(my_name)
