import requests


def shortlink(long_url: str) -> str:
    host = 'http://sina-t.cn'
    path = '/api'
    params = {'link': long_url}
    url = host + path

    r = requests.get(url, params=params)
    resp = r.text
    return resp
