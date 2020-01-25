from nonebot import CommandGroup, CommandSession
from .data_source import *

cmd = ['isearch']

__plugin_name__ = '搜图'
__plugin_usage__ = fr"""搜二次元图
搜索源: Pixivic.com

指令: {' / '.join(cmd)}"""

cg = CommandGroup('isearch', only_to_me=False)


@cg.command('pixivic', aliases=cmd)
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

# @isearch_pixivic.args_parser
# async def _(session: CommandSession):
#     stripped_arg = session.current_arg_text.strip()
#
#     if session.is_first_run:
#         if stripped_arg:
#             session.state['oiu'] = stripped_arg
#         return
#
#     if not stripped_arg:
#         session.pause('搜什么?')
#
#     session.state[session.current_key] = stripped_arg
