# coding:utf-8
class Mission:

    # 初始化函数
    def __init__(self, group, ip, item):
        # 所属主机组
        self.group = group
        # IP
        self.ip = ip
        # 项目报
        self.item = item

    # 把Object对象转换成Dict对象
    def convert2dict(self):
        dictionary = {}
        dictionary.update(self.__dict__)
        return dictionary
