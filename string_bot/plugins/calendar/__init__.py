from nonebot import CommandGroup, CommandSession
from .data_source import get_calendar
from datetime import date, timedelta

__plugin_name__ = '日历'
__plugin_usage__ = r"""获取日历

指令: 日历 / 今日历"""


cg = CommandGroup('calendar', only_to_me=False)


@cg.command('one_day', aliases=['日历'])
async def one_day(session: CommandSession):
    date = session.get('date', prompt='你想查哪一天的日历(20190101)?')
    msg = await get_calendar(date)
    await session.send(str(msg))


@one_day.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            if stripped_arg == '明天' or stripped_arg == '后天':
                if stripped_arg == '明天':
                    days = 1
                elif stripped_arg == '后天':
                    days = 2
                the_day = date.today() + timedelta(days)
                current_arg_text = the_day
                session.state['date'] = current_arg_text
            session.state['date'] = session.current_arg_text
        return

    if not stripped_arg:
        session.pause('要查询的内容不能为空')

    session.state[session.current_key] = stripped_arg


@cg.command('today', aliases=['今日历'])
async def one_day(session: CommandSession):
    msg = await get_calendar()
    await session.send(str(msg))
