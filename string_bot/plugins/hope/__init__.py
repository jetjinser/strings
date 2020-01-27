from nonebot import CommandGroup, CommandSession
from nonebot.permission import SUPERUSER
from .data_source import *

cmd = ['色图', '涩图', '瑟图', '来张色图', '来张涩图', '来张瑟图']

__plugin_name__ = '希望'
__plugin_usage__ = fr"""色图服务
暂不开放

指令: {' / '.join(cmd)}"""

cg = CommandGroup('hope', only_to_me=False)


@cg.command('random_hope', aliases=cmd, permission=SUPERUSER)
async def hope_random_hope(session: CommandSession):
    bot = session.bot
    boo = await bot.can_send_image()
    boo = boo['yes']

    if boo:
        await session.send('少女祈祷中...')
        hope_url = await get_random_hope()
        msg = f'[CQ:image,file={hope_url}]'
        await session.send(msg)
    else:
        await session.send('机器人暂不支持发图, 请给作者打钱')
