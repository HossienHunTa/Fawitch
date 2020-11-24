from fawitch.settings import HEADERS
from django.http import Http404
from collections import ChainMap
from requests_futures import sessions
import operator

def get_channel_id(name: str) -> str:
    session = sessions.FuturesSession()
    response = session.get(f'https://api.twitch.tv/kraken/users?login={name}', headers=HEADERS).result().json()
    return response['users'][0]['_id']


def get_channel_by_id(id: str) -> str:
    session = sessions.FuturesSession()
    return session.get(f'https://api.twitch.tv/kraken/channels/{id}', headers=HEADERS).result().json()

def get_stream_by_id(id: str) -> str:
    session = sessions.FuturesSession()
    response = session.get(f'https://api.twitch.tv/kraken/streams/{id}', headers=HEADERS).result().json()
    return response['stream']

def get_channels_id(l: list) -> list:
    listToStr = ','.join([str(i) for i in l]) 
    session = sessions.FuturesSession(max_workers=2)
    response = session.get(f'https://api.twitch.tv/kraken/users?login={listToStr}', headers=HEADERS).result().json()
    channel_id = [response['users'][i]['_id'] for i in range(0,response['_total'])]
    return channel_id

def get_streams_by_id(l: list) -> list:
    data = {}
    session = sessions.FuturesSession(max_workers=len(l))
    for n,i in enumerate(l):
        response = session.get(f'https://api.twitch.tv/kraken/streams/{i}', headers=HEADERS).result().json()
        new_data = {f'{n}':response['stream']}
        #data = ChainMap(data,new_data)
        data = ChainMap(new_data,data)
    return data

def three_top_viewer(stream: dict) -> dict:
    try:
        streamers = {}
        for n,i in stream.items():
            if i != None:
                streamer = {i['channel']['name']: i['viewers']}
                streamers = ChainMap(streamer,streamers)
        top_streams = {}
        top_viewe = max(streamers.items(), key=operator.itemgetter(1))
        new_stream = {top_viewe[0]:top_viewe[1]}
        top_streams = ChainMap(new_stream,top_streams)
        var = {key:value for key, value in streamers.items() if key != top_viewe[0]}
        try:
            for i in range(2):
                top_viewe = max(var.items(), key=operator.itemgetter(1))
                new_stream = {top_viewe[0]:top_viewe[1]}
                top_streams = ChainMap(new_stream,top_streams)
                var = {key:value for key, value in var.items() if key != top_viewe[0]}
        except:
            return top_streams
    except:
        return None
    
