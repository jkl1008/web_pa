import requests
import webbrowser
import time
api = 'https://api.github.com/users/kennethreitz/starred'
last_list = None
all_info = requests.get(api).json()
cur_list = []
for info in all_info:
    cur_list.append(info['id'])
print(cur_list)
while True:
    if not last_list:
        last_list = cur_list

    for info in all_info:
        if not info['id'] in last_list:
            repo_name = info['name']
            owner = info['owner']['login']
            web_page = 'https://github.com/' + owner +'/' + repo_name
            webbrowser.open(web_page)
    time.sleep(600)