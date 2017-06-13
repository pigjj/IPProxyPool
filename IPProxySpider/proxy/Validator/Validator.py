# coding=utf8

import sys
import time
import chardet
import requests
from lxml import etree

from gevent import monkey
monkey.patch_all()
import gevent

sys.path.append('..')
from config import config
from IPSpider.tools import tools
from DBHelper.DBHelper import DBHelper
from Logger.Logger import logging


class Validator(object):

    def __init__(self):
        self.url = config.TEST_IP
        self.cookie = 'pgv_pvi=1605740544; ASPSESSIONIDSACCBACQ=ENJJEHFCFLAPCEBDHDKLODDJ; pgv_si=s8669043712'
        self.host = '1212.ip138.com'

    def ipCheck(self):
        while(True):
            db = DBHelper()
            ids = db.getIds()
            db.destory()
            spawns = []
            if ids:
                # print len(ids)
                logging.info("[+] there are {0} ip in database".format(len(ids)))
                for id in ids:
                    db = DBHelper()
                    ip = db.getIp(id[0])
                    # print ip
                    spawns.append(gevent.spawn(self.inspectIp, ip, db))
                    if len(spawns) >= 500:
                        gevent.joinall(spawns)
                        spawns = []
                gevent.joinall(spawns)
            else:
                logging.info("[+] no ip in database")
                # print 'no ip in database'
            logging.info("[+] sleep now")
            # print 'sleep now'
            time.sleep(config.CHECK_INTERVAL)

    def inspectIp(self, ip, db):
        headers = tools.getHeader(self.host, self.cookie)
        if not ip:
            db.deleteIp(ip)
        else:
            if "HTTP" in ip.protocol and "HTTPS" in ip.protocol:
                proxies = {"http": "http://%s:%s" % (ip.ip, ip.port), "https": "http://%s:%s" % (ip.ip, ip.port)}
            elif not ip.protocol or ip.protocol == "HTTP":
                proxies = {"http": "http://%s:%s" % (ip.ip, ip.port)}
            elif ip.protocol == "HTTPS":
                proxies = {"https": "https://%s:%s" % (ip.ip, ip.port)}
            else:
                pass
            # print proxies
            logging.info("[+] proxies is {0}".format(proxies))
            try:
                # proxies = {"http": "http://%s:%s" % (ip.ip, ip.port), "https": "http://%s:%s" % (ip.ip, ip.port)}
                result = requests.get(url=self.url, headers=headers, timeout=config.TIMEOUT, proxies=proxies)
                result.encoding = chardet.detect(result.content)['encoding']
                # print result.text
                if not result.ok:
                    logging.info("[-] result is not ok")
                    # print '[-] ', 'result is not ok'
                    raise Exception('ConnectionError', 'There is an error')
                else:
                    logging.info("[+] result is ok")
                    # print '[+] ', 'result is ok'
                    root = etree.HTML(result.text)
                    proxys = root.xpath('//center/text()')
                    # print proxys
                    reip = proxys[0].split('[')[-1].split(']')[0]
                    # print reip
                    localip = tools.getOutIP()
                    logging.info("[+] remote ip: {0},\tlocalip: {1}".format(reip, localip))
                    # print localip
                    if localip == reip:
                        db.deleteIp(ip)

            except Exception, e:
                # print e
                logging.info("[-] Drop ip: {0}, port: {1}".format(ip.ip, ip.port))
                # print "Drop ip: {0}, port: {1}".format(ip.ip, ip.port)
                db.deleteIp(ip)

        db.destory()
inspector = Validator()

# if __name__ == "__main__":
#     import random
#     from DBHelper.models import IpPool
#     from DBHelper.DBHelper import DBHelper
#     db = DBHelper()
#     ids = db.session.query(IpPool.id).all()
#     print len(ids)
#     id = random.choice(ids)[0]
#     # print id
#     ip = db.getIp(id)
#     print ip.ip, ip.port, ip.protocol
#     inspector = Inspector().inspectIp(ip, db)
