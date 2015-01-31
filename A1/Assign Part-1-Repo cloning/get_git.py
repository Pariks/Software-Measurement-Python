__author__ = 'Dell'
import requests,os
from bs4 import BeautifulSoup


f = open('git_config','r+')



lst = [' ']
url_ls = [' ']
sp_url_ls = [' ']
lst = f.readlines()
for ls in lst:
    sp_url_ls = ls.split('=')
    for dir in sp_url_ls:
       if 'root_directory' in dir:
            direct = sp_url_ls[1]
       if 'https://f-droid.org' in dir:
            sting = dir
       if 'https://github.com' in dir:
           sting1 = dir




if 'https://f-droid.org' in sting:
     r = requests.get(sting)
     soup = BeautifulSoup(r.content)
     get_data_4m_f_droid = soup.find_all('a')
     for link in get_data_4m_f_droid:
        git_repo = link.text
        comad = 'git clone'
        os.chdir(direct)
        if 'https://github.com' in git_repo:
            if 'issues' in git_repo:
                git_repo = git_repo[:-7]
                print git_repo
                comad = comad + '\t' + git_repo
                os.system(comad)



print 'Cloning repos from github.com \n It may take while to initiate and clone..'
os.chdir(direct)

if 'https://github.com' in sting1:
    r = requests.get(sting1)
    soup = BeautifulSoup(r.content)
    get_data = soup.find_all('h3',{'class':'repo-list-name'})
    for link in get_data:
        a_link = link.find_all('a')
        comad = 'git clone'
        for href_link in a_link:
            git_repo_name = href_link.get('href')
            git_repo_url = 'https://github.com' + git_repo_name
            comad = comad + '\t' + git_repo_url
            os.system(comad)

print 'cloning sucessfully done'

f.close()






