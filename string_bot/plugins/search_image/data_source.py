import requests


async def to_isearch_pixivic(original_image_url, boo: bool) -> str:
    url = 'https://api.pixivic.com/similarityImages'

    params = {'imageUrl': original_image_url}

    resp = requests.get(url, params=params)

    try:
        data = resp.json()['data']
        first_img = data[0]

        title = data['title']

        artistPreView = first_img['artistPreView']
        name = artistPreView['name']
        id = artistPreView['id']

        img_id = first_img['id']

        img_url = first_img['imageUrls'][0]['original']

        xrestrict = first_img['xrestrict']

        if not xrestrict:
            img_url = img_url.replace('ximg.net', 'ixiv.cat')
            img_url_1 = img_url.replace('.jpg', '-1.jpg')

            msg = title + '\n图片id：' + str(img_id) + '\n作者：' + name + '    作者id：' + str(id)
            if boo:
                msg = f'[CQ:image,file={img_url}][CQ:image,file={img_url_1}]' + msg
            else:
                msg = img_url + msg
        else:
            msg = '搜索结果含r-18内容, 暂不予显示'
    except (IndexError, KeyError):
        if resp.json().get('error'):
            msg = resp.json().get('error')
        else:
            msg = '无数据'
    except TypeError:
        msg = resp.json()
    return msg


async def to_isearch_trace(original_image_url, boo: bool) -> str:
    url = 'https://trace.moe/api/search'

    params = {'url': original_image_url}

    resp = requests.get(url, params)

    try:
        data = resp.json()['docs'][0]

        season = data['season']
        similarity = '%.2f%%' % (data['similarity'] * 100)

        title_native = data['title_native']

        is_adult = data['is_adult']

        mal_id = data['mal_id']

        img_id, site_url = await _get_anime_detail(mal_id)

        msg = '\n' + title_native + '\n' + season + '\n相似度: ' + str(
            similarity) + '\n成人向: ' + str(is_adult) + '\n' + site_url
        if boo:
            msg = f'[CQ:image,file={img_id}]' + msg
        else:
            msg = img_id + msg

    except (IndexError, KeyError):
        msg = '无数据'

    return msg


async def to_isearch_saucenao(original_image_url, boo: bool):
    url = 'https://saucenao.com/search.php'

    SAUCENAO_API_KEY = 'c7d48a9ddf52b984616b9ce40feec69f7b387854'

    params = {'output_type': 2, 'api_key': SAUCENAO_API_KEY, 'testmode': 1, 'db': 999,
              'numres': 5, 'url': original_image_url}

    resp = requests.get(url, params)
    results = resp.json()['results'][0]

    header = results['header']
    similarity = header['similarity']

    data = results['data']
    title = data.get('title')
    ext_url = data['ext_urls'][0]

    pixiv_id = data.get('pixiv_id')
    if pixiv_id:
        img_url = f'https://pixiv.cat/{pixiv_id}.jpg' if is_active(
            f'https://pixiv.cat/{pixiv_id}.jpg') else '结果图片不止一张, 无法显示\n'
        member_name = data['member_name']
        member_id = data['member_id']
        msg = '\n' + title + '\n图片id：' + str(pixiv_id) + '\n相似度：' + str(similarity) + \
              '%\n作者：' + member_name + '    作者id：' + str(member_id) + '\n' + ext_url
        if boo:
            msg = f'[CQ:image,file={img_url}]' + msg
        else:
            msg = img_url + msg
    else:
        try:
            img_url = header['thumbnail']
            msg = '\n' + title + '\n相似度：' + str(similarity) + '%\n' + ext_url
            if boo:
                msg = f'[CQ:image,file={img_url}]' + msg if is_active(
                    img_url) else '结果图片不止一张, 无法显示\n'
            else:
                msg = img_url + msg
        except TypeError:
            pixiv_id = data['source'].split('/')[-1]
            img_url = f'https://pixiv.cat/{pixiv_id}.jpg' if is_active(
                f'https://pixiv.cat/{pixiv_id}.jpg') else '结果图片不止一张, 无法显示\n'
            msg = '\n' + '作者 ' + data['creator'] + '\nmaterial ' + data['material'] + '\n' + data['ext_urls'][0]
            if boo:
                msg = f'[CQ:image,file={img_url}]' + msg
            else:
                msg = img_url + msg

    return msg


async def _get_anime_detail(anilist_id):
    url = 'https://trace.moe/info'

    params = {'anilist_id': anilist_id}
    try:
        resp = requests.get(url, params)
        data = resp.json()[0]
        img_id = data['coverImage']['large']
        site_url = data['siteUrl']
    except TypeError:
        img_id = 'https://jinser.xyz/image/undefined.jpg'
        site_url = '网址暂无数据'

    return img_id, site_url


def is_active(url: str) -> bool:
    """
    404 or not
    :param url: url
    :return: True: is active False: is not active
    """
    resp = requests.head(url)
    if resp.status_code == 200:
        return True
    else:
        return False
