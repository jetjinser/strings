from nonebot import on_command, CommandSession
from nonebot.permission import *
from aiocqhttp import ActionFailed


__plugin_name__ = 'send'
__plugin_usage__ = r"""不开放功能
"""


@on_command('send_private', aliases=['send_private', 'say_private', '私发'], permission=SUPERUSER)
async def send_private(session: CommandSession):
    user = session.get('user', prompt='发给谁')
    msg = session.get('msg', prompt='发什么')
    bot = session.bot
    try:
        await bot.send_private_msg(user_id=user, message=msg)
        await session.send('成功')
    except ActionFailed:
        await session.send('QQ号有误')


@on_command('send_group', aliases=['send_group', 'say_group', '群发'], permission=SUPERUSER)
async def send_group(session: CommandSession):
    group_id = session.get('group_id', prompt='发给哪个群')
    msg = session.get('msg', prompt='发什么')
    bot = session.bot
    try:
        await bot.send_group_msg(group_id=group_id, message=msg)
        await session.send('成功')
    except ActionFailed:
        await session.send('群号有误')


# 私人消息的参数处理器
@send_private.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.rstrip()

    if session.is_first_run:
        if stripped_arg:
            try:
                session.state['user'] = int(stripped_arg.split()[0])
            except TypeError:
                session.pause('错误, 再输入一次QQ号')
            try:
                # 怪
                start = len(stripped_arg.split()[0]) + 1
                session.state['msg'] = stripped_arg[start:]
            except IndexError:
                session.state['msg'] = None
        return

    if not stripped_arg:
        if session.state.get('msg'):
            session.pause('错误, 再输入一次消息')

        session.pause('错误, 再输入一次QQ号')

    session.state[session.current_key] = stripped_arg


# 群聊天消息的参数处理器
@send_group.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.rstrip()

    if session.is_first_run:
        if stripped_arg:
            try:
                session.state['group_id'] = int(stripped_arg.split()[0])
            except TypeError:
                session.pause('错误, 再输入一次群号')
            try:
                # 怪
                start = len(stripped_arg.split()[0]) + 1
                session.state['msg'] = stripped_arg[start:]
            except IndexError:
                session.state['msg'] = None
        return

    if not stripped_arg:
        if session.state.get('msg'):
            session.pause('错误, 再输入一次消息')

        session.pause('错误, 再输入一次群号')

    session.state[session.current_key] = stripped_arg
