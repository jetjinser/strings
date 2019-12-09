from nonebot import CommandGroup, CommandSession
from string_bot.bot_lib.chick_in_system import *
from string_bot.bot_lib.check_in_image import *
from string_bot.bot_lib.api import get_image

__plugin_name__ = '签到'

cg = CommandGroup('chick_in', only_to_me=False)


@cg.command('registered', aliases=['注册'])
async def registered(session: CommandSession):
    user_id = await session.ctx['sender']['user_id']
    data = await get_user_info()
    if user_id not in data.keys():
        await user_registration(session.ctx)
        await session.send('注册成功!')
    else:
        await session.send('您已经注册过了')


# 失败, 尝试中
@cg.command('chick_in', aliases=['签到'])
async def chick_in(session: CommandSession):
    try:
        user_id = session.ctx['sender']['user_id']
        if check_in_interval_judgment(str(user_id)):
            # 找不到文件, 文件路径太乱了, 标记
            image = get_image(user_id)

            data = await get_chick_info(str(user_id))
            coin = await data['user_coin']
            cid = await data['check_in_days']
            favor = await data['user_favor']

            card = await session.ctx['sender']['card']
            if card:
                text = f'{card}\n签 到 成 功\nCuprum {coin}\n签到天数    {cid}     好感度    {favor}'
            else:
                nickname = await session.ctx['sender']['nickname']
                text = f'{nickname}\n签 到 成 功\nCuprum {coin}\n签到天数:   {cid}     好感度:   {favor}'

            image = ImageProcessing(image, text, 256, 'send')
            image.save()
            try:
                await session.send('[CQ:image,file=send.png]')
            except:
                await session.send(f'{card}\n签 到 成 功\nCuprum {coin}\n签到天数    {cid}     好感度    {favor}')
        else:
            await session.send('您今天已经签到过了')
    except KeyError:
        await session.send('请发送"注册"  来完成注册!')
