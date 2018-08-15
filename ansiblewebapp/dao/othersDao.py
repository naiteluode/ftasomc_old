# coding:utf-8
from django.db import connection
from AnsibleWebApp.dto.Project import Project
from AnsibleWebApp.dto.Inventory import Inventory
from AnsibleWebApp.dto.Item import Item
from AnsibleWebApp.dto.Mission import Mission
import json
import threading


class OthersDao:
    # 初始化函数
    def __init__(self):
        self.connection = None
        self.cursor = None

    def init_cursor(self):
        self.connection = connection
        self.cursor = connection.cursor()

    # 获取工程列表
    def get_project_list(self):
        sql = "select distinct project from groups"
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
                p = Project(obj[0].encode('utf8'))
                result.append(p.convert2dict())
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        # 函数返回值
        return json.dumps(result)

    # 根据主机组id获取项目
    def get_items_by_groups_id(self, _id):
        lock = threading.Lock()
        try:
            lock.acquire(True)
            self.init_cursor()
            # 执行语句
            self.cursor.execute("""select i.id,i.name
            from groups_items gi, groups g, items i
            where gi.grp_id=g.id and gi.itm_id=i.id and g.id=%s""" % _id)
            # 创建一个用于存放对象集的集合
            result = []
            # 迭代每一个查到的信息存入数据传输对象中并集中于list
            for obj in self.cursor.fetchall():
                # 数据传输对象
                i = Item(
                        obj[0],
                        obj[1].encode('utf8')
                )
                result.append(i.convert2dict())
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        # 函数返回值
        return json.dumps(result)

    # 根据主机组id获取项目
    def get_items_list(self):
        lock = threading.Lock()
        try:
            lock.acquire(True)
            self.init_cursor()
            # 执行语句
            self.cursor.execute("select i.id,i.name from items i")
            # 创建一个用于存放对象集的集合
            result = []
            # 迭代每一个查到的信息存入数据传输对象中并集中于list
            for obj in self.cursor.fetchall():
                # 数据传输对象
                i = Item(
                        obj[0],
                        obj[1].encode('utf8')
                )
                result.append(i.convert2dict())
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        # 函数返回值
        return json.dumps(result)

    # 获取机器详细信息列表
    def get_inventory_list(self):
        lock = threading.Lock()
        try:
            lock.acquire(True)
            # 要执行的SQL语句
            sql = """
                select i.id,s.id as 'sid',s.ip,s.hostname,s.type,s.os,g.name as 'group'
                from groups g,groups_servers i,servers s
                where g.id=i.grp_id and s.id=i.ser_id"""
            self.init_cursor()
            # 执行语句
            self.cursor.execute(sql)
            # 创建一个用于存放对象集的集合
            result = []
            # 迭代每一个查到的信息存入数据传输对象中并集中于list
            for obj in self.cursor.fetchall():
                # 数据传输对象
                inv = Inventory(
                        obj[0],
                        obj[1],
                        obj[2].encode('utf8'),
                        obj[3].encode('utf8'),
                        obj[4].encode('utf8'),
                        obj[5].encode('utf8'),
                        obj[6].encode('utf8')
                )
                result.append(inv.convert2dict())
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        # 函数返回值
        return json.dumps(result)

    # 添加资产关系
    def inventory_add(self, grp_id, ser_id):
        lock = threading.Lock()
        try:
            lock.acquire(True)
            # 要执行的SQL语句
            sql = """insert into groups_servers(grp_id,ser_id) values('%s','%s')""" % (grp_id, ser_id)
            self.init_cursor()
            # 执行语句
            self.cursor.execute(sql)
            rowcount = self.cursor.rowcount
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        result = "ok" if rowcount != 0 else "error"
        # 函数返回值
        return json.dumps(result)

    # 删除关系
    def inventory_delete(self, _id):
        # 要执行的SQL语句
        sql = "delete from groups_servers where id='%s'" % _id
        lock = threading.Lock()
        try:
            lock.acquire(True)
            self.init_cursor()
            # 执行语句
            self.cursor.execute(sql)
            rowcount = self.cursor.rowcount
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        result = "ok" if rowcount != 0 else "error"
        return result

    # 通过工程名获取所有任务
    def get_all_mission_by_project(self, project):
        # 要执行的SQL语句
        sql = """
            select g.name as 'group',s.ip,i.name as 'item'
            from groups_items gi, groups g, items i,servers s,groups_servers gs
            where gi.grp_id=g.id and gi.itm_id=i.id
            and gs.grp_id=g.id and gs.ser_id=s.id and g.name like '"""+project+"""%'"""
        lock = threading.Lock()
        try:
            lock.acquire(True)
            self.init_cursor()
            # 执行语句
            self.cursor.execute(sql)
            # 创建一个用于存放对象集的集合
            result = []
            # 迭代每一个查到的信息存入数据传输对象中并集中于list
            for obj in self.cursor.fetchall():
                # 数据传输对象
                m = Mission(
                        obj[0].encode('utf8'),
                        obj[1].encode('utf8'),
                        obj[2].encode('utf8')
                )
                result.append(m.convert2dict())
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        # 函数返回值
        return json.dumps(result)
