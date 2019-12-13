from nonebot import on_command, CommandSession
from pyquery import PyQuery as pq
import requests,json
import random

@on_command('scp', aliases=('SCP','Scp'))
async def scp(session: CommandSession):
    q_type = session.get('type', prompt='最近翻译or最近原创or随机？')
    result_str = ''
    if q_type.find("原创") > -1:
    	q_type_int = 0
    elif q_type.find("翻译") > -1:
    	q_type_int = 1
    elif q_type.find("随机") > -1:
    	q_type_int = 2
    else:
    	q_type_int = -1
    if q_type_int == 0 or q_type_int == 1:
    	scp_list = await get_latest_article(q_type_int,1)
    	for s in scp_list[:5]:
    		result_str = result_str + s['title'] + '\nhttp://scp-wiki-cn.wikidot.com' + s['link'] + '\n创建于' \
    		+ s['created_time'] + '\n评分' + s['rank'] + '\n'
    elif q_type_int == 2:
    	scp = await get_scp_daily(random.randint(1,241))
    	result_str = scp['title'] + '\n' + scp['summary'] + '\n' + scp['link']
    # 向用户发送天气预报
    await session.send(result_str)

async def get_latest_article(page_type, page_index):
    article_list = []
    type_str = "created-cn" if page_type == 0 else "created-translated"
    # doc = pq('http://scp-wiki-cn.wikidot.com/most-recently-created-cn/p/1')
    link_str = 'http://scp-wiki-cn.wikidot.com/most-recently-%s/p/%s' % (type_str, page_index)
    doc = pq(link_str)
    for i in list(doc('table>tr').items())[2:]:
        new_article = {}
        info_list = list(i('td').items())
        new_article['title'] = info_list[0]('a').text()
        new_article['link'] = info_list[0]('a').attr('href')
        new_article['created_time'] = info_list[1]('span').text()
        new_article['rank'] = info_list[2].text()
        article_list.append(new_article)
    return article_list

async def get_scp_daily(index):
    count = 1
    res = requests.get('https://api.bilibili.com/x/space/article?mid=872507&pn=%s&ps=%s&sort=publish_time' % (index, count))
    article_dict = json.loads(res.text)
    first_article = article_dict['data']['articles'][0]
    link = 'https://www.bilibili.com/read/cv' + str(first_article['id'])
    title = first_article['title']
    full_summary = first_article['summary']
    summary = full_summary
    banner_url = first_article['banner_url']
    return {
            'title': title,
            'link': link,
            'summary': summary,
            'banner': banner_url
            }

# args_parser 装饰器将函数声明为 weather 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@scp.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            session.state['type'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('最近翻译or最近原创or随机？')
    session.state[session.current_key] = stripped_arg
