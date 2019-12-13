from nonebot import CommandGroup, CommandSession
from bot_lib.api import get_baidu_url, get_bing_url
from urllib import parse

__plugin_name__ = '搜索'

cg = CommandGroup('search', only_to_me=False)


@cg.command('baidu', aliases=['百度', '百度一下', '不会百度吗', '不会百度么'])
async def search_baidu(session: CommandSession):
    content = session.get('content', prompt='你想百度什么?')
    msg = await get_baidu_url(content)
    await session.send(str(msg))


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


@cg.command('bing', aliases=['bing', '必应'])
async def search_bing(session: CommandSession):
    content = session.get('content', prompt='你想bing什么?')
    msg = await get_bing_url(content)
    await session.send(str(msg))


@search_bing.args_parser
async def _(session: CommandSession):
    stripped_arg = parse.quote(session.current_arg_text.strip())

    if session.is_first_run:
        if stripped_arg:
            session.state['content'] = parse.quote(session.current_arg_text)
        return

    if not stripped_arg:
        session.pause('要查询的内容不能为空')

    session.state[session.current_key] = stripped_arg
