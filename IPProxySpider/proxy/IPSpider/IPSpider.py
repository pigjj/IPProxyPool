# coding=utf8

import sys
import time
from gevent import monkey
monkey.patch_all()

import random
import gevent
from tools import tools
from gevent.pool import Pool
from HtmlParser import html_parser
from HtmlDownloader import html_downloader


sys.path.append('..')

from config import config
from DBHelper.DBHelper import DBHelper
from Logger.Logger import logging

class IPSpider(object):

    def __init__(self, queue):
        # ip处理队列
        self.queue = queue
        # 外网ip
        self.outip = tools.getOutIP()
        # ?
        # self.db_ip_num = db_ip_num

    def run(self):
        while(True):
            logging.info("[+] Spider start runing")
            # print '[+] ', 'Spider start runing'
            spawns = []
            # 数据库中查出ip的列表
            # select * from ip_table
            db = DBHelper()
            ids = db.getIds()
            # self.db_ip_num.value = len(ids)
            # print selected_id
            # exit()
            logging.info("[+] db save ip: {0}".format(len(ids)))
            # print '[+] ', 'db save ip:%d' % len(ids)
            if len(ids) < config.MINNUM:
                logging.info("[+] now ip num < MINNUM start spider")
                # print '[+] ', 'now ip num < MINNUM start spider...'
                for parser in config.parser_list:
                    if ids:
                        selected_id = random.choice(ids)
                        ip = db.getIp(selected_id)
                    else:
                        ip = ''
                    spawns.append(gevent.spawn(self.spider, parser, ip))
                    if len(spawns) >= config.MAX_DOWNLOAD_CONCURRENT:
                        gevent.joinall(spawns)
                        spawns = []
                gevent.joinall(spawns)
            else:
                logging.info("[+] now ip num meet the requirement,wait check again...'")
                # print '[+] ', 'now ip num meet the requirement,wait check again...', '#'

            logging.info("[+] sleep now")
            # print "sleep now"
            time.sleep(config.CHECK_INTERVAL)

    def spider(self, parser, ip):
        for url in parser.get('urls'):
            response = html_downloader.download(url, parser, ip)
            # print response
            if response:
                print '[+] ', 'parse Html'
                iplist = html_parser.parse(response, parser)
                print '[+] ', 'ip list %d' % len(iplist)
                if iplist:
                    DBHelper().insertDb(iplist)
