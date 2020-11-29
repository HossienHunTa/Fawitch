import operator
from fawitch.settings import HEADERS
from collections import ChainMap
from requests_futures import sessions


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
        data = ChainMap(new_data,data)
    return data

def top_viewer(stream: dict, number: int) -> dict:
    top_viewer=[]
    streamers = {i['channel']['name']: i['viewers'] for n,i in stream.items() if i != None}
    if len(streamers.keys()) >= number:
        for i in range(number):
            streamer = max(streamers.keys(), key=operator.itemgetter(0))
            top_viewer.append(streamer)
            streamers.pop(streamer,None)
        return top_viewer
    elif len(streamers.keys()) <= 3:
        for i in range(len(streamers.keys())):
            streamer = max(streamers.keys(), key=operator.itemgetter(0))
            top_viewer.append(streamer)
            streamers.pop(streamer,None)
        return top_viewer
    else:
        return None
