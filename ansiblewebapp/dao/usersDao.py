# coding:utf-8
from django.db import connection
from AnsibleWebApp.dto.User import User
import json
import threading


class UsersDao:
    # 初始化函数
    def __init__(self):
        self.connection = None
        self.cursor = None

    def init_cursor(self):
        self.connection = connection
        self.cursor = connection.cursor()

    # 获取用户列表
    def get_user_list(self):
        # 要执行的SQL语句
        sql = "select * from users u"
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
                u = User(
                        obj[0],
                        obj[1].encode('utf8'),
                        obj[2].encode('utf8'),
                        obj[3].encode('utf8'),
                        obj[4].encode('utf8')
                )
                result.append(u.convert2dict())
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        # 函数返回值
        return json.dumps(result)

    # 增加用户
    def user_add(self, nickname, username, password, email):
        # 要执行的SQL语句
        sql = """insert into users(nickname,username,password,email)
        values ('%s','%s','%s','%s')""" % (nickname, username, password, email)
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

    # 获取用户
    def user_get(self, _id):
        # 要执行的SQL语句
        sql = """select id, nickname, username, password, email from users where id='%s'""" % _id
        lock = threading.Lock()
        try:
            lock.acquire(True)
            self.init_cursor()
            # 执行语句
            self.cursor.execute(sql)
            # 迭代每一个查到的信息存入数据传输对象中并集中于list
            obj = self.cursor.fetchone()
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        # 数据传输对象
        u = User(
                obj[0],
                obj[1].encode('utf8'),
                obj[2].encode('utf8'),
                obj[3].encode('utf8'),
                obj[4].encode('utf8')
        )
        # result = u.convert2dict()
        result = u
        # 函数返回值
        return result

    # 修改用户
    def user_modify(self, nickname, username, password, email):
        # 要执行的SQL语句
        sql = """update users
        set nickname='%s',password='%s',email='%s'
        where username='%s'""" % (nickname,  password, email, username)
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

    # 删除用户
    def user_delete(self, _id):
        # 要执行的SQL语句
        sql = "delete from users where id=%s" % _id
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
