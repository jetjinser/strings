from nonebot import CommandGroup, CommandSession
from .data_source import *
import random

__plugin_name__ = 'scp'
__plugin_usage__ = r"""scp查询

指令: scp"""

cg = CommandGroup('scp', only_to_me=False)


@cg.command('scp', aliases=['SCP', 'Scp', 'scp'])
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
        try:
            assert int(q_type)

            if len(q_type) == 1:
                q_type = '00' + q_type
            elif len(q_type) == 2:
                q_type = '0' + q_type

            msg = await get_scp_by_num(q_type)
            session.finish(msg)
            return
        except ValueError:
            q_type_int = -1

    if q_type_int == 0 or q_type_int == 1:
        scp_list = await get_latest_article(q_type_int, 1)
        for s in scp_list[:5]:
            result_str = result_str + s['title'] + '\nhttp://scp-wiki-cn.wikidot.com' + s['link'] + '\n创建于' \
                         + s['created_time'] + '\n评分' + s['rank'] + '\n'
    elif q_type_int == 2:
        scp = await get_scp_daily(random.randint(1, 241))
        result_str = scp['title'] + '\n' + scp['summary'] + '\n' + scp['link']

    await session.send(result_str)


@scp.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['type'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('最近翻译or最近原创or随机？')
    session.state[session.current_key] = stripped_arg
