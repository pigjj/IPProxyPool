# coding=utf8

import re
import base64

from lxml import etree

from config import config
from Logger.Logger import logging

class HtmlParser(object):

    def __init__(self):
        self.ips = []

    def parse(self, response, parser):
        return self.XpathPraser(response, parser)

    def XpathPraser(self, response, parser):
        iplist = []
        root = etree.HTML(response)
        proxys = root.xpath(parser['pattern'])
        for proxy in proxys:
            try:
                ip = proxy.xpath(parser['position']['ip'])[0].text.replace(' ', '')
                port = proxy.xpath(parser['position']['port'])[0].text.replace(' ', '')
                location = proxy.xpath(parser['position']['location'])[0].text.replace(' ', '')
                iptype = proxy.xpath(parser['position']['type'])[0].text.replace(' ', '')
                if parser['position']['protocol']:
                    protocol = proxy.xpath(parser['position']['protocol'])[0].text.replace(' ', '')
                else:
                    protocol = ''

                logging.info("{0}:{1}\t{2}\t{3}\t{4}".format(ip, port, location, iptype, protocol))
                # print "###", ip, ':', port, location, iptype, "###"
                proxy = {
                    "ip": ip,
                    "port": port,
                    "location": location,
                    "iptype": iptype,
                    "protocol": protocol,
                }
            except Exception as e:
                logging.info("Exception: {0}".format(e))
                # print e
                continue
            iplist.append(proxy)
        return iplist


html_parser = HtmlParser()
