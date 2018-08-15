# coding:utf-8
class Project:

    # 初始化函数
    def __init__(self, name):
        # 名称
        self.name = name

    # 把Object对象转换成Dict对象
    def convert2dict(self):
        dictionary = {}
        dictionary.update(self.__dict__)
        return dictionary
