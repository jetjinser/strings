from nonebot import on_command, CommandSession
from pyquery import PyQuery as pq
import requests,json
import time

@on_command('新番', aliases=('新番时间表'))
async def _(session: CommandSession):
    q_type = session.get('type', prompt='国创or番剧？')
    result_str = ''
    q_type_int = 0 if q_type.find("国创") > -1 else 1
    time_line = await get_time_line(q_type_int)
    if len(time_line) == 0:
        result_str = '今日无更新'
    else:
        for t in time_line:
            result_str = result_str + t['title'] + t['index'] + '\n' \
            + t['time'] +  '更新\n' + t['link'] + '\n'

    # 向用户发送天气预报
    await session.send(result_str)

async def get_time_line(a_type):
    count = 1
    type_str = "cn" if a_type == 0 else "global"
    res = requests.get('https://bangumi.bilibili.com/web_api/timeline_'+type_str)
    article_dict = json.loads(res.text)
    # get date
    month = time.localtime()[1]
    day = time.localtime()[2]
    day_of_week = time.localtime()[6]
    time_lines = article_dict['result']
    today_line = []
    result_line = []
    for line in time_lines:
        if line['is_today'] == 1:
            today_line = line['seasons']
    if len(today_line) > 0:
        result_line = [{
        'title': s['title'],
        'link':'https://www.bilibili.com/bangumi/play/ss' + str(s['season_id']),
        'time': s['pub_time'],
        'index':s['pub_index'] if s.get('pub_index') is not None else "",
        } for s in today_line]
    
    return result_line

# args_parser 装饰器将函数声明为 weather 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@_.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            session.state['type'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('国创or番剧？')
    session.state[session.current_key] = stripped_arg