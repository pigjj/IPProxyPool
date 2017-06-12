# coding=utf8


import os
import random


class Config(object):

    def __init__(self):
        self.TEST_IP = "http://1212.ip138.com/ic.asp"
        self.TIMEOUT = 10
        self.PORT = 8001
        self.MINNUM = 500  # 有效ip值小于MINNUM时开启爬虫
        self.RETRY_TIME = 3  # 重试次数
        self.CHECK_INTERVAL = 24 * 60 * 60  # 每天,检查一次ip
        self.MAX_DOWNLOAD_CONCURRENT = 3  # 从免费下载代理网站下载的最大并发
        self.MAX_CONCURRENT_PER_PROCESS = 30  # 每个进程最大的并发数量
        self.parser_list = [
            {
                "urls": ["http://www.66ip.cn/%s.html" % n for n in ["index"] + list(range(2, 899))],
                # "urls": ["http://www.66ip.cn/index.html"],
                "type": "xpath",
                "pattern": "//*[@id='main']/div/div[1]/table/tr[position()>1]",
                "position": {"ip": "./td[1]", "port": "./td[2]", "location": "./td[3]", "type": "./td[4]", "protocol": ""},
                "Host": "www.66ip.cn",
                "Cookie": "__cfduid=d6c82a17908633a521f00045d8bff60fb1495723582; UM_distinctid=15c401310fa4e8-0662cb5af41e81-30637509-13c680-15c401310fb408; cf_clearance=4db0a2643299db834f8890ff2dcfd7fc5c34cead-1496152039-3600; CNZZDATA1253901093=298321565-1495722021-%7C1496151425; Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1495723610,1496152048; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1496152708"
            },
            {
                "urls": ["http://www.66ip.cn/areaindex_%s/%s.html" % (m, n) for m in range(1, 35) for n in range(1, 10)],
                # "urls": ["http://www.66ip.cn/areaindex_%s/%s.html" % (m, n) for m in range(1, 2) for n in range(1, 2)],
                "type": "xpath",
                "pattern": "//*[@id='main']/div/div/div/div[2]/div/table/tr[position()>1]",
                "position": {"ip": "./td[1]", "port": "./td[2]", "location": "./td[3]", "type": "./td[4]", "protocol": ""},
                "Host": "www.66ip.cn",
                "Cookie": "__cfduid=d6c82a17908633a521f00045d8bff60fb1495723582; UM_distinctid=15c401310fa4e8-0662cb5af41e81-30637509-13c680-15c401310fb408; cf_clearance=4db0a2643299db834f8890ff2dcfd7fc5c34cead-1496152039-3600; CNZZDATA1253901093=298321565-1495722021-%7C1496151425; Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1495723610,1496152048; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1496152708"
            },
            {
                'urls': ['http://www.mimiip.com/gngao/%s' % n for n in range(1, 683)],
                # 'urls': ['http://www.mimiip.com/gngao/%s' % n for n in range(1, 2)],
                'type': 'xpath',
                'pattern': ".//table[@class='list']/tr",
                'position': {'ip': './td[1]', 'port': './td[2]', "location": "./td[3]/a[last()]", 'type': './td[4]', 'protocol': './td[5]'},
                "Cookie": "UM_distinctid=15c40109d1c0-0db52417db9645-30637509-13c680-15c40109d1d11b; _ip84_session=b1Q1VWg5RmJ3aWpaUDJRTENYbnhxRWFOY0NFWlBrRGpheUlTQkY0V0lBSFFLZS9sT3poL2ZyaitRSlkvM2JrSzJoU2drYXpyWUlUcTJyVmRTby9jYTliU0hpbVdlYmt0YXp5aUtVVldPVmlUcFBJL3ZIcm40Q0VNOC9kb3p3V2tJazBZV001MVdSZTZLdnB5Wjc3Uk1BPT0tLTI0UVROUHVvMEFOY0RTK1pyMVJGUXc9PQ%3D%3D--c541ab9396953ad6e3c6faf05595da206fac1401; CNZZDATA1258159534=1832115569-1495720496-%7C1496326884"
            },
            {
                # 'urls': ['http://www.kuaidaili.com/proxylist/%s/' % n for n in range(1, 11)],
                'urls': ['http://www.kuaidaili.com/proxylist/%s/' % n for n in range(1, 2)],
                'type': 'xpath',
                'pattern': ".//*[@id='index_free_list']/table/tbody/tr[position()>0]",
                'position': {'ip': './td[1]', 'port': './td[2]', "location": "./td[6]", 'type': './td[3]', 'protocol': './td[4]'},
                "Host": "www.kuaidaili.com",
                "Cookie": "channelid=0; sid=1496329395448162; _ga=GA1.2.282154072.1496329375; _gid=GA1.2.463820057.1496330148; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1496329375; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1496330148",
            },
            {
                'urls': ['http://www.kuaidaili.com/free/%s/%s/' % (m, n) for m in ['inha', 'intr', 'outha', 'outtr'] for n in range(1, 1661)],
                # 'urls': ['http://www.kuaidaili.com/free/%s/%s/' % (m, n) for m in ['inha', 'intr', 'outha', 'outtr'] for n in range(1, 10)],
                'type': 'xpath',
                'pattern': ".//*[@id='list']/table/tbody/tr[position()>0]",
                'position': {'ip': './td[1]', 'port': './td[2]', "location": "./td[6]", 'type': './td[3]', 'protocol': './td[4]'},
                'Host': "www.kuaidaili.com",
                "Cookie": "_gat=1; channelid=0; sid=1496329395448162; _ga=GA1.2.282154072.1496329375; _gid=GA1.2.1936394886.1496330130; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1496329375; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1496330130",
            },
            {
                'urls': ['http://www.ip181.com/daili/%s.html' % n for n in range(1, 1134)],
                # 'urls': ['http://www.ip181.com/daili/%s.html' % n for n in range(1, 11)],
                'type': 'xpath',
                'pattern': ".//div[@class='row']/div[3]/table/tbody/tr[position()>1]",
                'position': {'ip': './td[1]', 'port': './td[2]', 'type': './td[3]', 'protocol': './td[4]'},
                "Host": "www.ip181.com",
                "Cookie": "ASPSESSIONIDASRAAQRB=FEOHDHBAIFOMDNBDCINDDIPG; a2837_pages=3; a2837_times=1",
            },

        ]


config = Config()
