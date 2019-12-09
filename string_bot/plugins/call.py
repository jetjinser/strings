from nonebot import CommandSession, CommandGroup
from random import randint

__plugin_name__ = '叫'

cg = CommandGroup('call', only_to_me=False)


@cg.command('yyy', aliases=['嘤一下', '嘤一个', '来嘤'])
async def call_yyy(session: CommandSession):
    await session.send('嘤嘤嘤')


@cg.command('meow', aliases=['喵一下', '喵一个', '来喵'])
async def call_meow(session: CommandSession):
    await session.send('喵~')


@cg.command('kusa', aliases=['草'])
async def call_kusa(session: CommandSession):
    if randint(1, 10) > 6:
        await session.send('草')
    else:
        return


@cg.command('robot', aliases=['机屑人'])
async def call_robot(session: CommandSession):
    if randint(1, 10) > 5:
        await session.send('机屑人')
    else:
        return


@cg.command('string', aliases=['五十弦'])
async def call_string(session: CommandSession):
    if randint(1, 10) > 3:
        await session.send('干嘛')
    else:
        return


@cg.command('mua', aliases=['mua', 'mua~'])
async def call_mua(session: CommandSession):
    num = randint(1, 10)
    if num >= 5:
        await session.send('mua')
    elif num < 5:
        await session.send('呕呕!谁想和死肥宅亲亲啊!kimo!')
    else:
        return


@cg.command('zaima', aliases=['zaima', 'wei,zaima'])
async def call_zaima(session: CommandSession):
    if randint(1, 10) > 7:
        await session.send('buzai,cnm')
    else:
        return


@cg.command('hello', aliases=['你好', '泥嚎'])
async def call_hello(session: CommandSession):
    if randint(1, 10) > 7:
        await session.send('泥嚎，我很阔爱，请给我钱')
    else:
        return
