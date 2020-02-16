from nonebot import CommandGroup, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand

from .data_source import *

import re

__plugin_name__ = 'link'
__plugin_usage__ = r"""根据链接自动返回相关信息

目前支持: bilibili的av/cv号"""

cg = CommandGroup('link', only_to_me=False)


@cg.command('bili_av')
async def bili_av(session: CommandSession):
    av = session.get('av')
    url = f'https://www.bilibili.com/video/av{av}'

    av_dict = await get_from_bili_av(av)

    if av_dict:
        pic = av_dict.get('pic')
        title = av_dict.get('title')
        desc = av_dict.get('desc')

        await session.send(f'[CQ:share,url={url},title={title},content={desc},image={pic}]')


@cg.command('bili_cv')
async def bili_cv(session: CommandSession):
    cv = session.get('cv')
    url = f'https://www.bilibili.com/read/cv{cv}'

    cv_dict = await get_from_bili_cv(cv)

    if cv_dict:
        img = cv_dict.get('img')
        title = cv_dict.get('title')
        desc = cv_dict.get('desc')

        await session.send(f'[CQ:share,url={url},title={title},content={desc},image={img}]')


@on_natural_language(only_to_me=False)
async def _(session: NLPSession):
    stripped_msg = session.msg_text.strip()

    av_pattern = re.compile(r'^.*av(\d{3,8}).*$', re.I)
    cv_pattern = re.compile(r'^.*cv(\d{3,7}).*$', re.I)

    av_match = av_pattern.match(stripped_msg)
    cv_match = cv_pattern.match(stripped_msg)

    if av_match:
        return IntentCommand(100, ('link', 'bili_av'), args={'av': av_match.group(1).lower()})
    elif cv_match:
        return IntentCommand(100, ('link', 'bili_cv'), args={'cv': cv_match.group(1).lower()})
    else:
        return
