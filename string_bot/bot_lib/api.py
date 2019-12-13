from bot_lib.shortlink import shortlink
import requests
import time
import random
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib import parse


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
        formatted = resp['data']['city'] + '  ' + dialect['type'] + '  ' + dialect['date'] + '\n' + '当前温度 ' \
                    + resp['data']['wendu'] + '℃' + '\n' + dialect['fengxiang'] + '  ' \
                    + dialect['fengli'].lstrip('<![CDATA[').rstrip(']]>') + '\n' + '最高温度' + dialect['high'][3:] \
                    + '\n' + '最低温度' + dialect['low'][3:] + '\n' + \
                    resp['data']['ganmao']
    except KeyError:
        return 'error,无数据或语法错误'
    return formatted


async def get_baidu_url(content: str) -> str:
    baidu_url = f'https://baidu.com/s?wd={content}'
    short_baidu_link = shortlink(baidu_url)
    return short_baidu_link


async def get_bing_url(content: str) -> str:
    bing_url = f'https://cn.bing.com/search?q={content}'
    short_bing_link = shortlink(bing_url)
    return short_bing_link


async def get_calendar(date: str = time.strftime('%Y%m%d', time.localtime(time.time()))) -> str:
    url = f'https://www.mxnzp.com/api/holiday/single/{date}'
    r = requests.get(url)
    response_dict = r.json()
    dialect = response_dict['data']
    formatted = dialect['date'] + '  ' + '农历' + dialect['lunarCalendar'] + '  ' + dialect['solarTerms'] + '  ' + \
                dialect['typeDes'] + '\n' + '今年是' + dialect['yearTips'] + dialect[
                    'chineseZodiac'] + '年' + '  ' + '今日星座是' + dialect['constellation'] + '\n' + '今天是本年度第' + str(
        dialect['weekOfYear']) + '周 第' + str(dialect['dayOfYear']) + '天\n' + '宜 ' + dialect['suit'] + \
                '\n忌 ' + dialect['avoid']
    return formatted


async def get_random_things() -> str:
    url = 'http://www.boredapi.com/api/activity/'
    response = requests.get(url)
    r = response.json()
    formatted = '你可以:\n\t' + r['activity'] + '\n可行性:\n\t' + str(r['accessibility']) + '\n类型:\n\t' + r['type']
    return formatted


async def get_image(user_id: str) -> str:
    url = f'http://q1.qlogo.cn/g?b=qq&nk={user_id}&s=5'
    response = requests.get(url)
    with open('./data/demo.jpg', 'wb') as f:
        f.write(response.content)
    return './data/demo.jpg'


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
    url = 'https://lajifenleiapp.com/sk/{}'.format(parse.quote(arg))
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    one_soup = soup.find_all('span', {'style': 'color:#643f30'})
    two_soup = soup.find_all('span', {'style': 'color:#00447b'})
    three_soup = soup.find_all('span', {'style': '#2e2a2b'})
    four_soup = soup.find_all('span', {'style': 'color:#e23322'})
    if one_soup + two_soup + three_soup + four_soup:
        for i in one_soup + two_soup + three_soup + four_soup:
            return i.get_text()
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
