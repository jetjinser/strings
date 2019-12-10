from nonebot import CommandGroup, CommandSession
from string_bot.bot_lib import api

__plugin_name__ = '信息'

cg = CommandGroup('info', only_to_me=False)


@cg.command('today_in_history', aliases=['历史上的今天'])
async def info_today_in_history(session: CommandSession):
    msg = await api.get_today_in_history()
    await session.send(msg)


@cg.command('one_sentence_a_day', aliases=['每日一句'])
async def info_one_sentence_a_day(session: CommandSession):
    msg = await api.get_one_sentence_a_day()
    await session.send(msg)


@cg.command('five_sayings', aliases=['five语录', '废物语录'])
async def info_five_sayings(session: CommandSession):
    msg = await api.get_five_sayings()
    await session.send(msg)


# **是什么垃圾
@cg.command('garbage_classification', aliases=['垃圾分类', '分类'])
async def info_garbage_classification(session: CommandSession):
    garbage = session.get('garbage', prompt='分类什么垃圾?')
    msg = await api.get_garbage_classification(garbage)
    await session.send(msg)


@cg.command('joke', aliases=['joke', '段子', '笑话'])
async def info_joke(session: CommandSession):
    msg = await api.get_a_joke()
    await session.send(msg)


@cg.command('news', aliases=['news', '新闻', '近闻'])
async def info_news(session: CommandSession):
    msg = await api.get_news()
    await session.send(msg)


@info_garbage_classification.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['garbage'] = stripped_arg.split()[0]
        return

    if not stripped_arg:
        session.pause('你倒是说啊')

    session.state[session.current_key] = stripped_arg
