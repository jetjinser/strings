import requests


async def search_song(keyword, platform, search_type='song'):
    path = f'https://v1.itooi.cn/{platform}/search'
    args = f'?keyword={keyword}&pageSize=10&page=0&type={search_type}'
    url = path + args

    resp = requests.get(url)
    resp = resp.json()

    try:
        if platform == 'netease':
            song_data = resp['data']['songs'][0]
            song_id = song_data['id']
        elif platform == 'tencent':
            song_data = resp['data']['list'][0]
            song_id = song_data['songid']
        else:
            song_id = None
        return song_id
    except KeyError:
        return
