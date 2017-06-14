# coding=utf8

from sqlalchemy.sql import and_
from models import IpPool, DBSession


class DBHelper(object):

    def __init__(self):
        self.session = DBSession()
        # keep a session open
        self.session.expire_on_commit = False

    def insertDb(self, ip_list):
        print '[+]', 'insert db'
        save_pool = []
        # print ip_list
        for ip in ip_list:
            old_ip = self.session.query(IpPool).filter(and_(IpPool.ip == ip['ip'], IpPool.port == ip['port'])).first()
            if old_ip:
                continue
            if len(save_pool) > 100:
                self.session.add_all(save_pool)
                self.session.commit()
                print '[+] ', "session commit"
                save_pool = []
            else:
                ip_obj = IpPool(ip=ip['ip'], port=ip['port'], location=ip['location'], iptype=ip['iptype'], protocol=ip['protocol'])
                save_pool.append(ip_obj)
        if save_pool:
            self.session.add_all(save_pool)
            self.session.commit()
        # self.session.close()

    def deleteIp(self, delip):
        self.session.delete(delip)
        self.session.commit()
        # self.session.close()

    def getIds(self):
        ids = self.session.query(IpPool.id).all()
        self.session.commit()
        # self.session.close()
        return ids

    def getIp(self, id):
        ip = self.session.query(IpPool).filter(IpPool.id == id).first()
        self.session.commit()
        # self.session.close()
        return ip

    def __del__(self):
        self.session.close()

# if __name__ == '__main__':
#     db = DBHelper()
#     # db.insertDb([])
#     # db.deleteDb(['127.0.0.1', ])
