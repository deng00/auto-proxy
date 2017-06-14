#! /usr/bin/env python
# coding=utf-8
from __future__ import print_function
import logging
import time
from termcolor import colored


class Logger:
    def __init__(self, path="log.txt"):
        log_instance = logging.getLogger('live_logger')
        log_instance.setLevel(logging.DEBUG)
        ch = logging.FileHandler(path, 'w')
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        log_instance.addHandler(ch)
        self.logger = log_instance

    def pr(self, message, level):
        color_map = {
            "debug": "white",
            "info": "green",
            "warning": "magenta",
            "error": "red",
            "critical": "red"
        }
        eval("self.logger." + level + "(message)")
        message = "[" + time.strftime('%Y-%m-%d %H:%M:%S') + "] " + "[" + level + "] " + message
        print(colored(message, color_map[level]))

    def debug(self, message):
        self.pr(message, "debug")

    def info(self, message):
        self.pr(message, "info")

    def warning(self, message):
        self.pr(message, "warning")

    warn = warning

    def error(self, message):
        self.pr(message, "error")

    def critical(self, message):
        self.pr(message, "critical")


if __name__ == '__main__':
    log = Logger('log.txt')
    log.debug('一个debug信息')
    log.info('一个info信息')
    log.warn('一个warning信息')
    log.error('一个error信息')
