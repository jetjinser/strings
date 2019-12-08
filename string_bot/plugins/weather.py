from nonebot import on_command, CommandSession, CommandGroup
import shlex, random

a_list = ['天气', '查天气', '今天什么天气', '明天什么天气', '后天什么天气', '最近什么天气', '最近天气怎么样', '今天天气怎么样',
          '明天天气怎么样', '最近天气怎么样', '后天天气怎么样']

cg = CommandGroup('weather', only_to_me=False)


@cg.command('weather', aliases=a_list)
async def weather(session: CommandSession):
    # city = session.get('city', prompt='你想查哪个城市?')
    # date = session.get('date', prompt='你想查哪一天?')
    # await session.send('你查的是' + str(city))
    # await session.send('你查的是' + date)
    argv = shlex.split(session.current_arg_text)
    if not argv:
        session.finish('cnm')
    await session.send(str(argv))


@cg.command('choice', aliases=['抽签'])
async def random_choice(session: CommandSession):
    argv = shlex.split(session.current_arg_text)
    if not argv:
        session.finish('用法不对啦，需要给我提供要抽签的内容哦')
    await session.send(random.choice(argv))


# @weather.args_parser
# async def _(session: CommandSession):
#     if session.is_first_run:
#         return
#
#     session.args[session.current_key] = session.current_arg_text
