from nonebot import CommandGroup, CommandSession
from .data_source import *

pixivic_cmd = ['psearch', 'pixiv_search', 'p识图1']
trace_cmd = ['asearch', 'trace_search', '动画识图']
saucenao_cmd = ['ssearch', 'saucenao_search', 'p识图', 'p识图2']

__plugin_name__ = '搜图'
__plugin_usage__ = fr"""搜二次元图
搜索源: Pixivic.com, trace.moe, saucenao.com
存在bug

指令: {' / '.join(pixivic_cmd) + ' | ' + ' / '.join(trace_cmd) + ' | ' + ' / '.join(saucenao_cmd)}"""

cg = CommandGroup('isearch', only_to_me=False)


@cg.command('pixivic', aliases=pixivic_cmd)
async def isearch_pixivic(session: CommandSession):
    oiu = session.get('oiu', prompt='请发送要搜索的图片, 或图片的url')

    bot = session.bot
    boo = await bot.can_send_image()
    boo = boo['yes']
    await session.send('少女祈祷中...')

    # 怪
    if '[CQ:' in oiu:
        message = session.ctx.get('message')[0]
        m = str(message)
        start = m.find('url=') + 4
        url = m[start:-1]
        msg = await to_isearch_pixivic(url, boo)
    else:
        msg = await to_isearch_pixivic(oiu, boo)

    await session.send(msg)


@cg.command('trace', aliases=trace_cmd)
async def isearch_trace(session: CommandSession):
    oiu = session.get('oiu', prompt='请发送要搜索的图片, 或图片的url')

    bot = session.bot
    boo = await bot.can_send_image()
    boo = boo['yes']

    await session.send('少女祈祷中...')

    # 怪
    if '[CQ:' in oiu:
        message = session.ctx.get('message')[0]
        m = str(message)
        start = m.find('url=') + 4
        url = m[start:-1]
        msg = await to_isearch_trace(url, boo)
    else:
        msg = await to_isearch_trace(oiu, boo)

    await session.send(msg)


@cg.command('saucenao', aliases=saucenao_cmd)
async def isearch_saucenao(session: CommandSession):
    oiu = session.get('oiu', prompt='请发送要搜索的图片, 或图片的url')

    bot = session.bot
    boo = await bot.can_send_image()
    boo = boo['yes']

    await session.send('少女祈祷中...')

    # 怪
    if '[CQ:' in oiu:
        message = session.ctx.get('message')[0]
        m = str(message)
        start = m.find('url=') + 4
        url = m[start:-1]
        msg = await to_isearch_saucenao(url, boo)
    else:
        msg = await to_isearch_saucenao(oiu, boo)

    await session.send(msg)
