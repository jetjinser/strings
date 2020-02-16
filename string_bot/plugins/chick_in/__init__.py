from nonebot import CommandGroup, CommandSession
from .chick_in_system import *
from .check_in_image import ImageProcessing
from .data_source import get_image
from shutil import copyfile
import os

__plugin_name__ = '签到'
__plugin_usage__ = r"""签到服务

指令: 签到 / 注册"""

cg = CommandGroup('chick_in', only_to_me=False)


@cg.command('registered', aliases=['注册'])
async def registered(session: CommandSession):
    user_id = session.ctx['sender']['user_id']

    if user_registration_interval_judgment(user_id):
        user_registration(session.ctx)
        await session.send('注册成功!💃💃💃')
    else:
        await session.send('您已经注册过了🙌')


@cg.command('chick_in_cmd', aliases=['签到'])
async def chick_in_cmd(session: CommandSession):
    try:
        uid = session.ctx['sender']['user_id']

        if check_in_interval_judgment(uid):

            chick_in(uid)

            image = await get_image(uid)

            card = session.ctx.get('sender').get('_card')
            if card:
                text = chick_in_text(uid, card)
            else:
                nickname = session.ctx['sender']['nickname']
                text = chick_in_text(uid, nickname)

            image = ImageProcessing(image, text, 256, str(uid))
            image.save()

            bot = session.bot
            boo = await bot.can_send_image()
            boo = boo['yes']

            if not boo:
                await session.send(text)
                image.remove()
            else:
                # 把这个文件复制到docker挂载的coolq的文件夹里才能识别到
                copyfile('cache/' + str(uid) + '.png', '/home/ubuntu/coolq-pro/data/' + str(uid) + '.png')
                await session.send('[CQ:image,file=file:///data/' + str(uid) + '.png]')
                # await session.send('[CQ:image,file=file:///cache/'+ str(uid) + '.png]')
                image.remove()
                os.remove('/home/ubuntu/coolq-pro/data/' + str(uid) + '.png')
        else:
            await session.send('您今天已经签到过了')
    except IndexError:
        await session.finish('请发送"注册"  来完成注册!')


@cg.command('chick_in_check', aliases=['查询', '个人信息'])
async def chick_in_check(session: CommandSession):
    user_id = session.ctx['sender']['user_id']

    try:
        if not check_in_interval_judgment(user_id):
            msg = get_chick_in_check(user_id, '今日已签到✔')
        else:
            msg = get_chick_in_check(user_id, '今日未签到❌')
        await session.send(msg)
    except IndexError:
        await session.send('您还没有注册👀')
