# coding=utf8

import datetime

from sqlalchemy import Column, String, Integer, DateTime, create_engine

from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

# 创建数据对象的基类
Base = declarative_base()

# engine = create_engine('mysql://root:@localhost:3306/IPPool', echo=True)
engine = create_engine('mysql://root:@localhost:3306/IPPool')
DBSession = sessionmaker(bind=engine, autoflush=True)


def getNow():
    now = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
    return now


class IpPool(Base):
    __tablename__ = 'ip_pool'

    id = Column(Integer, primary_key=True)
    ip = Column(String(15), nullable=False)
    port = Column(String(6), nullable=False)
    iptype = Column(String(20), nullable=True)
    protocol = Column(String(20), nullable=True)
    location = Column(String(200), nullable=True)
    last_check = Column(DateTime, default=getNow())


def __init__db():
    Base.metadata.create_all(engine)


def __drop_db():
    Base.metadata.drop_all(engine)


if __name__ == "__main__":
    print "drop..."
    __drop_db()
    print "init..."
    __init__db()
