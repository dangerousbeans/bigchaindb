# -*- coding: utf-8 -*-
"""(Re)create the RethinkDB configuration file conf/bigchaindb.conf.
Start with conf/bigchaindb.conf.template
then append additional configuration settings (lines).
"""

from __future__ import unicode_literals
import os
import os.path
import shutil
from hostlist import hosts_dev

# cwd = current working directory
old_cwd = os.getcwd()
os.chdir('conf')
if os.path.isfile('bigchaindb.conf'):
    os.remove('bigchaindb.conf')

# Create the initial bigchaindb.conf using bigchaindb.conf.template
shutil.copy2('bigchaindb.conf.template', 'bigchaindb.conf')

# Append additional lines to bigchaindb.conf
with open('bigchaindb.conf', 'a') as f:
    f.write('## The host:port of a node that RethinkDB will connect to\n')
    for public_dns_name in hosts_dev:
        f.write('join=' + public_dns_name + ':29015\n')

os.chdir(old_cwd)

# Note: The original code by Andreas wrote a file with lines of the form
#       join=public_dns_name_0:29015
#       join=public_dns_name_1:29015
#       but it stopped about halfway through the list of public_dns_names
#       (publist). In principle, it's only strictly necessary to
#       have one join= line.
#       Maybe Andreas thought that more is better, but all is too much?
#       Below is Andreas' original code. -Troy
# lfile = open('add2dbconf', 'w')
# before = 'join='
# after = ':29015'
# lfile.write('## The host:port of a node that rethinkdb will connect to\n')
# for entry in range(0,int(len(publist)/2)):
#     lfile.write(before + publist[entry] + after + '\n')