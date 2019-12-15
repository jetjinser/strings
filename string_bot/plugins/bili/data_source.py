import requests
import json
import time


async def get_time_line(a_type):
    # count = 1
    type_str = "cn" if a_type == 0 else "global"
    res = requests.get('https://bangumi.bilibili.com/web_api/timeline_' + type_str)
    article_dict = json.loads(res.text)
    # # get date
    # month = time.localtime()[1]
    # day = time.localtime()[2]
    # day_of_week = time.localtime()[6]
    time_lines = article_dict['result']
    today_line = []
    result_line = []
    for line in time_lines:
        if line['is_today'] == 1:
            today_line = line['seasons']
    if len(today_line) > 0:
        result_line = [{
            'title': s['title'],
            'link': 'https://www.bilibili.com/bangumi/play/ss' + str(s['season_id']),
            'time': s['pub_time'],
            'index': s['pub_index'] if s.get('pub_index') is not None else "",
        } for s in today_line]

    return result_line
