import time,requests

def push_it(message):
    api = 'https://api.pushover.net/1/messages.json/'
    data = {
        'token':'akbucw54u98r6c7emy8ap1re91gbg5',
        'user':'upnp62gkug98tkvhctghouubebg2yz',
        'message':message
    }
    print(api)
    print(data)
    requests.post(api,data)

def get_project(lask_week,topic):
    api = 'https://api.github.com/search/repositories?q='
    query_created = 'created:>' + lask_week
    query_topic = 'topic:' + topic
    r = requests.get(api + query_created + '+' + query_topic)
    return r.json()['items']

last_week = '2018-09-03T00:00:00Z'
topic = 'java'
result = []

while True:
    project_list = get_project(last_week,topic)
    for p in project_list:
        stars = p['stargazers_count']
        if stars > 200 and not p['html_url'] in result:
            message = 'The Project '+ p['name'] +'is qualified  ' + 'URL :' + p['html_url']
            push_it(message)
            result.append(p['html_url'])
    time.sleep(800)

