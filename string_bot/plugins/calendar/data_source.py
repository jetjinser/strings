import requests
import time


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
