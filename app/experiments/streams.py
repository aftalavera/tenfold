import requests
import json
from datetime import datetime, timedelta

session = requests.Session()
session.get('http://m-api.ustvnow.com/gtv/1/live/login?username=aftalavera%40sdipr.net&password=talavera')
response = session.get('http://m-api.ustvnow.com/gtv/1/live/channelguide', params={'token': session.cookies['token']})
data = json.loads(response.content)

streams = set()

for c in data['results']:
    streams.add(c['stream'])

print str(datetime.now() - timedelta(hours=6)) + " (" + session.cookies['token'] + ")"

for s in streams:
    print s
