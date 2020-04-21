import requests


def shortlink(long_url: str) -> str:
    host = 'https://www.98api.cn'
    path = '/api/sinaDwz.php'
    params = {'url': long_url}
    url = host + path

    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
            ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }

    r = requests.get(url, params=params, headers=headers, verify=False)
    resp = r.json()
    return resp['short_url']


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
