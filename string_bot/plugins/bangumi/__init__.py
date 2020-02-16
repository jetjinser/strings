from nonebot import CommandGroup, CommandSession
from .data_source import *

__plugin_name__ = '新番'
__plugin_usage__ = r"""获取bili新番时间表

指令: 新番 / 新番时间表"""

cg = CommandGroup('new_animation', only_to_me=False)


@cg.command('新番', aliases=['新番时间表', '新番'])
async def new_animation(session: CommandSession):
    q_type = session.get('type', prompt='⌘国创or番剧？⌘')
    result_str = ''
    q_type_int = 0 if q_type.find("国创") > -1 else 1
    time_line = await get_time_line(q_type_int)
    if len(time_line) == 0:
        result_str = '今日无更新'
    else:
        for t in time_line:
            result_str = result_str + t['title'] + t['index'] + '\n' \
                         + t['time'] + '更新\n' + t['link'] + '\n'

    await session.send(result_str)


@new_animation.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['type'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('⌘国创or番剧？⌘')
    session.state[session.current_key] = stripped_arg
