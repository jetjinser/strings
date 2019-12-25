from nonebot import CommandSession, CommandGroup
from random import randint

__plugin_name__ = '回应'
__plugin_usage__ = r"""应激反应"""


cg = CommandGroup('response', only_to_me=False)


@cg.command('yyy', aliases=['嘤一下', '嘤一个', '来嘤'])
async def response_yyy(session: CommandSession):
    await session.send('嘤嘤嘤')


@cg.command('meow', aliases=['喵一下', '喵一个', '来喵'])
async def response_meow(session: CommandSession):
    await session.send('喵~')


@cg.command('kusa', aliases=['草'])
async def response_kusa(session: CommandSession):
    if randint(1, 10) > 4:
        await session.send('草')
    else:
        return


@cg.command('robot', aliases=['机屑人'])
async def response_robot(session: CommandSession):
    if randint(1, 10) > 5:
        await session.send('机屑人')
    else:
        return


@cg.command('string', aliases=['五十弦'])
async def response_string(session: CommandSession):
    if randint(1, 10) > 3:
        await session.send('干嘛')
    else:
        return


@cg.command('mua', aliases=['mua', 'mua~'])
async def response_mua(session: CommandSession):
    num = randint(1, 10)
    if num >= 5:
        await session.send('mua')
    elif num < 5:
        await session.send('呕呕!谁想和死肥宅亲亲啊!kimo!')
    else:
        return


@cg.command('zaima', aliases=['zaima', 'wei,zaima', 'wei，zaima'])
async def response_zaima(session: CommandSession):
    if randint(1, 10) > 2:
        await session.send('buzai,cnm')
    else:
        return


@cg.command('nihao', aliases=['你好', '泥嚎'])
async def response_nihao(session: CommandSession):
    if randint(1, 10) > 6:
        await session.send('泥嚎,我很阔爱,请给我钱')
    else:
        return


@cg.command('help', aliases=['help', '怎么用', '怎么玩'])
async def response_help(session: CommandSession):
    await session.send('@我说 帮助 查看功能')


