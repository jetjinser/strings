import requests

from typing import Union


async def search_song(keyword, *, platform, search_type='song') -> Union[str, None]:
    url = f'http://111.229.83.234:3000/search?keywords={keyword}&limit=1'

    resp = requests.get(url)
    resp = resp.json()

    try:
        result = resp['result']['songs'][0]['id']
    except TypeError:
        return
    return result
