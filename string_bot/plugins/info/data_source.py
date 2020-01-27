import requests
import random
import time


async def get_today_in_history():
    url = 'https://api.ooopn.com/history/api.php'
    r = requests.get(url)
    response_dict = r.json()
    history = response_dict['content']
    return random.choice(history)


async def get_one_sentence_a_day():
    url = 'https://apiv3.shanbay.com/weapps/dailyquote/quote/'
    r = requests.get(url)
    response_dict = r.json()
    formatted = response_dict['content'] + '\n' + response_dict['translation']
    return formatted


async def get_five_sayings():
    url = 'https://api.ooopn.com/yan/api.php'
    r = requests.get(url)
    response_dict = r.json()
    return response_dict['hitokoto']


async def get_garbage_classification(arg):
    host = 'https://www.98api.cn'
    path = '/api/rubbish.php'
    params = {'kw': arg}
    url = host + path

    r = requests.get(url, params=params)
    resp = r.json()

    if resp:
        return '\n'.join([i['key'] + ' 是 ' + i['type'] for i in resp])
    else:
        return 'buzhidao'


async def get_a_joke():
    url = 'https://www.mxnzp.com/api/jokes/list/random'
    r = requests.get(url)
    response_dict = r.json()
    data = response_dict['data']
    one_joke = random.choice(data)['content']
    return one_joke


async def get_news():
    url = 'http://c.m.163.com/nc/article/headline/T1348647853363/0-40.html'
    r = requests.get(url)
    response_dict = r.json()
    b = response_dict['T1348647853363']
    n = random.choice(b)
    content = '【' + n['source'] + n['ptime'] + '】\n    ' + n['title'] + '\n    ' + n[
        'digest'] + '...\n'
    if n['url_3w']:
        content += n['url_3w']
    else:
        content += '暂无数据'
    return content


async def get_weather_of_city(city: str, date: str = None) -> str:
    if date == '今天' or not date:
        date = 0
    elif date == '明天':
        date = 1
    elif date == '后天':
        date = 2
    elif date == '大后天':
        date = 3
    elif date == '大大后天':
        date = 4
    url = f'https://api.ooopn.com/weather/api.php?city={city}'
    try:
        r = requests.post(url)
        resp = r.json()
        dialect = resp['data']['forecast'][date]
        formatted = (
                resp['data']['city'] + '  ' + dialect['type'] + '  ' + dialect['date'] + '\n' + '当前温度 '
                + resp['data']['wendu'] + '℃' + '\n' + dialect['fengxiang'] + '  '
                + dialect['fengli'].lstrip('<![CDATA[').rstrip(']]>') + '\n' + '最高温度' + dialect['high'][3:]
                + '\n' + '最低温度' + dialect['low'][3:] + '\n' +
                resp['data']['ganmao']
        )
    except KeyError:
        return 'error,无数据或语法错误'
    return formatted


async def get_daily_zhihu() -> str:
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/79.0.3945.79 Safari/537.36'}

    resp = requests.get('https://news-at.zhihu.com/api/4/stories/latest', headers=header)

    resp = resp.json()

    stories = resp['stories']
    top_stories = resp['top_stories']

    all_stories = stories + top_stories
    data = random.choice(all_stories)

    data = data['title'] + '\n' + data['hint'] + '\n' + data['url']

    return data


async def get_gank() -> str:
    resp = requests.get('http://gank.io/api/random/data/all/1')

    resp = resp.json()
    resp = resp['results'][0]

    data = resp['type'] + ' / ' + resp['desc'] + ' / ' + resp['who'] + '\n' + resp['publishedAt'] + '\n' + resp['url']

    return data


async def get_steam_sale() -> str:
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/79.0.3945.79 Safari/537.36'}

    resp = requests.get('http://www.vgtime.com/steam/steamapi.php?saleType=PROMOTIONAL+PRICE', headers=header)

    resp = resp.json()

    # count = resp['count']
    data = resp['data']

    detail = random.choice(data)
    msg = (
            detail['name'] + '   ' + detail['saleRate'] + '\n原价: ￥' + detail['oldPrice'] + '   现价: ￥' +
            detail['nowPrice'] + '\n平台: ' + detail['platform'] + '\n' + detail['rateInfo'].replace('<br>', '  ') +
            f'https://store.steampowered.com/app/{detail["aid"]}'
    )

    return msg


async def get_calendar() -> str:
    date = time.strftime('%Y%m%d', time.localtime(time.time()))
    url = f'https://www.mxnzp.com/api/holiday/single/{date}'
    r = requests.get(url)
    response_dict = r.json()
    dialect = response_dict['data']
    formatted = (
            dialect['date'] + '  ' + '农历' + dialect['lunarCalendar'] + '  ' + dialect['solarTerms'] + '  ' +
            dialect['typeDes'] + '\n' + '今年是' + dialect['yearTips'] + dialect['chineseZodiac'] + '年' + '  ' +
            '今日星座是' + dialect['constellation'] + '\n' + '今天是本年度第' + str(dialect['weekOfYear']) +
            '周 第' + str(dialect['dayOfYear']) + '天\n' + '宜 ' + dialect['suit'] + '\n忌 ' + dialect['avoid']
    )
    return formatted


async def get_isbn_book(isbn):
    url = f'https://api.isoyu.com/books/isbn/?isbn={isbn}'
    resp = requests.get(url)
    data = resp.json()
    try:
        if data['page'] != '未知':
            msg = (
                    '《' + data['title'] + '》  ' + data['description'] + '\n作者：' + data['author'][0]['name'] + '  ' +
                    data['designed'] + '\n' + data['page'][1:] + '页 ' + data['price'] + ' ' + data['published']
            )
        else:
            msg = (
                    '《' + data['title'] + '》  ' + data['description'] + '\n作者：' + data['author'][0]['name'] + '  ' +
                    data['designed'] + '\n' + '页数未知' + data['price'] + ' ' + data['published']
            )
    except TypeError:
        msg = '无数据，请确认ISBN正确'

    return msg

# 下次一定
# async def get_steam_sale_list() -> str:
#     header = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                       'Chrome/79.0.3945.79 Safari/537.36'}
#
#     resp = requests.get('http://www.vgtime.com/steam/steamapi.php?saleType=PROMOTIONAL+PRICE', headers=header)
#
#     resp = resp.json()
#
#     # count = resp['count']
#     data = resp['data']
#
#     msg = '\n'
#     detail = random.choice(data, seq=3)
#     formatted = (
#           detail['name'] + '   ' + detail['saleRate'] + '\n原价: ￥' + detail['oldPrice'] + '   现价: ￥' +
#           detail['nowPrice'] + '\n平台: ' + detail['platform'] + '\n' + detail['rateInfo'].replace('<br>', '  ') +
#           f'https://store.steampowered.com/app/{detail["aid"]}'
#     )
#     msg.join(formatted)
#
#     print(msg)
#     return str(msg)
