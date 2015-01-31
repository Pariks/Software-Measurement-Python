__author__ = 'Dell'
import requests, os,time
from bs4 import BeautifulSoup

f = open('bug_config','r+')

i = 0
lst = [' ']
url_ls = [' ']
sp_url_ls = [' ']
lst = f.readlines()
for ls in lst:
    sp_url_ls = ls.split('=')
    for dir in sp_url_ls:
       if 'root_directory' in dir:
           direct = sp_url_ls[1]
       if 'url' in dir:
           sting = sp_url_ls[1]
       if 'project_tag' in dir:
           project_tag = sp_url_ls[1]
       if 'bug_start' in dir:
           start_val = sp_url_ls[1]
       if 'bug_end' in dir:
           end_val = sp_url_ls[1]
       if 'max_timeout_secs' in dir:
           time_out = sp_url_ls[1]





print '\nDownloading Bugs..\n'
print 'You have wait for Time_out : %s sec after every bug\n' %(time_out)

os.chdir(direct)

for i in range(int(start_val),int(end_val)):
    file_name = 'bug' + str(i) + '.html'
    print file_name
    bug_url = sting.replace('\n','')+project_tag.replace('\n','')+'-'+str(i).replace('\n','')
    f1 = open(file_name, 'w')
    r = requests.get(bug_url)
    soup = BeautifulSoup(r.content)
    f1.write(str(soup))
    f1.close()
    time.sleep(time_out)

print 'Bugs in range[%s, %s] downloaded sucessfully' %(start_val,end_val)

f.close()