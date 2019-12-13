from nonebot import CommandGroup, CommandSession
from bot_lib.chick_in_system import *
from bot_lib.check_in_image import *
from bot_lib.api import get_image

__plugin_name__ = '签到'

cg = CommandGroup('chick_in', only_to_me=False)


@cg.command('registered', aliases=['注册'])
async def registered(session: CommandSession):
    user_id = session.ctx['sender']['user_id']
    data = get_user_info()
    if user_id not in data.keys():
        user_registration(session.ctx)
        await session.send('注册成功!')
    else:
        await session.send('您已经注册过了')


@cg.command('chick_in_cmd', aliases=['签到'])
async def chick_in_cmd(session: CommandSession):
    try:
        uid = session.ctx['sender']['user_id']
        uid = str(uid)
    except KeyError:
        await session.finish('请发送"注册"  来完成注册!')
    if check_in_interval_judgment(uid):

        image = await get_image(uid)

        card = session.ctx.get('sender').get('card')
        if card:
            text = chick_in_text(uid, card)
        else:
            nickname = session.ctx['sender']['nickname']
            text = chick_in_text(uid, nickname)

        image = ImageProcessing(image, text, 256, 'send')
        image.save()

        chick_in(uid)

        # 不抛异常, 但是没有酷Q pro就无法发图
        # 无法直接捕获异常
        # air时用:
        await session.send(text)
        # pro时用:
        # await session.send('[CQ:image,file=send.png]')
    else:
        await session.send('您今天已经签到过了')
