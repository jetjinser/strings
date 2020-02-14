from nonebot import CommandGroup, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from datetime import date, timedelta
from jieba import posseg


from .data_source import *

__plugin_name__ = '信息'
__plugin_usage__ = r"""信息服务

指令: 历史上的今天 / 每日一句 / 新闻 / etc."""


cg = CommandGroup('info', only_to_me=False)


@cg.command('today_in_history', aliases=['历史上的今天'])
async def info_today_in_history(session: CommandSession):
    msg = await get_today_in_history()
    await session.send(msg)


@cg.command('one_sentence_a_day', aliases=['每日一句'])
async def info_one_sentence_a_day(session: CommandSession):
    msg = await get_one_sentence_a_day()
    await session.send(msg)


@cg.command('five_sayings', aliases=['five语录', '废物语录', '二次元语录'])
async def info_five_sayings(session: CommandSession):
    msg = await get_five_sayings()
    await session.send(msg)


@cg.command('one_day', aliases=['日历'])
async def one_day(session: CommandSession):
    date = session.get('date', prompt='你想查哪一天的日历(20190101)?')
    msg = await get_calendar(date)
    await session.send(str(msg))


@cg.command('today', aliases=['今日历'])
async def one_day(session: CommandSession):
    msg = await get_calendar()
    await session.send(str(msg))


# **是什么垃圾
@cg.command('garbage_classification', aliases=['垃圾分类', '分类'])
async def info_garbage_classification(session: CommandSession):
    garbage = session.get('garbage', prompt='分类什么垃圾?')
    msg = await get_garbage_classification(garbage)
    await session.send(msg)


@cg.command('joke', aliases=['joke', '段子', '笑话'])
async def info_joke(session: CommandSession):
    msg = await get_a_joke()
    await session.send(msg)


@cg.command('news', aliases=['news', '新闻', '近闻'])
async def info_news(session: CommandSession):
    msg = await get_news()
    await session.send(msg)


@cg.command('weather', aliases=['天气', '今天天气'])
async def info_weather(session: CommandSession):
    city = session.get('city', prompt='你想查哪个城市?')
    msg = await get_weather_of_city(city)
    await session.send(msg)


@cg.command('weather_the_date', aliases=['指定天气', '日期指定天气'])
async def info_weather_the_date(session: CommandSession):
    city = session.get('city', prompt='你想查哪个城市?')
    the_date = session.get('the_date', prompt='你想查哪一天?')
    msg = await get_weather_of_city_n_date(city, the_date)
    await session.send(msg)


@cg.command('daily_zhihu', aliases=['daily_zhihu', 'daily', '知乎日报'])
async def info_daily_zhihu(session: CommandSession):
    msg = await get_daily_zhihu()
    await session.send(msg)


@cg.command('gank', aliases=['gank', '干货', '整活'])
async def info_gank(session: CommandSession):
    gank_type = session.get('gank_type', prompt='')


@cg.command('steam', aliases=['steam_sale', 'steam促销', 'steam优惠'])
async def info_steam(session: CommandSession):
    msg = await get_steam_sale()
    await session.send(msg)


@cg.command('steam_list', aliases=['steamsales', 'steam促销列表', 'steam优惠列表'])
async def info_steam(session: CommandSession):
    msg = await get_steam_sale_list()
    await session.send(msg)


@cg.command('isbn', aliases=['isbn', 'isbn查询', 'ISBN', 'ISBN查询', '书号查询'])
async def info_isbn(session: CommandSession):
    isbn = session.get('isbn', prompt='请输入要查询的书号')
    msg = await get_isbn_book(isbn)
    await session.send(msg)


# 下次一定
@cg.command('steam_list', aliases=['steam_sale_list', 'steam促销列表', 'steam优惠列表'])
async def info_steam(session: CommandSession):
    msg = await get_steam_sale_list()
    await session.send(msg)


# 垃圾分类的参数处理器
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


# 带日期参数的天气的参数处理器
@info_weather_the_date.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['city'] = stripped_arg.split()[0]
            try:
                session.state['the_date'] = stripped_arg.split()[1]
            except IndexError:
                session.state['the_date'] = None
        return

    if not stripped_arg:
        if session.state.get('the_date'):
            session.pause('要查询的城市名称不能为空呢，请重新输入')

        session.pause('要查询的日期不能为空呢，请重新输入')

    session.state[session.current_key] = stripped_arg


# 天气的参数处理器
@info_weather.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['city'] = stripped_arg.split()[0]
        return

    if not stripped_arg:
        session.pause('查个城市?')

    session.state[session.current_key] = stripped_arg


# 日历的参数处理器
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


# ISBN查询的参数处理器
@info_isbn.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['isbn'] = stripped_arg.split()[0]
        return

    if not stripped_arg:
        session.pause('查啥啊')

    session.state[session.current_key] = stripped_arg


# 干货的参数处理器
@info_gank.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    type_list = ['福利', 'Android', 'iOS', '休息视频', '拓展资源', '前端']

    if session.is_first_run:
        if stripped_arg:
            session.state['gank_type'] = stripped_arg.split()[0]
            if session.state.get('gank_type') not in type_list + ['1', '2', '3', '4', '5', '6']:
                session.finish(f'干货支持的类型有: {" / ".join(type_list)}, 或与其对应的数字: 如 2 对应 Android')
            try:
                type_num = int(session.state.get('gank_type'))
                msg = await get_gank(type_list[type_num - 1])
                session.finish(msg)
            except (ValueError, IndexError):
                msg = await get_gank(session.state.get('gank_type'))
                session.finish(msg)
        msg = await get_gank()
        session.finish(msg)

    if not stripped_arg:
        session.finish()

    session.state[session.current_key] = stripped_arg


@on_natural_language(keywords={'天气'})
async def _(session: NLPSession):
    stripped_msg = session.msg_text.strip()
    words = posseg.lcut(stripped_msg)

    city = None
    for word in words:
        if word.flag == 'ns':
            city = word.word
            break

    return IntentCommand(90.0, ('info', 'weather'), current_arg=city or '')
