import requests, re, random, time, json
from urllib import parse
from pprint import pprint
from bs4 import BeautifulSoup
from urllib.request import urlopen

data = {}

def daily():
    url = 'https://apiv3.shanbay.com/weapps/dailyquote/quote/'
    r = requests.get(url)
    respons_dict = r.json()
    return respons_dict['content'] + '\n' +respons_dict['translation']

def five():
    url = 'https://api.ooopn.com/yan/api.php'
    r = requests.get(url)
    respons_dict = r.json()
    return respons_dict['hitokoto']

def weather(city, date = 0):
    url = 'https://api.ooopn.com/weather/api.php?city={}'.format(city)
    try:
        r = requests.post(url)
        respons_dict = r.json()
        # pprint(respons_dict)
        u = respons_dict['data']['forecast'][date]
        i = respons_dict['data']['city'] + '  ' + u['type'] + '  ' + u['date'] + '\n' + '当前温度 ' \
            + respons_dict['data']['wendu'] + '℃' + '\n' + u['fengxiang'] + '  ' \
            + u['fengli'].lstrip('<![CDATA[').rstrip(']]>') + '\n' + '最高温度' + u['high'][3:] \
            + '\n' + '最低温度' + u['low'][3:] + '\n' + respons_dict['data']['ganmao']
    except KeyError:
        return 'error,无数据或语法错误'
    return i

def shortlink(arg = 'www.bing.com'):
    url = 'https://www.charfun.com/api/shorturl'
    payload = {'longurl': arg}
    response = requests.post(url, data=payload)
    return response.json()['shorturl']


def laji(arg):
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

def jielong(arg):
    url = 'https://chengyujielong.51240.com/{}__chengyujielong/'.format(parse.quote(arg))
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    a_soup = soup.find('a', {'href': re.compile('//chengyu.51240.com' + '.*?')})
    return a_soup.get_text()

def his():
    url = 'https://api.ooopn.com/history/api.php'
    r = requests.get(url)
    respons_dict = r.json()
    his = respons_dict['content']
    return random.choice(his)

def tim():
     return time.strftime('%Y%m%d', time.localtime(time.time()))

def today(arg = tim()):
    url = 'https://www.mxnzp.com/api/holiday/single/{}'.format(arg)
    r = requests.get(url)
    respons_dict = r.json()
    a = respons_dict['data']
    n = a['date'] + '  ' + '农历' + a['lunarCalendar'] + '  ' + a['solarTerms'] + '  ' + a['typeDes'] + '\n' \
        + '今年是' + a['yearTips'] + a['chineseZodiac'] + '年' + '  ' + '今日星座是' + a['constellation'] + '\n' \
        + '今天是这一年的第' + str(a['weekOfYear']) + '周 第' + str(a['dayOfYear']) + '天\n' + '宜 ' + a['suit'] + '\n忌 ' \
        + a['avoid']
    return n

def joke():
    url = 'https://www.mxnzp.com/api/jokes/list/random'
    r = requests.get(url)
    respons_dict = r.json()
    a = respons_dict['data']
    n = random.choice(a)
    return n['content']

def jokeen():
    url = 'http://api.icndb.com/jokes/random'
    r = requests.get(url)
    respons_dict = r.json()
    return respons_dict['value']['joke']

def news():
    url = 'http://c.m.163.com/nc/article/headline/T1348647853363/0-40.html'
    try:
        r = requests.get(url)
        respons_dict = r.json()
        b = respons_dict['T1348647853363']
        n = random.choice(b)
        try:
            if n['url_3w']:
                content = '【' + n['source'] + n['ptime'] + '】\n    ' + n['title'] + '\n    ' + n[
                    'digest'] + '...\n' + \
                          n['url_3w']
            else:
                content = '【' + n['source'] + n['ptime'] + '】\n    ' + n['title'] + '\n    ' + n[
                    'digest'] + '...\n' + \
                          '暂无数据'
        except:
            try:
                n_ = n['ads']
                content = '【' + n['source'] + n['ptime'] + '】\n    ' + n['title'] + '\n    ' + n[
                    'digest'] + '...\n' + \
                          n['url_3w']
            except:
                content = '错误,请重试'
    except:
        content = '错误,请重试'
    return content

def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    r = requests.get(url)
    respons_dict = r.json()
    a = respons_dict['bpi']
    return 'EUR   ' + a['EUR']['rate'] + '\nGBP   ' + a['GBP']['rate'] + '\nUSD   ' + a['USD']['rate']

def add(a, b):
    with open(r'C:\Users\cmdrj\PycharmProjects\xbot0.0.1.190706\venv\text.json', 'r', encoding='utf-8') as f:
        d = json.load(f)
    file = open('text.json', 'w', encoding='utf-8')
    count = d[-1]['number']
    data['number'] = count + 1
    data['name'] = a
    data['content'] = b
    datalist = [data]
    d.extend(datalist)
    json.dump(d, file, ensure_ascii=False, indent=4)
    return '添加成功' + ' 号{}'.format(str(data['number']))

def delete(number):
    with open(r'C:\Users\cmdrj\PycharmProjects\xbot0.0.1.190706\venv\text.json', 'r', encoding='utf-8') as f:
        d = json.load(f)
    d1 = str(d[number]['number'])
    d2 = d[number]['name']
    del d[number]
    file = open('text.json', 'w', encoding='utf-8')
    json.dump(d, file, ensure_ascii=False, indent=4)
    return '删除成功  号' + d1 + ' | ' + '《' + d2 + '》'

def bggo():
    with open(r'C:\Users\cmdrj\PycharmProjects\xbot0.0.1.190706\venv\text.json', 'r', encoding='utf-8') as f:
        d = json.load(f)
    bg = open('bg.json', 'w', encoding='utf-8')
    json.dump(d, bg, ensure_ascii=False, indent=4)
    return True

def book():
    with open(r'C:\Users\cmdrj\PycharmProjects\xbot0.0.1.190706\venv\text.json', 'r', encoding='utf-8') as f:
        d = json.load(f)
    b = random.choice(d)
    return b['content'] + '\n           --《' + b['name'] + '》 ' + '号{}'.format(str(b['number']))

def booklist():
    with open(r'C:\Users\cmdrj\PycharmProjects\xbot0.0.1.190706\venv\text.json', 'r', encoding='utf-8') as f:
        d = json.load(f)
    u = ''
    for i in d:
        u += '《' + i['name'] + '》' + i['content'][:8] + '...号' + str(i['number']) + '\n'
    return u

def setu():
    url = 'https://api.lolicon.app/setu/'
    r = requests.get(url)
    r = r.json()
    return r['url']

def gender(arg = 'peter'):
    url = 'https://api.genderize.io?name={}&country_id=US'.format(parse.quote(arg))
    try:
        response = requests.get(url)
        r = response.json()
        return '[{}] 性别推测为 '.format(arg) + r['gender'] + '\t正确概率 ' \
               + str(r['probability']) + '\n在美统计有 {} 人'.format(r['count'])
    except TypeError:
        return '无数据'

def ramdom_things():
    url = 'http://www.boredapi.com/api/activity/'
    response = requests.get(url)
    r = response.json()
    return '你可以:\n\t' + r['activity'] + '\n可行性:\n\t' + str(r['accessibility']) + '\n类型:\n\t' + r['type']

def QR(arg = 'www.bing.com'):
    url = 'https://qrtag.net/api/qr_4.png?url={}'.format(parse.quote(arg))
    return '[CQ: image, file = {}]'.format(url)

def get_image(user_id):
    url = 'http://q1.qlogo.cn/g?b=qq&nk={}&s=5'.format(user_id)
    response = requests.get(url)
    with open('demo.jpg', 'wb') as f:
        f.write(response.content)
    return './demo.jpg'

def tips_writer(args):
    with open(r'./data/tips.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    number0 = list(data[0].keys())[-1]
    number = int(number0) + 1

    data[0][str(number)] = args

    file = open(r'./data/tips.json', 'w', encoding='utf-8')
    json.dump(data, file, ensure_ascii=False, indent=4)

    return number

if __name__ == '__main__':
    print(ramdom_things())
