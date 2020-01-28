from nonebot import CommandGroup, CommandSession
from .data_source import *
from urllib import parse

__plugin_name__ = '搜索'
__plugin_usage__ = r"""有关搜索

指令: 百度 / bing / 不会百度么"""

cg = CommandGroup('search', only_to_me=False)


@cg.command('baidu', aliases=['百度', '百度一下'])
async def search_baidu(session: CommandSession):
    content = session.get('content', prompt='你想百度什么?')
    msg = await get_baidu_url(content)
    await session.send(str(msg))


@cg.command('bing', aliases=['bing', '必应'])
async def search_bing(session: CommandSession):
    content = session.get('content', prompt='你想bing什么?')
    msg = await get_bing_url(content)
    await session.send(str(msg))


@cg.command('buhuibaidume', aliases=['不会百度吗', '不会百度么'])
async def search_buhuibaidume(session: CommandSession):
    content = session.get('content', prompt='你想百度什么?')
    msg = await get_buhuibaidume_url(content)
    await session.send(str(msg))


# 搜索的参数处理器
@search_bing.args_parser
@search_buhuibaidume.args_parser
@search_baidu.args_parser
async def _(session: CommandSession):
    stripped_arg = parse.quote(session.current_arg_text.strip())

    if session.is_first_run:
        if stripped_arg:
            session.state['content'] = parse.quote(session.current_arg_text)
        return

    if not stripped_arg:
        session.pause('要查询的内容不能为空')

    session.state[session.current_key] = stripped_arg
