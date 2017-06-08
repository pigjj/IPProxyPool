# coding=utf8

import sys
# from threading import Thread
from gevent import monkey
monkey.patch_all()

import gevent

from DBHelper.DBHelper import DBHelper
from Validator.Validator import inspector

if __name__ == "__main__":
    db = DBHelper()
    ids = db.getIds()
    db.destory()
    spawns = []
    if ids:
        print len(ids)
        for id in ids:
            print id
            db = DBHelper()
            ip = db.getIp(id[0])
            print ip.protocol
            spawns.append(gevent.spawn(inspector.inspectIp, ip, db))
            # break
            if len(spawns) >= 500:
                gevent.joinall(spawns)
                spawns = []
        gevent.joinall(spawns)
    else:
        print 'no ip in database'
