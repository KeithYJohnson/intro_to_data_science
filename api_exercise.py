import json
import requests

def api_get_request(url):
    raw_data = requests.get(url).text
    json_data = json.loads(raw_data)

    artists = json_data[u'topartists'][u'artist']
    for artist in artists:
        if artist[u'@attr'][u'rank'] == u'1':
            top_artist =  artist

api_get_request('http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=YOURKEY&format=json')
