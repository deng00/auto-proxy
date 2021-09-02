#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests

from util.func import *

__author__ = 'Danny0'


class ProxyGetter():
    proxy_source = [
        "kuaidaili"
    ]

    def __init__(self):
        self.log_ins = get_logger()
        pass

    def get_ip(self, source, num):
        if source not in self.proxy_source:
            return False
        ips = eval("self.from_" + source + "(num)")
        self.log_ins.debug("got new ip num : " + str(len(ips)))
        return ips

    def from_kuaidaili(self, num):
        """
        获取代理ip列表
        """
        self.log_ins.debug("start get new ip from kuaidaili")
        api = "http://dps.kuaidaili.com/api/getdps/"
        param = {
            "orderid": ORDER_ID_KUAIDAILI,
            "num": NEW_IP_NUM,
            "ut": 1,
            "sep": 1,
        }
        res = requests.get(api, params=param, headers={
            "Accept-Encoding": "gzip"
        })
        if res.text[0:5] == "ERROR":
            return []
        ips = res.text.split("\r\n")
        return ips


if __name__ == '__main__':
    getter = ProxyGetter()
    print(getter.get_ip("kuaidaili", 2))
