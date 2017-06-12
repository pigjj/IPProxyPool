# coding=utf8

# from tools import tools
# from WebServer.WebServer import server

# if __name__ == '__main__':
    # outip = tools.getOutIP()
    # server.startServer()
import time

from multiprocessing import Queue, Process

from IPSpider.IPSpider import IPSpider
from DBHelper.DBHelper import DBHelper
from Validator.Validator import inspector


if __name__ == "__main__":
    # DB_PROXY_NUM = Value('i', 0)
    db = DBHelper()
    ids = db.getIds()
    db.destory()

    q1 = Queue()
    p1 = Process(target=IPSpider(q1, ).run)

    p1.start()
    try:
        p2 = Process(target=inspector.ipCheck(ids, db).run)
        p2.start()
    except:
        print "no ip in database"
        time.sleep(60 * 60)
        p2 = Process(target=inspector.ipCheck(ids, db).run)
        p2.start()
