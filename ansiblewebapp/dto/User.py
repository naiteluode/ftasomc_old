# coding:utf-8
class User:

    # 初始化函数
    def __init__(self, id, nickname, username, password, email):
        # ID
        self.id = id
        # host名称
        self.nickname = nickname
        # 处理器类型
        self.username = username
        # 操作系统
        self.password = password
        # 分组
        self.email = email

    # 把Object对象转换成Dict对象
    def convert2dict(self):
        dictionary = {}
        dictionary.update(self.__dict__)
        return dictionary
