# coding=utf8

import json
import random
import requests

from config import config

from fake_useragent import UserAgent


class Tools(object):

    def getOutIP(self):
        try:
            result = requests.get(
                url=config.TEST_IP, headers=self.getHeader(), timeout=config.TIMEOUT)
            ip = result.text[result.text.find("[") + 1: result.text.find("]")]
        except Exception, e:
            # print e, "#" * 20
            return ''
        return ip

    def getHeader(self, host='', cookie=''):
        # 伪造的useragent
        ua = UserAgent()
        # 随机获取伪造的useagent
        if host:
            return {
                'User-Agent': ua.random,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
                'Connection': 'keep-alive',
                'Accept-Encoding': 'gzip, deflate, sdch',
                'Upgrade-Insecure-Requests': '1',
                'Host': host,
                'Cookie': cookie
            }
        elif not host and not cookie:
            return {
                'User-Agent': ua.random,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
                'Connection': 'keep-alive',
                'Accept-Encoding': 'gzip, deflate, sdch',
                'Upgrade-Insecure-Requests': '1',
            }
        else:
            return {
                'User-Agent': ua.random,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
                'Connection': 'keep-alive',
                'Accept-Encoding': 'gzip, deflate, sdch',
                'Upgrade-Insecure-Requests': '1',
                'Cookie': cookie
            }


tools = Tools()
