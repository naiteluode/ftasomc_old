# coding:utf-8
from django.db import connection
from AnsibleWebApp.dto.Server import Server
import json
import threading


class ServersDao:
    # 初始化函数
    def __init__(self):
        self.connection = None
        self.cursor = None

    def init_cursor(self):
        self.connection = connection
        self.cursor = connection.cursor()

    # 获取主机列表
    def get_server_list(self):
        # 要执行的SQL语句
        sql = "select id, ip, hostname, type, os from servers"
        lock = threading.Lock()
        try:
            lock.acquire(True)
            self.init_cursor()
            self.cursor.execute(sql)
            # 创建一个用于存放对象集的集合
            result = []
            # 迭代每一个查到的信息存入数据传输对象中并集中于list
            for obj in self.cursor.fetchall():
                # 数据传输对象
                s = Server(
                        obj[0],
                        obj[1].encode('utf8'),
                        obj[2].encode('utf8'),
                        obj[3].encode('utf8'),
                        obj[4].encode('utf8')
                )
                result.append(s.convert2dict())
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        # 函数返回值
        return json.dumps(result)

    # 根据主机id查询主机信息
    def server_get(self, _id):
        # 要执行的SQL语句
        sql = "select id, ip, hostname, type, os from servers where id = '%s'" % _id
        lock = threading.Lock()
        try:
            lock.acquire(True)
            self.init_cursor()
            self.cursor.execute(sql)
            # 迭代每一个查到的信息存入数据传输对象中并集中于list
            obj = self.cursor.fetchone()
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        # 数据传输对象
        s = Server(
                obj[0],
                obj[1].encode('utf8'),
                obj[2].encode('utf8'),
                obj[3].encode('utf8'),
                obj[4].encode('utf8')
        )
        # result = s.convert2dict()
        result = s
        # 函数返回值
        return result

    # 增加主机
    def server_add(self, _id, ip, hostname, _os, _type):
        # 要执行的SQL语句
        sql = """insert into servers(id, ip, hostname, type, os)
        values ('%s','%s','%s','%s','%s')""" % (_id, ip, hostname, _type, _os)
        lock = threading.Lock()
        try:
            lock.acquire(True)
            self.init_cursor()
            self.cursor.execute(sql)
            rowcount = self.cursor.rowcount
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        result = "ok" if rowcount != 0 else "error"
        return result

    # 修改主机
    def server_modify(self, _id, ip, hostname, _type, _os):
        # 要执行的SQL语句
        sql = """update servers
        set ip='%s',hostname='%s',os='%s',type='%s'
        where id='%s'""" % (ip, hostname, _os, _type, _id)
        lock = threading.Lock()
        try:
            lock.acquire(True)
            self.init_cursor()
            self.cursor.execute(sql)
            rowcount = self.cursor.rowcount
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        result = "ok" if rowcount != 0 else "error"
        return result

    # 删除主机
    def server_delete(self, _id):
        # 要执行的SQL语句
        sql = "delete from servers where id='%s'" % _id
        lock = threading.Lock()
        try:
            lock.acquire(True)
            self.init_cursor()
            self.cursor.execute(sql)
            rowcount = self.cursor.rowcount
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        result = "ok" if rowcount != 0 else "error"
        return result

    # 通过组id查询组内主机ip列表
    def get_server_by_group(self, _id):
        # 要执行的SQL语句
        sql = """select ip from groups_servers gs,servers s, groups g
        where gs.grp_id=g.id and gs.ser_id=s.id and grp_id='%s'""" % _id
        lock = threading.Lock()
        try:
            lock.acquire(True)
            self.init_cursor()
            self.cursor.execute(sql)
            # 创建一个用于存放对象集的集合
            result = []
            # 迭代每一个查到的信息存入数据传输对象中并集中于list
            for obj in self.cursor.fetchall():
                # 数据传输对象
                s = Server(
                        "null",
                        obj[0].encode('utf8'),
                        "null",
                        "null",
                        "null"
                )
                result.append(s.convert2dict())
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        return json.dumps(result)
