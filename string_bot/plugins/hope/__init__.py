from PIL import Image
from nonebot import CommandGroup, CommandSession
from nonebot.permission import SUPERUSER
from aiocqhttp import MessageSegment
from .data_source import *
from ..chick_in import get_image
from ..tips import cuprum

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

#
# @cg.command('grey_scale', aliases=('灰色头像', '灰度头像'))
# async def hope_grey_scale(session: CommandSession):
#     user_id = session.ctx['sender']['user_id']
#
#     if not await cuprum(user_id, 10):
#         session.finish('铜币不足')
#     else:
#         await grey_scale_process(user_id)
#         img = MessageSegment.image('grey.jpg')
#         await session.send('该行为消耗10铜币')
#         await session.send(img)
#
#
# async def grey_scale_process(uid):
#     img = await get_image(uid)
#     image = Image.open(img).convert('L')
#     image.save('C:/Users/Administrator/Desktop/酷Q Pro/data/image/grey.jpg')
