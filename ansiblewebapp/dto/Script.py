# coding:utf-8
class Script:

    # 初始化函数
    def __init__(self, id, name, extension, file):
        # ID
        self.id = id
        # 名称
        self.name = name
        # 扩展名
        self.extension = extension
        # 文件内容
        self.file = file

    # 把Object对象转换成Dict对象
    def convert2dict(self):
        dictionary = {}
        dictionary.update(self.__dict__)
        return dictionary
