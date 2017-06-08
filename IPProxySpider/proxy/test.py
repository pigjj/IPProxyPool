# coding=utf8


from multiprocessing import Queue, Process, Value

from fake_useragent import UserAgent

from IPSpider.IPSpider import IPSpider

parser = {
    'urls': ['http://www.mimiip.com/gngao/1', ],
    'type': 'xpath',
    'pattern': ".//table[@class='list']/tr",
    'position': {'ip': './td[1]', 'port': './td[2]', 'type': '', 'protocol': ''}

}

q1 = Queue()
DB_PROXY_NUM = Value('i', 0)
IPSpider(q1, DB_PROXY_NUM).spider(parser)
