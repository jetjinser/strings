import requests


async def get_random_hope():
    url = 'https://api.lolicon.app/setu/'
    resp = requests.get(url)
    hope = resp.json()
    hope_data = hope.get('data')[0]
    hope_url = hope_data.get('url')
    if hope_url:
        return hope_url
    else:
        return
