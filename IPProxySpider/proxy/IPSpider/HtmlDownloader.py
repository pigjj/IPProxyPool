# coding=utf8

import random
import chardet
import requests

from tools import tools
from config import config
from Logger.Logger import logging


class HtmlDownloader(object):

    def __init__(self):
        pass

    @staticmethod
    def download(url, parser, ip):
        headers = tools.getHeader(parser.get('Host', ''), parser.get('Cookie', ''))
        # print headers
        logging.info("[+] Download url: {0}".format(url))
        # print '[+] Download url: %s' % url
        try:
            if ip:
                proxies = {"http": "http://%s:%s" % (ip.get('ip'), ip.get('port')), "https": "http://%s:%s" % (ip.get('ip'), ip.get('port'))}
                result = requests.get(url=url, headers=headers, timeout=config.TIMEOUT, proxies=proxies)
            else:
                result = requests.get(url=url, headers=headers, timeout=config.TIMEOUT)
            # if len(result) < 100:
            # print "#" * 20, result, "#" * 20
            result.encoding = chardet.detect(result.content)['encoding']
            if not result.ok or len(result.content) < 500:
                logging.info("[-] result is not ok")
                # print '[-] ', 'result is not ok'
                raise Exception('ConnectionError', 'There is an error')
            else:
                logging.info("[+] result is ok")
                return result.text
        except Exception, e:
            logging.info("[-] Download exception: {0}".format(e))
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
                        logging.info("[-] Exception logic result is not ok")
                        # print '[-] ', 'Exception logic result is not ok'
                        raise Exception('ConnectionError', 'Exception logic result is not ok')
                    else:
                        logging.info("[+] Exception logic result is ok")
                        # print '[+] ', 'Exception logic result is ok'
                        return result.text
                except Exception, e:
                    logging.info("[-] Exception logic download exception: {0}".format(e))
                    # print '[-] ', 'Exception logic download exception: %s' % e
                    count += 1
        return

html_downloader = HtmlDownloader()
