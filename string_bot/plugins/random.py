from nonebot import on_command, CommandSession

from random import randint


@on_command('随机数')
async def _(session: CommandSession):
    num = randint(1, 1000)
    await session.send(str(num))
