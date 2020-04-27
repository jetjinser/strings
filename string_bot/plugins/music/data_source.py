import requests

from typing import Union


async def search_song_163(keyword: str) -> Union[str, None]:
    url = f'http://127.0.0.1:3000/search?keywords={keyword}&limit=1'

    resp = requests.get(url)
    resp = resp.json()

    try:
        result = resp['result']['songs'][0]['id']
    except TypeError:
        return
    return result


async def search_song_qq(keyword: str) -> Union[str, None]:
    url = 'http://127.0.01:3300/search'

    params = {'key': keyword, 'pageSize': 1}

    resp = requests.get(url, params=params)
    resp = resp.json()

    try:
        result = resp['data']['list'][0]['songid']
    except TypeError:
        return
    return result
