# coding:utf-8
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from AnsibleWebApp.dao.dao import Dao
#from xlwt import *
#import StringIO
import commands
import os
import json
import datetime
import urllib

# 初始化数据连接对象
dao = Dao()


# 执行任务
@csrf_exempt
def start_mission(request):
    command_start_time = datetime.datetime.now()
    query_dict = request.POST
    string = ""
    for x in query_dict:
        string = string+x+"="+request.POST[x].encode('utf-8')+" "
    project_path = os.path.abspath('.')
    bits = 'set -o pipefail;ansible-playbook '\
           + project_path + '/playbook.yml -C --extra-vars "'+string+'"'
    (status, output) = commands.getstatusoutput("bash -c '{0}'".format(bits))
    command_end_time = datetime.datetime.now()
    result = "[ "+str(command_start_time.strftime("%Y-%m-%d %H:%M:%S.%f"))[0:22]+" start ]" + \
                 output + \
             "[ "+str(command_end_time.strftime("%Y-%m-%d %H:%M:%S.%f"))[0:22]+" end ]" + \
             "\n[ 耗时: "+str((command_end_time - command_start_time))[0:10]+" ]"
    return HttpResponse(result, content_type="html/text")


# 跳转到主页
def go_index(request):
    # 用户数量
    users = dao.get_total('users')
    # 主机数量
    hosts = dao.get_total('servers')
    # 工程数量
    projects = dao.get_project_count()
    # 主机组数量
    groups = dao.get_total('groups')
    return render(request, 'index.html', {'hosts': hosts, 'projects': projects, 'users': users, 'groups': groups})


# 跳转到主机列表页面
def go_inventory(request):
    return render(request, 'inventory.html')


# 删除关系操作
@csrf_exempt
def inventory_delete(request):
    inventory_id = request.POST['id'].encode('utf8')
    result = dao.inventory_delete(str(inventory_id))
    if result == "error":
        send = {'status': 'error'}
    else:
        send = {'status': 'ok'}
    return HttpResponse(json.dumps(send), content_type="application/json")


# 添加资产关系
@csrf_exempt
def inventory_add(request):
    group_id = request.POST['group_id'].encode('utf8')
    server_id = request.POST['host_id'].encode('utf8')
    result = dao.inventory_add(str(group_id), str(server_id))
    if result == "ok":
        return HttpResponseRedirect('/inventory/')
    else:
        return HttpResponse(result, content_type="application/json")


# 跳转到主机组列表页面
def go_group(request):
    return render(request, 'group.html')


# 跳转到部署页面
def go_deploy(request):
    return render(request, 'deploy.html')


# 获取所有的主机组项目总数
@csrf_exempt
def get_all_items_count(request):
    result = dao.get_all_items_count()
    return HttpResponse(result, content_type="application/json")


# 获取主机组列表
@csrf_exempt
def get_group_list(request):
    result = dao.get_group_list()
    return HttpResponse(result, content_type="application/json")


# 获取服务器列表
@csrf_exempt
def get_server_list(request):
    result = dao.get_server_list()
    return HttpResponse(result, content_type="application/json")


# 获取机器详细列表
@csrf_exempt
def get_inventory_list(request):
    result = dao.get_inventory_list()
    return HttpResponse(result, content_type="application/json")


# 获取工程列表
@csrf_exempt
def get_project_list(request):
    result = dao.get_project_list()
    return HttpResponse(result, content_type="application/json")


# 跳转到用户列表页面
def go_user(request):
    return render(request, 'user.html')


# 跳转到添加用户页面
def go_user_new(request):
    return render(request, 'addUser.html')


# 添加用户操作
@csrf_exempt
def user_add(request):
    username = request.POST['username'].encode('utf8')
    password = request.POST['password'].encode('utf8')
    nickname = request.POST['nickname'].encode('utf8')
    email = request.POST['email'].encode('utf8')
    result = dao.user_add(nickname, username, password, email)
    if result == "ok":
        return HttpResponseRedirect('/user/')
    else:
        return HttpResponse(result, content_type="application/json")


# 检查用户名
@csrf_exempt
def user_check(request):
    username = request.POST['username'].encode('utf8')
    result = dao.check_username(username)
    if result == "no":
        send = {'status': 'no'}
    else:
        send = {'status': 'ok'}
    return HttpResponse(json.dumps(send), content_type="application/json")


# 检查IP
@csrf_exempt
def server_check(request):
    ip = request.POST['ip'].encode('utf8')
    result = dao.check_ip(ip)
    if result == "no":
        send = {'status': 'no'}
    else:
        send = {'status': 'ok'}
    return HttpResponse(json.dumps(send), content_type="application/json")


# 获取用户列表
@csrf_exempt
def get_user_list(request):
    result = dao.get_user_list()
    return HttpResponse(result, content_type="application/json")


# 跳转到编辑用户页面
@csrf_exempt
def go_user_edit(request):
    _id = request.POST['id'].encode('utf8')
    user = dao.user_get(str(_id))
    __id = user.id
    nickname = user.nickname
    username = user.username
    password = user.password
    email = user.email
    return render(request, 'editUser.html',
                  {"id": __id, "nickname": nickname, "username": username, "password": password, "email": email})


# 修改用户操作
@csrf_exempt
def user_modify(request):
    username = request.POST['username'].encode('utf8')
    password = request.POST['password'].encode('utf8')
    nickname = request.POST['nickname'].encode('utf8')
    email = request.POST['email'].encode('utf8')
    result = dao.user_modify(nickname, username, password, email)
    if result == "ok":
        return HttpResponseRedirect('/user/')
    else:
        return HttpResponse(result, content_type="application/json")


# 删除用户操作
@csrf_exempt
def user_delete(request):
    user_id = request.POST['id'].encode('utf8')
    result = dao.user_delete(str(user_id))
    if result == "error":
        send = {'status': 'error'}
    else:
        send = {'status': 'ok'}
    return HttpResponse(json.dumps(send), content_type="application/json")


# 根据工程id获取工程项目组
@csrf_exempt
def get_groups_by_projects_name(request, parm):
    parm_str = str(parm)
    result = dao.get_groups_by_projects_name(parm_str)
    return HttpResponse(result, content_type="application/json")


# 根据主机组id获取项目
@csrf_exempt
def get_items_by_groups_id(request, parm):
    if parm == "" or parm is None:
        parm = -1
    parm_str = str(parm)
    result = dao.get_items_by_groups_id(parm_str)
    return HttpResponse(result, content_type="application/json")


# 删除主机组操作
@csrf_exempt
def group_delete(request):
    group_id = request.POST['id'].encode('utf8')
    result = dao.group_delete(str(group_id))
    if result == "error":
        send = {'status': 'error'}
    else:
        send = {'status': 'ok'}
    return HttpResponse(json.dumps(send), content_type="application/json")


# 添加主机组操作
@csrf_exempt
def group_add(request):
    name = request.POST['name'].encode('utf8')
    project = request.POST['project'].encode('utf8')
    result = dao.group_add(name, project)
    return HttpResponse(json.dumps(result), content_type="application/json")


# 跳转到添加主机页面
def go_server_new(request):
    result = dao.get_max_table_id(str("servers"))
    return render(request, 'addHost.html', {"id": result+1})


# 获取表最大id
@csrf_exempt
def get_max_table_id(request, parm):
    result = dao.get_max_table_id(str(parm))
    return HttpResponse(result, content_type="application/json")


# 添加主机操作
@csrf_exempt
def server_add(request):
    server_id = request.POST['id'].encode('utf8')
    server_ip = request.POST['ip'].encode('utf8')
    server_hostname = request.POST['hostname'].encode('utf8')
    server_type = request.POST['type'].encode('utf8')
    server_os = request.POST['os'].encode('utf8')
    # server_group = request.POST['group'].encode('utf8')
    result = dao.server_add(str(server_id),
                            str(server_ip),
                            str(server_hostname),
                            str(server_os),
                            str(server_type))
    #                       str(server_group))
    if result == "ok":
        return HttpResponseRedirect('/inventory/')
    else:
        return HttpResponse(result, content_type="application/json")


# 删除主机组操作
@csrf_exempt
def server_delete(request):
    group_server_id = request.POST['id'].encode('utf8')
    result = dao.server_delete(str(group_server_id))
    if result == "error":
        send = {'status': 'error'}
    else:
        send = {'status': 'ok'}
    return HttpResponse(json.dumps(send), content_type="application/json")


# 通过工程名获取所有任务
@csrf_exempt
def get_all_mission_by_project(request):
    project = request.POST['project'].encode('utf-8')
    result = dao.get_all_mission_by_project(project)
    return HttpResponse(result, content_type="application/json")


# 通过组id获取组内ip地址
@csrf_exempt
def get_server_by_group(request):
    group_id = request.POST['id'].encode('utf-8')
    result = dao.get_server_by_group(group_id)
    return HttpResponse(result, content_type="application/json")


# 跳转到编辑主机页面
@csrf_exempt
def go_server_edit(request):
    result = request.POST['id'].encode('utf-8')
    server = dao.server_get(str(result))
    _id = server.id
    ip = server.ip
    hostname = server.hostname
    _type = server.type
    _os = server.os
    return render(request, 'editHost.html', {"id": _id, "ip": ip, "hostname": hostname, "type": _type, "os": _os})


# 修改主机
@csrf_exempt
def server_modify(request):
    _id = request.POST['id'].encode('utf8')
    ip = request.POST['ip'].encode('utf8')
    hostname = request.POST['hostname'].encode('utf8')
    _type = request.POST['type'].encode('utf8')
    _os = request.POST['os'].encode('utf8')
    result = dao.server_modify(_id, ip, hostname, _type, _os)
    if result == "ok":
        return HttpResponseRedirect('/inventory/')
    else:
        return HttpResponse(result, content_type="application/json")


# 跳转到帮助页面
def go_help(request):
    return render(request, 'help.html')


# 跳转到日志页面
def go_log(request):
    return render(request, 'log.html')


# 用户登出
def logout(request):
    result = "to be continued..."
    return HttpResponse(result, content_type="application/json")


# 获取项目列表
@csrf_exempt
def get_items_list(request):
    result = dao.get_items_list()
    return HttpResponse(result, content_type="application/json")


# 获取主机组项目列表
@csrf_exempt
def get_group_items_list(request):
    result = dao.get_group_items_list()
    return HttpResponse(result, content_type="application/json")


# 添加主机组项目操作
@csrf_exempt
def group_items_add(request):
    group_id = request.POST['groupId'].encode('utf8')
    item_id = request.POST['itemId'].encode('utf8')
    result = dao.group_items_add(str(group_id), str(item_id))
    return HttpResponse(json.dumps(result), content_type="application/json")


# 删除主机组项目操作
@csrf_exempt
def group_items_delete(request):
    _id = request.POST['id'].encode('utf8')
    result = dao.group_items_delete(str(_id))
    if result == "error":
        send = {'status': 'error'}
    else:
        send = {'status': 'ok'}
    return HttpResponse(json.dumps(send), content_type="application/json")


# 添加项目操作
@csrf_exempt
def items_add(request):
    name = request.POST['name'].encode('utf8')
    result = dao.items_add(str(name))
    return HttpResponse(json.dumps(result), content_type="application/json")


# 删除项目操作
@csrf_exempt
def items_delete(request):
    _id = request.POST['id'].encode('utf8')
    result = dao.items_delete(str(_id))
    if result == "error":
        send = {'status': 'error'}
    else:
        send = {'status': 'ok'}
    return HttpResponse(json.dumps(send), content_type="application/json")


# 跳转到ansible执行页面
def go_ansible(request):
    return render(request, 'ansible.html')


# 根据参数组合Ansible命令
@csrf_exempt
def ansible_comb(request):
    grp = request.POST['grp'].encode('utf-8')
    mod = request.POST['mod'].encode('utf-8')
    arg = request.POST['arg'].encode('utf-8')
    final_cmd = "ansible "+grp+" -m "+mod+" -a '"+arg+"'"
    return HttpResponse(json.dumps(final_cmd))


# 根据参数组合Ansible命令
@csrf_exempt
def ansible_run(request):
    cmd = request.POST['cmd'].encode('utf-8')
    bits = 'set -o pipefail;'+cmd
    (status, output) = commands.getstatusoutput('bash -c "{0}"'.format(bits))
    result = output
    print output
    return HttpResponse(result, content_type="html/text")


# 跳转到hosts页面
def go_hosts(request):
    return render(request, 'hosts.html')


# 设置hosts文件内容列表
@csrf_exempt
def hosts_list(request):
    result = dao.make_hosts_file()
    return HttpResponse(result, content_type="text")


# 获取hosts文件内容
@csrf_exempt
def hosts_get(request):
    result = dao.hosts_get()
    return HttpResponse(result, content_type="text")


# 设置编辑hosts文件内容
@csrf_exempt
def hosts_set(request):
    text = request.POST['text'].encode('utf-8')
    result = dao.hosts_set(text)
    return HttpResponse(result, content_type="text")


# 跳转到script页面
def go_playbook(request):
    return render(request, 'playbook.html')


# 获取playbook列表
@csrf_exempt
def get_playbook_list(request):
    result = dao.get_playbook_list()
    return HttpResponse(result, content_type="application/json")


# 根据ID获取playbook内容
@csrf_exempt
def get_playbook(request):
    _id = request.POST['id'].encode('utf-8')
    result = dao.get_playbook(_id)
    return HttpResponse(result, content_type="text")


# 添加playbook脚本
@csrf_exempt
def playbook_add(request):
    name = request.POST['name'].encode('utf-8')
    _file = request.POST['file'].encode('utf-8')
    extension = "yml"
    result = dao.playbook_add(name, extension, _file)
    return HttpResponse(result, content_type="application/json")


# 执行playbook脚本
@csrf_exempt
def playbook_start(request):
    command_start_time = datetime.datetime.now()
    query_dict = request.POST
    string = ""
    playbook = dao.playbook_start(request.POST['id'].encode('utf-8'))
    p_stat = playbook['status']
    name = playbook['name']
    for x in query_dict:
        if x == "id":
            pass
        else:
            string = string+x+"="+request.POST[x].encode('utf-8')+" "
    db_path = os.path.abspath('.')+"/AnsibleWebApp/db"
    bits = 'set -o pipefail;ansible-playbook '\
           + db_path + '/playbook.yml -C --extra-vars \"'+string+'\"'
    (status, output) = commands.getstatusoutput("bash -c '{0}'".format(bits))
    # print "bash -c '{0}'".format(bits)
    command_end_time = datetime.datetime.now()
    if p_stat == "ok":
        result = "[ "+str(command_start_time.strftime("%Y-%m-%d %H:%M:%S.%f"))[0:22]+" "+str(name)+" start ]"+\
                 output+\
                 "[ "+str(command_end_time.strftime("%Y-%m-%d %H:%M:%S.%f"))[0:22]+" "+str(name)+" end ]\n"+\
                 "[ 耗时: "+str((command_end_time - command_start_time))[0:10]+" ]"
    else:
        result = "Database Error!"
    return HttpResponse(result, content_type="html/text")


# 获取playbook列表
@csrf_exempt
def get_script_list(request):
    result = dao.get_script_list()
    return HttpResponse(result, content_type="application/json")


"""
# 执行script脚本
@csrf_exempt
def script_start(request):
    command_start_time = datetime.datetime.now()
    script = dao.script_start(request.POST['id'].encode('utf-8'))
    ip = request.POST['ip'].encode('utf-8')
    p_stat = script['status']
    script_list = script['file']
    result = []
    for line in script_list:
        bits = 'set -o pipefail;ansible '+ip+' -m shell -a \"'+line+'\" | sed \'1d;$d\''
        (status, output) = commands.getstatusoutput(bits)
        result.append("[ "+line+" ]\n")
        result.append(output+"\n")
    command_end_time = datetime.datetime.now()
    if p_stat == "ok":
        result.append("[ time: "+str((command_end_time - command_start_time))+" ]")
    else:
        result = "Database Error!"
    return HttpResponse(''.join(result), content_type="html/text")
"""

"""
# 执行script脚本
@csrf_exempt
def script_start(request):
    command_start_time = datetime.datetime.now()
    script = dao.script_start(request.POST['id'].encode('utf-8'))
    ip = request.POST['ip'].encode('utf-8')
    p_stat = script['status']
    script_list = script['file']
    result = []
    bits = 'set -o pipefail;ansible '+ip+' -m shell -a \"'+(''.join(script_list))+'\" | sed \'1d;$d\''
    (status, output) = commands.getstatusoutput(bits)
    command_end_time = datetime.datetime.now()
    result.append(output)
    if p_stat == "ok":
        result.append("\n[ 耗时: "+str((command_end_time - command_start_time))+" ]")
    else:
        result = "Database Error!"
    return HttpResponse(result, content_type="html/text")
"""


# 执行script脚本
@csrf_exempt
def script_start(request):
    command_start_time = datetime.datetime.now()
    script = dao.script_start(request.POST['id'].encode('utf-8'))
    ip = request.POST['ip'].encode('utf-8')
    p_stat = script['status']
    result = []
    filename = script['filename']
    extension = script['extension']
    db_path = os.path.abspath('.')+"/AnsibleWebApp/db"
    # 解决在windows中换行与linux换行格式不一致的问题
    bits1 = 'tr -d "\r" < '+db_path+'/'+filename+'.'+extension+' > '+db_path+'/'+filename+'_final.'+extension
    (status1, output1) = commands.getstatusoutput("bash -c '{0}'".format(bits1))
    # 将文件发放到目标机
    if status1 == 0:
        bits2 = 'set -o pipefail;ansible '\
               + ip + ' -m copy -a \"src='\
               + db_path + '/' + filename + '_final.' + extension + ' dest=/tmp'\
               + '/' + filename + '.' + extension + '\" | grep -i success'
        (status2, output2) = commands.getstatusoutput("bash -c '{0}'".format(bits2))
        # 从目标机执行文件
        if status2 == 0:
            bits3 = 'set -o pipefail;ansible ' \
                    + ip + ' -m shell -a \"sh /tmp/' + filename + '.' + extension + '\" | sed \'1d;$d\''
            (status3, output3) = commands.getstatusoutput(bits3)
            command_end_time = datetime.datetime.now()
            result.append(output3)
        else:
            result.append("No hosts matched")
            command_end_time = datetime.datetime.now()
    else:
        command_end_time = datetime.datetime.now()
    if p_stat == "ok":
        result.append("\n[ 耗时: "+str((command_end_time - command_start_time))[0:10]+" ]")
    else:
        result = "Database Error!"
    return HttpResponse(result, content_type="html/text")


# 跳转到files页面
def go_files(request):
    return render(request, 'files.html')


# 文件列表
@csrf_exempt
def list_dir(request):
    r = ['<ul class="jqueryFileTree" style="display: none;">']
    try:
        r = ['<ul class="jqueryFileTree" style="display: none;">']
        files_path = os.path.abspath('.')+os.path.sep+'AnsibleWebApp'+os.path.sep+'db'+os.path.sep+'files'
        d = urllib.unquote(request.POST.get('dir', files_path))
        for f in os.listdir(d):
            ff = os.path.join(d, f)
            if os.path.isdir(ff):
                r.append('<li class="directory collapsed"><a href="#" rel="%s/">%s</a></li>' % (ff, f))
            else:
                # get .ext and remove dot
                e = os.path.splitext(f)[1][1:]
                r.append('<li class="file ext_%s"><a href="#" rel="%s">%s</a></li>' % (e, ff, f))
        r.append('</ul>')
    except Exception, e:
        r.append('Could not load directory: %s' % str(e))
    r.append('</ul>')
    return HttpResponse(''.join(r))


# 获取文件目录路径
@csrf_exempt
def get_file_path(request):
    files_path = os.path.abspath('.')+os.path.sep+'AnsibleWebApp'+os.path.sep+'db'+os.path.sep+'files'
    return HttpResponse(files_path, content_type="html/text")


# 查看文件内容
@csrf_exempt
def file_view(request):
    path = request.POST['path'].encode('utf-8')
    file_size = os.path.getsize(path)
    if file_size > 15360:
        output = "文件内容过大,本页无法显示"
    elif file_size == 0:
        output = "文件内容为空"
    else:
        bits = 'set -o pipefail;cat ' + path
        (status, output) = commands.getstatusoutput("bash -c '{0}'".format(bits))
    return HttpResponse(output, content_type="html/text")


# 文件上传处理
@csrf_exempt
def file_upload(request):
    files_path = os.path.abspath('.')+os.path.sep+'AnsibleWebApp'+os.path.sep+'db'+os.path.sep+'files'
    files = request.FILES['file']
    upload_files_path = os.path.join(files_path, files.name)

    destination = open(upload_files_path, 'w')
    for chunk in files.chunks():
        print chunk
        destination.write(chunk)
    destination.close()

    result = {}
    result["status"] = True
    id = {"id": dao.utl.get_uuid()}
    result["data"] = id
    result["message"] = "success"
    result_json = json.dumps(result)
    return HttpResponse(result_json, content_type="application/json")


# 跳转到添加脚本页面
def go_add_script(request):
    return render(request, 'addScript.html')

"""
# excel测试
@csrf_exempt
def excel_export(request):
    # 导出excel表格
    list_obj = [{"id": 1, "username": "a", "time": str(datetime.datetime.now().strftime("%Y-%m-%d"))[:10], "content": "cc", "source": "ss"}]
    strs = '{"id": 2, "username": "a", "time": "' + str(datetime.datetime.now().strftime("%Y-%m-%d"))[:10] \
           + '", "content": "cc", "source": "ss"}'
    strs2 = '{"id": 3, "username": "a", "time": "' + str(datetime.datetime.now().strftime("%Y-%m-%d"))[:10] \
           + '", "content": "cc", "source": "ss"}'
    a = json.loads("["+strs+","+strs2+"]")
    print a
    list_obj.append(a[0])
    list_obj.append(a[1])
    if list_obj:
        # 创建工作薄
        ws = Workbook(encoding='utf-8')
        w = ws.add_sheet(u"数据报表第一页")
        w.write(0, 0, "id")
        w.write(0, 1, u"用户名")
        w.write(0, 2, u"发布时间")
        w.write(0, 3, u"内容")
        w.write(0, 4, u"来源")
        # 写入数据
        excel_row = 1
        for obj in list_obj:
            data_id = obj['id']
            data_user = obj['username']
            data_time = obj['time']
            data_content = obj['content']
            dada_source = obj['source']
            w.write(excel_row, 0, data_id)
            w.write(excel_row, 1, data_user)
            w.write(excel_row, 2, data_time)
            w.write(excel_row, 3, data_content)
            w.write(excel_row, 4, dada_source)
            excel_row += 1
        # 检测文件是够存在
        # 方框中代码是保存文件使用，可以不用加
        ###########################
        exist_file = os.path.exists("test.xls")
        if exist_file:
            os.remove(r"test.xls")
        ws.save("test.xls")
        ############################
        sio = StringIO.StringIO()
        ws.save(sio)
        sio.seek(0)
        response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=test.xls'
        response.write(sio.getvalue())
        return response
"""
