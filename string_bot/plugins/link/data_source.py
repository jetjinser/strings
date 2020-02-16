import requests
from pyquery import PyQuery as pq


async def get_from_bili_av(av):
    url = f'https://api.bilibili.com/x/web-interface/view?aid={av}'

    resp = requests.get(url)

    data = resp.json().get('data')

    try:
        pic = data['pic']
        title = data['title'] + '_哔哩哔哩 (゜-゜)つロ 干杯~-bilibili'
        desc = data['desc']

        return {'pic': pic, 'title': title, 'desc': desc}
    except (KeyError, TypeError):
        return


async def get_from_bili_cv(cv):
    url = f'https://api.bilibili.com/x/article/viewinfo?id={cv}'

    resp = requests.get(url)

    date = resp.json().get('data')

    doc = pq(url='https://www.bilibili.com/read/cv4435286')
    p = doc('[name=description]')
    desc = p.attr('content')[:177]

    try:
        img = date['origin_image_urls'][0]
        title = date['title']

        return {'img': img, 'title': title, 'desc': desc}
    except (KeyError, TypeError):
        return


async def get_from_youtube():
    pass
    # TODO you2jinser 下次做
