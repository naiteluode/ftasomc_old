# coding:utf-8
class GroupItem:

    # 初始化函数
    def __init__(self, id, group, item):
        # ID
        self.id = id
        # 名称
        self.group = group
        # 所属项目
        self.item = item

    # 把Object对象转换成Dict对象
    def convert2dict(self):
        dictionary = {}
        dictionary.update(self.__dict__)
        return dictionary
