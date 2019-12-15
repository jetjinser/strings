import requests


def shortlink(long_url: str) -> str:
    host = 'http://sina-t.cn'
    path = '/api'
    params = {'link': long_url}
    url = host + path

    r = requests.get(url, params=params)
    resp = r.text
    return resp


async def get_baidu_url(content: str) -> str:
    baidu_url = f'https://baidu.com/s?wd={content}'
    short_baidu_link = shortlink(baidu_url)
    return short_baidu_link


async def get_bing_url(content: str) -> str:
    bing_url = f'https://cn.bing.com/search?q={content}'
    short_bing_link = shortlink(bing_url)
    return short_bing_link


async def get_buhuibaidume_url(content: str) -> str:
    buhuibaidume_url = f'https://nbhbdm.cn/?s={content}'
    short_buhuibaidume_url = shortlink(buhuibaidume_url)
    return short_buhuibaidume_url
