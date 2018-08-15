#!/bin/bash
ansible -m setup --tree /home/ubuntu/workspace/asset/out/ all
ansible-cmdb -p local_js=1 /home/ubuntu/workspace/asset/out/ > /home/ubuntu/workspace/ops/templates/overview.html
sed -i 's/<script type=\"text\/javascript\" charset=\"utf8\" src=\"file:\/\/\/usr\/lib\/ansible-cmdb\/ansiblecmdb\/data\/static\/\/js\/jquery-1.10.2.min.js\"><\/script>/<script src=\"\/static\/plugins\/jQuery\/jQuery-2.1.4.min.js\"><\/script>/g' /home/ubuntu/workspace/ops/templates/overview.html
sed -i 's/<script type=\"text\/javascript\" charset=\"utf8\" src=\"file:\/\/\/usr\/lib\/ansible-cmdb\/ansiblecmdb\/data\/static\/\/js\/jquery.dataTables.js\"><\/script>/<script src=\"\/static\/plugins\/datatables\/jquery.dataTables.min.js\"><\/script>/g' /home/ubuntu/workspace/ops/templates/overview.html

