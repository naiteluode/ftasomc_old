# coding:utf-8
from AnsibleWebApp.dto.Group import Group
from django.db import connection
import json
import threading


class GroupsDao:
    # 初始化函数
    def __init__(self):
        self.connection = None
        self.cursor = None

    def init_cursor(self):
        self.connection = connection
        self.cursor = connection.cursor()

    # 获取主机组列表
    def get_group_list(self):
        lock = threading.Lock()
        try:
            lock.acquire(True)
            # 要执行的SQL语句
            sql = "select * from groups"
            self.init_cursor()
            # 执行语句
            self.cursor.execute(sql)
            # 创建一个用于存放对象集的集合
            result = []
            # 迭代每一个查到的信息存入数据传输对象中并集中于list
            for obj in self.cursor.fetchall():
                # 数据传输对象
                g = Group(
                        obj[0],
                        obj[1].encode('utf8'),
                        obj[2].encode('utf8')
                )
                result.append(g.convert2dict())
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        # 函数返回值
        return json.dumps(result)

    # 增加主机组
    def group_add(self, name, project):
        # 要执行的SQL语句
        sql = "insert into groups(name,project) values ('%s','%s')" % (name, project)
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

    # 删除主机组
    def group_delete(self, _id):
        # 要执行的SQL语句
        sql = "delete from groups where id='%s'" % _id
        lock = threading.Lock()
        try:
            lock.acquire(True)
            self.init_cursor()
            # 执行语句
            self.cursor.execute(sql)
            rowcount_first = self.cursor.rowcount
            first = "ok" if rowcount_first != 0 else "error"
            if first == "ok":
                sql = "delete from groups_servers where grp_id='%s'" % _id
                self.init_cursor()
                # 执行语句
                self.cursor.execute(sql)
                rowcount_sec = self.cursor.rowcount
                sec = "ok" if rowcount_sec != 0 else "error"
                if sec == "ok":
                    result = "ok"
                else:
                    result = "sql error"
            else:
                result = "sql error"
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        return result

    # 根据工程id获取主机组
    def get_groups_by_projects_name(self, parm):
        # 要执行的SQL语句
        sql = "select id,name from groups where project='%s'" % parm
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
                g = Group(
                        obj[0],
                        obj[1].encode('utf8'),
                        "null"
                )
                result.append(g.convert2dict())
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
        # 函数返回值
        return json.dumps(result)

    # 设置主机组生产Ansible配置文件
    def make_hosts_file(self):
        self.init_cursor()
        lock = threading.Lock()
        try:
            lock.acquire(True)
            sql = """select distinct gs.grp_id as 'id',g.name from groups g,servers s,groups_servers gs
            where g.id=gs.grp_id and s.id=gs.ser_id"""
            self.cursor.execute(sql)
            # 创建一个用于存放对象集的集合
            result_group_list = []
            # 迭代每一个查到的信息存入数据传输对象中并集中于list
            for obj in self.cursor.fetchall():
                # 数据传输对象
                g = Group(
                        obj[0],
                        obj[1].encode('utf8'),
                        ""
                )
                result_group_list.append(g.convert2dict())
            # f = file("AnsibleWebApp/db/groups.txt", "w+")
            f = file("/etc/ansible/hosts", "w+")
            for x in result_group_list:
                self.cursor.execute("""select s.ip from groups g,servers s,groups_servers gs
                where g.id=gs.grp_id and s.id=gs.ser_id and gs.grp_id='%s'""" % x['id'])

                # 创建一个用于存放对象集的集合
                result_ip_list = []
                # 迭代每一个查到的信息存入数据传输对象中并集中于list
                for obj in self.cursor.fetchall():
                    result_ip_list.append(obj[0].encode('utf8'))

                f.writelines("["+x['name']+"]\n")
                for y in result_ip_list:
                    f.writelines(y+"\n")
                f.writelines("\n")
            f.close()
        finally:
            self.cursor.close()
            self.connection.commit()
            self.connection.close()
            lock.release()
            file_object = open('/etc/ansible/hosts')
            try:
                result = file_object.read()
            finally:
                file_object.close()
        return result

    # 获取ansible hosts文件内容
    def hosts_get(self):
        file_object = open('/etc/ansible/hosts')
        try:
            result = file_object.read()
        finally:
            file_object.close()
        return result

    # 设置编辑hosts文件内容
    def hosts_set(self, text):
        f = file("/etc/ansible/hosts", "w+")
        try:
            f.write(text)
            result = "ok"
        except:
            result = "error"
        finally:
            f.close()
        return result
