# coding:utf-8


class ItemCount:

    # 初始化函数
    def __init__(self, name, count):
        # 名称
        self.name = name
        # 子项个数
        self.count = count

    # 把Object对象转换成Dict对象
    def convert2dict(self):
        dictionary = {}
        dictionary.update(self.__dict__)
        return dictionary
