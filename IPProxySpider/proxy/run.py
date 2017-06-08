# coding=utf8

# from tools import tools
# from WebServer.WebServer import server

# if __name__ == '__main__':
    # outip = tools.getOutIP()
    # server.startServer()

from multiprocessing import Queue, Process, Value

from IPSpider.IPSpider import IPSpider


if __name__ == "__main__":
    DB_PROXY_NUM = Value('i', 0)

    q1 = Queue()
    p1 = Process(target=IPSpider(q1, DB_PROXY_NUM).run)

    p1.start()

