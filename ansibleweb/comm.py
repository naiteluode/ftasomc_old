#!/usr/bin/env python
#coding=utf-8
####################
#全局变量
from_mail = 'salt@ftas.cn'
samail_list = ['salt@ftas.cn','err@ftas.cn',]
interval = 7200 #报警间隔
masterip = '127.0.0.1'
network_list = ('192.168','10.0')
pagelimit = 8	#分页
dangercmdlist = ('rm','reboot','init ','shutdown')
download_url = 'http://%s:8000/' % masterip
base_dir = ''
script_dir = '%sscripts/' % base_dir
rrd_dir = '%srrdtool/' % base_dir
rrdpic_dir = '%sstatic/rrd/' % base_dir
upload_dir = '%supload/' % base_dir
sshdefaultport = 50718
thread_num = 20
rrdstep = 120 
groupsconf = '/etc/salt/master.d/group.conf'
ansiblegroupsconf = '/etc/ansible/hosts'
ansiblelog = '/var/log/ansible.log'
dbname = 'salt'
dbuser = 'root'
dbpasswd = 'root'
####################
def ssh(ip,port,user,passwd,cmd):
    import paramiko
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip,int(port),user,passwd,timeout=5)
    except:
        return {ip:"Error: connect fail !!!"}
    try:
        stdin, stdout, stderr = ssh.exec_command(cmd)
    except:
        return {ip:"Error: exec fail !!!"}
    i = stderr.readlines()
    if i:
        return {ip:''.join(i)}
    return {ip:''.join(stdout.readlines())}
    ssh.close()

def curl(url,ip,port):
    import os
    from urlparse import urlparse
    ipport = str(ip) + ':' + str(port)
    output = urlparse(url)
    newurl = output[0]+"://"+ipport+output[2]
    domainname = output[1].split(':')[0]
    ret = os.popen("curl --connect-timeout 3 -s -I -H 'Host: %s' '%s'|head -1|awk '{print $2}'" %(domainname,newurl) ).read().strip('\n')
    return [domainname,ret]
