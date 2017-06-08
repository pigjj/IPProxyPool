# coding=utf8

import random
import chardet
import requests

from tools import tools
from config import config


class HtmlDownloader(object):

    def __init__(self):
        pass

    @staticmethod
    def download(url, parser, ip):
        headers = tools.getHeader(parser.get('Host', ''), parser.get('Cookie', ''))
        # print headers

        print '[+] Download url: %s' % url
        try:
            if ip:
                proxies = {"http": "http://%s:%s" % (ip.get('ip'), ip.get('port')), "https": "http://%s:%s" % (ip.get('ip'), ip.get('port'))}
                result = requests.get(url=url, headers=headers, timeout=config.TIMEOUT, proxies=proxies)
            else:
                result = requests.get(url=url, headers=headers, timeout=config.TIMEOUT)
            # if len(result) < 100:
            print "#" * 20, result, "#" * 20
            result.encoding = chardet.detect(result.content)['encoding']
            if not result.ok or len(result.content) < 500:
                print '[-] ', 'result is not ok'
                raise Exception('ConnectionError', 'There is an error')
            else:
                print '[+] ', 'result is ok'
                return result.text
        except Exception, e:
            print '[-] ', 'Download exception: %s' % e
            count = 0  # 重试次数
            # select * from ip_table
            proxylist = []  # 查询数据库中的ip
            if not proxylist:
                return None

            while count < config.RETRY_TIME:
                try:
                    proxy = random.choice(proxylist)
                    ip = proxy[0]
                    port = proxy[1]
                    proxies = {"http": "http://%s:%s" %
                               (ip, port), "https": "http://%s:%s" % (ip, port)}
                    result = requests.get(url=url, headers=headers, timeout=config.TIMEOUT, proxies=proxies)
                    result.encoding = chardet.detect(
                        result.content)['encoding']
                    if not result.ok or len(result.content) < 500:
                        print '[-] ', 'Exception logic result is not ok'
                        raise Exception('ConnectionError', 'Exception logic result is not ok')
                    else:
                        print '[+] ', 'Exception logic result is ok'
                        return result.text
                except Exception, e:
                    print '[-] ', 'Exception logic download exception: %s' % e
                    count += 1
        return

html_downloader = HtmlDownloader()
