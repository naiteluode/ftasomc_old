# coding:utf-8
from AnsibleWebApp.dto.ItemCount import ItemCount
from django.db import connection
import json
import threading
import uuid


class UtilsDao:
    # 初始化函数
    def __init__(self):
        self.connection = None
        self.cursor = None

    def init_cursor(self):
        self.connection = connection
        self.cursor = connection.cursor()

    # 查询表内数据总数
    def get_total(self, table):
        sql = "select count(id) as 'total' from %s" % table
        # 执行语句
        lock = threading.Lock()
        try:
            lock.acquire(True)
            self.init_cursor()
            self.cursor.execute(sql)
            count = self.cursor.fetchone()
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        result = count[0]
        # 函数返回值
        return result

    # 查询工程总数
    def get_project_count(self):
        sql = "select count(distinct project) as 'total' from groups"
        # 执行语句
        lock = threading.Lock()
        try:
            lock.acquire(True)
            self.init_cursor()
            self.cursor.execute(sql)
            count = self.cursor.fetchone()
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        result = count[0]
        # 函数返回值
        return result

    # 获取表最大id
    def get_max_table_id(self, table):
        sql = "select seq from sqlite_sequence where name='%s'" % table
        # 执行语句
        lock = threading.Lock()
        try:
            lock.acquire(True)
            self.init_cursor()
            self.cursor.execute(sql)
            count = self.cursor.fetchone()
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        result = count[0]
        # 函数返回值
        return result

    # 验证用户名
    def check_username(self, name):
        # 要执行的SQL语句
        sql = "select * from users u where u.username='%s'" % name
        # 执行语句
        lock = threading.Lock()
        try:
            lock.acquire(True)
            self.init_cursor()
            self.cursor.execute(sql)
            name = self.cursor.fetchone()
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        result = "ok" if name is None else "no"
        # 函数返回值
        return result

    # 验证IP
    def check_ip(self, ip):
        # 要执行的SQL语句
        sql = "select * from servers where ip='%s'" % ip
        # 执行语句
        lock = threading.Lock()
        try:
            lock.acquire(True)
            self.init_cursor()
            self.cursor.execute(sql)
            name = self.cursor.fetchone()
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        result = "ok" if name is None else "no"
        # 函数返回值
        return result

    # 获取所有主机组的项目数
    def get_all_items_count(self):
        # 要执行的SQL语句
        sql = """select name,count(gi.itm_id) as count
        from groups_items gi,groups g
        where gi.grp_id = g.id
        group by name
        order by count,name desc
        """
        # 执行语句
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
                ic = ItemCount(
                        obj[0].encode('utf8'),
                        obj[1]
                )
                result.append(ic.convert2dict())
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        # 函数返回值
        return json.dumps(result)

    # 生成uuid
    def get_uuid(self):
        s_uuid = uuid.uuid1()
        l_uuid = str(s_uuid).split('-')
        s_uuid = ''.join(l_uuid)
        return s_uuid
