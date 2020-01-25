import requests


async def to_isearch_pixivic(original_image_url, boo: bool) -> str:
    url = 'https://api.pixivic.com/similarityImages'

    params = {'imageUrl': original_image_url}

    resp = requests.get(url, params=params)

    try:
        data = resp.json()['data']
        first_img = data[0]

        artistPreView = first_img['artistPreView']
        name = artistPreView['name']
        id = artistPreView['id']

        img_id = first_img['id']

        img_url = first_img['imageUrls'][0]['original']

        xrestrict = first_img['xrestrict']

        if not xrestrict:
            img_url = img_url.replace('ximg.net', 'ixiv.cat')
            if boo:
                msg = f'[CQ:image,file={img_url}]' + '\n图片id：' + str(img_id) + '\n作者：' + name + '    作者id：' + str(id)
            else:
                msg = img_url + '\n图片id：' + str(img_id) + '\n作者：' + name + '    作者id：' + str(id)
        else:
            msg = '搜索结果含r-18内容, 暂不予显示'
    except (IndexError, KeyError):
        if resp.json().get('error'):
            msg = resp.json().get('error')
        else:
            msg = '无数据'
    return msg
