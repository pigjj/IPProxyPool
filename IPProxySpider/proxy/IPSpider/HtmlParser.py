# coding=utf8

import re
import base64

from lxml import etree

from config import config


class HtmlParser(object):

    def __init__(self):
        self.ips = []

    def parse(self, response, parser):
        return self.XpathPraser(response, parser)

    def XpathPraser(self, response, parser):
        print '[+] ', 'XpathPraser'
        iplist = []
        root = etree.HTML(response)
        proxys = root.xpath(parser['pattern'])
        # proxys = root.xpath("//div[@id='main']")  # /div/div[1]/table/tr[position()>1]")
        # print proxys
        for proxy in proxys:
            try:
                ip = proxy.xpath(parser['position']['ip'])[0].text.replace(' ', '')
                # print ip
                port = proxy.xpath(parser['position']['port'])[0].text.replace(' ', '')
                # print port
                location = proxy.xpath(parser['position']['location'])[0].text.replace(' ', '')
                # print location
                iptype = proxy.xpath(parser['position']['type'])[0].text.replace(' ', '')
                # print iptype
                if parser['position']['protocol']:
                    protocol = proxy.xpath(parser['position']['protocol'])[0].text.replace(' ', '')
                else:
                    protocol = ''
                # print protocol
                print "###", ip, ':', port, location, iptype, protocol, "###"
                proxy = {
                    "ip": ip,
                    "port": port,
                    "location": location,
                    "iptype": iptype,
                    "protocol": protocol,
                }
            except Exception as e:
                print e
                continue
            iplist.append(proxy)
        return iplist


html_parser = HtmlParser()
