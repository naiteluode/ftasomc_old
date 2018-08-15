# coding:utf-8
from django.db import connection
from AnsibleWebApp.dto.Item import Item
from AnsibleWebApp.dto.GroupItem import GroupItem
import json
import threading


class ItemsDao:
    # 初始化函数
    def __init__(self):
        self.connection = None
        self.cursor = None

    def init_cursor(self):
        self.connection = connection
        self.cursor = connection.cursor()

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

    # 获取主机组项目列表
    def get_group_items_list(self):
        lock = threading.Lock()
        try:
            lock.acquire(True)
            self.init_cursor()
            # 执行语句
            self.cursor.execute("""select gi.id,g.name as 'group',i.name as 'item'
            from items i,groups g,groups_items gi
            where gi.grp_id=g.id and gi.itm_id=i.id""")
            # 创建一个用于存放对象集的集合
            result = []
            # 迭代每一个查到的信息存入数据传输对象中并集中于list
            for obj in self.cursor.fetchall():
                # 数据传输对象
                gi = GroupItem(
                        obj[0],
                        obj[1].encode('utf8'),
                        obj[2].encode('utf8')
                )
                result.append(gi.convert2dict())
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        # 函数返回值
        return json.dumps(result)

    # 添加主机组项目
    def group_items_add(self, group, item):
        lock = threading.Lock()
        try:
            lock.acquire(True)
            # 要执行的SQL语句
            sql = "insert into groups_items(grp_id,itm_id) values ('%s','%s')" % (group, item)
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

    # 删除主机组项目
    def group_items_delete(self, _id):
        lock = threading.Lock()
        try:
            lock.acquire(True)
            # 要执行的SQL语句
            sql = "delete from groups_items where id=%s" % _id
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

    # 添加项目
    def items_add(self, name):
        lock = threading.Lock()
        try:
            lock.acquire(True)
            # 要执行的SQL语句
            sql = "insert into items(name) values ('%s')" % name
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

    # 删除项目
    def items_delete(self, _id):
        lock = threading.Lock()
        try:
            lock.acquire(True)
            # 要执行的SQL语句
            sql = "delete from items where id=%s" % _id
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
