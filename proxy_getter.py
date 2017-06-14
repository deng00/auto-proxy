#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests

from util.func import *

__author__ = 'Danny0'


class ProxyGetter():
    proxy_source = [
        "tudoudaili",
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

    def from_tudoudaili(self, num):
        self.log_ins.debug("start get new ip from tudoudaili")
        api = "http://tvp.daxiangdaili.com/ip/"
        param = {
            "tid": ORDER_ID_TUDOU,
            "num": num,
            "area": "",
            "foreign": "all",
            "ports": "",
            "exclude_ports": "",
            "protocol": "",
            "filter": "on"
        }
        res = requests.get(api, param)
        if res.text[0:5] == "ERROR":
            return []
        ips = res.text.split("\r\n")
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
    print(getter.get_ip("tudoudaili", 2))
