# coding:utf-8
from AnsibleWebApp.dao.groupsDao import GroupsDao
from AnsibleWebApp.dao.utilsDao import UtilsDao
from AnsibleWebApp.dao.serversDao import ServersDao
from AnsibleWebApp.dao.usersDao import UsersDao
from AnsibleWebApp.dao.othersDao import OthersDao
from AnsibleWebApp.dao.itemsDao import ItemsDao
from AnsibleWebApp.dao.scriptDao import ScriptDao


# 数据连接对象
class Dao:
    # 初始化函数
    def __init__(self):
        self.g = GroupsDao()
        self.utl = UtilsDao()
        self.s = ServersDao()
        self.u = UsersDao()
        self.o = OthersDao()
        self.i = ItemsDao()
        self.p = ScriptDao()

    # ====================================================================================================
    # utilsDao start
    # ====================================================================================================

    # 查询表内数据总数
    def get_total(self, table):
        result = self.utl.get_total(table)
        return result

    # 查询工程总数
    def get_project_count(self):
        result = self.utl.get_project_count()
        return result

    # 获取表最大id
    def get_max_table_id(self, table):
        result = self.utl.get_max_table_id(table)
        return result

    # 验证用户名
    def check_username(self, name):
        result = self.utl.check_username(name)
        return result

    # 验证IP
    def check_ip(self, ip):
        result = self.utl.check_ip(ip)
        return result

    # 获取所有主机组项目数
    def get_all_items_count(self):
        result = self.utl.get_all_items_count()
        return result

    # 生成uuid
    def get_uuid(self):
        result = self.utl.get_uuid()
        return result

    # ====================================================================================================
    # utilsDao end
    # ====================================================================================================

    # ====================================================================================================
    # groupsDao start
    # ====================================================================================================

    # 获取主机组列表
    def get_group_list(self):
        result = self.g.get_group_list()
        return result

    # 增加主机组
    def group_add(self, name, project):
        result = self.g.group_add(name, project)
        return result

    # 删除主机组
    def group_delete(self, _id):
        result = self.g.group_delete(_id)
        return result

    # 根据工程id获取主机组
    def get_groups_by_projects_name(self, name):
        result = self.g.get_groups_by_projects_name(name)
        return result

    # 获取主机组生产Ansible配置文件
    def make_hosts_file(self):
        result = self.g.make_hosts_file()
        return result

    # 获取ansible hosts文件内容
    def hosts_get(self):
        result = self.g.hosts_get()
        return result

    # 设置编辑hosts文件内容
    def hosts_set(self, text):
        result = self.g.hosts_set(text)
        return result

    # ====================================================================================================
    # groupsDao end
    # ====================================================================================================

    # ====================================================================================================
    # serversDao start
    # ====================================================================================================

    # 获取主机列表
    def get_server_list(self):
        result = self.s.get_server_list()
        return result

    # 增加主机
    def server_add(self, _id, ip, hostname, _os, _type):
        result = self.s.server_add(_id, ip, hostname, _os, _type)
        return result

    # 修改主机
    def server_modify(self, _id, ip, hostname, _type, _os):
        result = self.s.server_modify(_id, ip, hostname, _type, _os)
        return result

    # 删除主机
    def server_delete(self, _id):
        result = self.s.server_delete(_id)
        return result

    # 通过组id查询组内主机ip列表
    def get_server_by_group(self, _id):
        result = self.s.get_server_by_group(_id)
        return result

    # 根据主机id查询主机信息
    def server_get(self, _id):
        result = self.s.server_get(_id)
        return result

    # ====================================================================================================
    # serversDao end
    # ====================================================================================================

    # ====================================================================================================
    # usersDao start
    # ====================================================================================================

    # 获取用户列表
    def get_user_list(self):
        result = self.u.get_user_list()
        return result

    # 增加用户
    def user_add(self, nickname, username, password, email):
        result = self.u.user_add(nickname, username, password, email)
        return result

    # 获取用户
    def user_get(self, _id):
        result = self.u.user_get(_id)
        return result

    # 修改用户
    def user_modify(self, nickname, username, password, email):
        result = self.u.user_modify(nickname, username, password, email)
        return result

    # 删除用户
    def user_delete(self, _id):
        result = self.u.user_delete(_id)
        return result

    # ====================================================================================================
    # usersDao end
    # ====================================================================================================

    # ====================================================================================================
    # othersDao start
    # ====================================================================================================

    # 获取工程列表
    def get_project_list(self):
        result = self.o.get_project_list()
        return result

    # 获取机器详细信息列表
    def get_inventory_list(self):
        result = self.o.get_inventory_list()
        return result

    # 删除关系
    def inventory_delete(self, _id):
        result = self.o.inventory_delete(_id)
        return result

    # 添加资产关系
    def inventory_add(self, grp_id, ser_id):
        result = self.o.inventory_add(grp_id, ser_id)
        return result

    # 通过工程名获取所有任务
    def get_all_mission_by_project(self, project):
        result = self.o.get_all_mission_by_project(project)
        return result

    # ====================================================================================================
    # othersDao end
    # ====================================================================================================

    # ====================================================================================================
    # itemsDao start
    # ====================================================================================================

    # 根据主机组id获取项目
    def get_items_by_groups_id(self, _id):
        result = self.i.get_items_by_groups_id(_id)
        return result

    # 获取项目列表
    def get_items_list(self):
        result = self.i.get_items_list()
        return result

    # 获取主机组项目列表
    def get_group_items_list(self):
        result = self.i.get_group_items_list()
        return result

    # 添加主机组项目
    def group_items_add(self, group, item):
        result = self.i.group_items_add(group, item)
        return result

    # 删除主机组项目
    def group_items_delete(self, _id):
        result = self.i.group_items_delete(_id)
        return result

    # 添加项目
    def items_add(self, name):
        result = self.i.items_add(name)
        return result

    # 删除项目
    def items_delete(self, _id):
        result = self.i.items_delete(_id)
        return result

    # ====================================================================================================
    # itemsDao end
    # ====================================================================================================

    # ====================================================================================================
    # scriptDao start
    # ====================================================================================================

    # 获取playbook列表信息
    def get_playbook_list(self):
        result = self.p.get_playbook_list()
        return result

    # 获取sh列表信息
    def get_script_list(self):
        result = self.p.get_script_list()
        return result

    # 根据id获取playbook文件内容
    def get_playbook(self, _id):
        result = self.p.get_playbook(_id)
        return result

    # 增加Playbook脚本
    def playbook_add(self, name, extension, _file):
        result = self.p.playbook_add(name, extension, _file)
        return result

    # 执行playbook脚本
    def playbook_start(self, _id):
        result = self.p.playbook_start(_id)
        return result

    # 执行script脚本
    def script_start(self, _id):
        result = self.p.script_start(_id)
        return result

    # ====================================================================================================
    # scriptDao end
    # ====================================================================================================
