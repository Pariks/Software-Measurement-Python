__author__ = 'Dell'
from pygithub3.services.repos import Repo


r = Repo()
r1 = r.list_contributors('poise', 'Python')
for page in r1:
    for contributors in page:
        print contributors