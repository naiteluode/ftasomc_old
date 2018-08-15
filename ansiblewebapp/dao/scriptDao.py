# coding:utf-8
from AnsibleWebApp.dto.Script import Script
from django.db import connection
import json
import threading


class ScriptDao:
    # 初始化函数
    def __init__(self):
        self.connection = None
        self.cursor = None

    def init_cursor(self):
        self.connection = connection
        self.cursor = connection.cursor()

    # 获取playbook列表
    def get_playbook_list(self):
        lock = threading.Lock()
        try:
            lock.acquire(True)
            # 要执行的SQL语句
            sql = "select s.id,s.name,s.extension from script s where s.extension='yml'"
            self.init_cursor()
            # 执行语句
            self.cursor.execute(sql)
            # 创建一个用于存放对象集的集合
            result = []
            # 迭代每一个查到的信息存入数据传输对象中并集中于list
            for obj in self.cursor.fetchall():
                # 数据传输对象
                s = Script(
                        obj[0],
                        obj[1].encode('utf8'),
                        obj[2].encode('utf8'),
                        ""
                )
                result.append(s.convert2dict())
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        # 函数返回值
        return json.dumps(result)

    # 获取脚本列表
    def get_script_list(self):
        lock = threading.Lock()
        try:
            lock.acquire(True)
            # 要执行的SQL语句
            sql = "select s.id,s.name,s.extension from script s where s.extension!='yml'"
            self.init_cursor()
            # 执行语句
            self.cursor.execute(sql)
            # 创建一个用于存放对象集的集合
            result = []
            # 迭代每一个查到的信息存入数据传输对象中并集中于list
            for obj in self.cursor.fetchall():
                # 数据传输对象
                s = Script(
                        obj[0],
                        obj[1].encode('utf8'),
                        obj[2].encode('utf8'),
                        ""
                )
                result.append(s.convert2dict())
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        # 函数返回值
        return json.dumps(result)

    # 根据id获取playbook文件内容
    def get_playbook(self, _id):
        self.init_cursor()
        lock = threading.Lock()
        try:
            lock.acquire(True)
            sql = """select name,extension,file from script where id='%s'""" % _id
            self.cursor.execute(sql)
            # 创建一个用于存放对象集的集合
            result = []
            # 迭代每一个查到的信息存入数据传输对象中并集中于list
            obj = self.cursor.fetchone()
            if type(obj[2]) == buffer:
                file_tmp = str(obj[2])
            else:
                file_tmp = obj[2].encode("utf8")
            # 数据传输对象
            s = Script(
                    "",
                    obj[0].encode("utf8"),
                    obj[1].encode("utf8"),
                    file_tmp
            )
            result.append(s.convert2dict())
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        return json.dumps(result)

    # 增加script脚本
    def playbook_add(self, name, extension, _file):
        # 要执行的SQL语句
        sql = "insert into script(name,extension,file) values('%s','%s','%s')" % (name, extension, _file)
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
        return json.dumps(result)

    # 执行script脚本
    def playbook_start(self, _id):
        self.init_cursor()
        lock = threading.Lock()
        try:
            lock.acquire(True)
            sql = "select id,name,extension,file from script where id='%s'" % _id
            self.cursor.execute(sql)
            # 创建一个用于存放对象集的集合
            result_group_list = []
            # 迭代每一个查到的信息存入数据传输对象中并集中于list
            obj = self.cursor.fetchone()
            if type(obj[3]) == buffer:
                file_tmp = str(obj[3])
            else:
                file_tmp = obj[3].encode("utf8")
            # 数据传输对象
            s = Script(
                    obj[0],
                    obj[1].encode("utf8"),
                    obj[2].encode("utf8"),
                    file_tmp
            )
            result_group_list.append(s.convert2dict())
            f = file("AnsibleWebApp/db/playbook.yml", "w+")
            f.write(s.file)
            f.close()
            result = {}
            result['status'] = "ok"
            result['name'] = s.name
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        return result

    """
    # 执行script脚本
    def script_start(self, _id):
        self.init_cursor()
        lock = threading.Lock()
        try:
            lock.acquire(True)
            sql = "select id,name,extension,file from script where id='%s'" % _id
            self.cursor.execute(sql)
            # 创建一个用于存放对象集的集合
            result_group_list = []
            # 迭代每一个查到的信息存入数据传输对象中并集中于list
            obj = self.cursor.fetchone()
            if type(obj[3]) == buffer:
                file_tmp = str(obj[3])
            else:
                file_tmp = obj[3].encode("utf8")
            # 数据传输对象
            s = Script(
                    obj[0],
                    obj[1].encode("utf8"),
                    obj[2].encode("utf8"),
                    file_tmp
            )
            result_group_list.append(s.convert2dict())
            file_name = s.name+"."+s.extension
            f = file("AnsibleWebApp/db/"+file_name, "w+")
            f.write(s.file)
            f.close()
            result = {}
            result['status'] = "ok"
            ff = open("AnsibleWebApp/db/"+file_name)
            file_list = []
            for line in ff:
                file_list.append(line.strip()+";")
            result['file'] = file_list
            ff.close()
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        return result
    """

    # 执行script脚本
    def script_start(self, _id):
        self.init_cursor()
        lock = threading.Lock()
        try:
            lock.acquire(True)
            sql = "select id,name,extension,file from script where id='%s'" % _id
            self.cursor.execute(sql)
            # 创建一个用于存放对象集的集合
            result_group_list = []
            # 迭代每一个查到的信息存入数据传输对象中并集中于list
            obj = self.cursor.fetchone()
            if type(obj[3]) == buffer:
                file_tmp = str(obj[3])
            else:
                file_tmp = obj[3].encode("utf8")
            # 数据传输对象
            s = Script(
                    obj[0],
                    obj[1].encode("utf8"),
                    obj[2].encode("utf8"),
                    file_tmp
            )
            result_group_list.append(s.convert2dict())
            file_name = s.name+"."+s.extension
            f = file("AnsibleWebApp/db/"+file_name, "w+")
            f.write(s.file)
            f.close()
            result = {}
            result['status'] = "ok"
            result['filename'] = s.name
            result['extension'] = s.extension
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        return result
