# coding:utf-8


class Inventory:

    # 初始化函数
    def __init__(self, id, sid, ip, host, type, os, group):
        # ID
        self.id = id
        # Server ID
        self.sid = sid
        # IP
        self.ip = ip
        # host名称
        self.host = host
        # 处理器类型
        self.type = type
        # 操作系统
        self.os = os
        # 分组
        self.group = group

    # 把Object对象转换成Dict对象
    def convert2dict(self):
        dictionary = {}
        dictionary.update(self.__dict__)
        return dictionary
