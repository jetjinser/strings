from string_bot.bot_lib.shortlink import shortlink
import requests
import time


async def get_weather_of_city(city: str, date: str) -> str:
    if date == '明天':
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


# 出错的函数
def get_image(user_id: str) -> str:
    url = f'http://q1.qlogo.cn/g?b=qq&nk={user_id}&s=5'
    response = requests.get(url)
    with open('../data/demo.jpg', 'wb') as f:
        f.write(response.content)
    return '../data/demo.jpg'


if __name__ == '__main__':
    image = get_image('2301583973')
