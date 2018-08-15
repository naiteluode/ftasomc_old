# coding:utf-8
import sqlite3
#
#
# class Test:
#
#     # 初始化函数
#     def __init__(self, group, name):
#         self.group = group
#         self.name = name
#
#     # 把Object对象转换成Dict对象
#     def convert2dict(self):
#         dictionary = {}
#         dictionary.update(self.__dict__)
#         return dictionary
#
# connection = sqlite3.connect("../db/ansible_web.db")
#
# cursor = connection.cursor()
#
# cursor.execute("""select distinct gs.grp_id as 'id',g.name from groups g,servers s,groups_servers gs
# where g.id=gs.grp_id and s.id=gs.ser_id""")
#
# # 创建一个用于存放对象集的集合
# result_group_list = []
# # 迭代每一个查到的信息存入数据传输对象中并集中于list
# for obj in cursor.fetchall():
#     # 数据传输对象
#     t = Test(
#             obj[0],
#             obj[1].encode('utf8')
#     )
#     result_group_list.append(t.convert2dict())
#
# f = file("hello.txt", "w+")
# for x in result_group_list:
#     cursor.execute("""select s.ip from groups g,servers s,groups_servers gs
#     where g.id=gs.grp_id and s.id=gs.ser_id and gs.grp_id='%s'""" % x['group'])
#
#     # 创建一个用于存放对象集的集合
#     result_ip_list = []
#     # 迭代每一个查到的信息存入数据传输对象中并集中于list
#     for obj in cursor.fetchall():
#         result_ip_list.append(obj[0].encode('utf8'))
#
#     f.writelines("["+x['name']+"]\n")
#     for y in result_ip_list:
#         f.writelines(y+"\n")
#     f.writelines("\n")
#
# f.close()
#
# cursor.close()
# connection.commit()
# connection.close()

connection = sqlite3.connect("../db/ansible_web.db")

cursor = connection.cursor()

# with open('../db/groups.txt', 'rb') as f:
#     cursor.execute("""insert into playbook(file) values(?)""", (sqlite3.Binary(f.read()), ))
#     cursor.close()
#     connection.commit()
#     connection.close()

cursor = connection.cursor()

cursor.execute("""select file from playbook where id=1""")

# f = file("hello.txt", "w+")

b = cursor.fetchone()[0]

with open('00.yml', 'wb') as f:
    f.write(b)

cursor.close()


