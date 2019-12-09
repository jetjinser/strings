from nonebot import CommandSession, CommandGroup
from string_bot.bot_lib.api import get_weather_of_city

a_list = ['天气', '查天气', '今天什么天气', '明天什么天气', '后天什么天气', '最近什么天气', '最近天气怎么样', '今天天气怎么样',
          '明天天气怎么样', '最近天气怎么样', '后天天气怎么样']

cg = CommandGroup('weather', only_to_me=False)


@cg.command('weather', aliases=a_list)
async def weather(session: CommandSession):
    city = session.get('city', prompt='你想查哪个城市?')
    date = session.get('date', prompt='你想查哪一天?')
    weather_report = await get_weather_of_city(city, date)
    await session.send(weather_report)


@weather.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['city'] = stripped_arg.split()[0]
            session.state['date'] = stripped_arg.split()[1]
        return

    if not stripped_arg:
        if session.state.get('date'):
            session.pause('要查询的城市名称不能为空呢，请重新输入')

        session.pause('要查询的日期不能为空呢，请重新输入')

    session.state[session.current_key] = stripped_arg
