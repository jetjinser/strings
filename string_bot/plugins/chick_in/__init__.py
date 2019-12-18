from nonebot import CommandGroup, CommandSession
from .chick_in_system import *
from .check_in_image import ImageProcessing
from .data_source import get_image
from shutil import copyfile

__plugin_name__ = '签到'
__plugin_usage__ = r"""签到服务

指令: 签到 / 注册"""

cg = CommandGroup('chick_in', only_to_me=False)


@cg.command('registered', aliases=['注册'])
async def registered(session: CommandSession):
    user_id = session.ctx['sender']['user_id']

    if user_registration_interval_judgment(user_id):
        user_registration(session.ctx)
        await session.send('注册成功!')
    else:
        await session.send('您已经注册过了')


@cg.command('chick_in_cmd', aliases=['签到'])
async def chick_in_cmd(session: CommandSession):
    try:
        uid = session.ctx['sender']['user_id']

        if check_in_interval_judgment(uid):

            chick_in(uid)

            image = await get_image(uid)

            card = session.ctx.get('sender').get('card')
            if card:
                text = chick_in_text(uid, card)
            else:
                nickname = session.ctx['sender']['nickname']
                text = chick_in_text(uid, nickname)

            image = ImageProcessing(image, text, 256, 'send')
            image.save()

            # 不抛异常, 但是没有酷Q pro就无法发图
            # 无法直接捕获异常
            # air时用:
            # await session.send(text)
            # pro时用:
            # 把这个文件复制到docker挂载的coolq的文件夹里才能识别到
            copyfile('data/send.png', '/home/ubuntu/coolq-pro/data/send.png')
            await session.send('[CQ:image,file=file:///data/send.png]')
        else:
            await session.send('您今天已经签到过了')
    except KeyError:
        await session.finish('请发送"注册"  来完成注册!')
