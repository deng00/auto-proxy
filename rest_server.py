#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Danny0'

import json
import time
import web
from abc import ABCMeta, abstractmethod
from util.func import *

urls = (
    "/", "Index",
    '/ip', 'Ip',
)


class Api:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.ERROR_CODE = {
            "0": "success",
            "3000": "miss param",
            "3001": "param num can not bigger than 5",
            "4003": "no auth",
            "5000": "ip pool is empty",
            "5001": "request fail",
        }
        self.params = web.input(num="5")
        self.time_start = time.time()

    @abstractmethod
    def GET(self):
        pass

    @staticmethod
    def set_json_response():
        """
        设置响应content-type为json
        :return:
        """
        web.header('content-type', 'application/json;charset=utf-8', unique=True)

    def json(self, errno, data=None):
        """
        发送json格式响应
        :param errno:
        :param data:
        :return:
        """
        data = data if data else []
        self.set_json_response()
        res = {
            "errno": errno,
            "message": self.ERROR_CODE[str(errno)],
            "data": data,
            "time": round(time.time() - self.time_start, 2)
        }
        return json.dumps(res)

    def result(self, data):
        """
        根据查询结果返回json
        :param data:
        """
        if not data:
            return self.json(5001)
        else:
            return self.json(0, data)


class Ip(Api):
    def GET(self):
        # 从redis中拿
        redis_ins = get_redis_ins()
        num = int(self.params.num)
        if num > 5:
            return self.json(3001)
        ips = redis_ins.zrange(REDIS_KEY, 0, num - 1)  # 会包含结束index
        if not ips:
            # 没有可用IP
            return self.json(5000)
        # 增加使用次数
        for ip in ips:
            redis_ins.zincrby(REDIS_KEY, ip)
        return self.result(ips)


class Index(Api):
    def GET(self):
        return "proxy rest api"


if __name__ == "__main__":
    os.environ["PORT"] = "9090" if os.uname()[0] == "Darwin" else "80"
    app = web.application(urls, globals())
    app.run()
