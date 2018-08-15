#!/bin/sh
/usr/local/bin/inotifywait -mrq --timefmt '%Y%m%d%H%M%S' --format '%T,%w%f,%e' -e modify,delete,create,attrib /home/ubuntu/workspace/upload/1/ | while read FL
do
#printf ${FL} | /bin/mail -s "file_test" nba0096@163.com
#echo "_"
echo ${FL} >> /home/ubuntu/workspace/upload/inotify.log
done

#做成开机启动
chmod u+x /tmp/mon.sh
echo "nohup /bin/bash /tmp/mon.sh &" >> /etc/rc.d/rc.local
nohup /bin/bash /tmp/mon.sh &