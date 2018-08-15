# coding:utf-8


class Server:

    # 初始化函数
    def __init__(self, id, ip, hostname, type, os):
        # ID
        self.id = id
        # IP
        self.ip = ip
        # host名称
        self.hostname = hostname
        # 处理器类型
        self.type = type
        # 操作系统
        self.os = os

    # 把Object对象转换成Dict对象
    def convert2dict(self):
        dictionary = {}
        dictionary.update(self.__dict__)
        return dictionary