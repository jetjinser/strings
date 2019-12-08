from nonebot import on_command, CommandSession


@on_command('嘤一个', aliases=['嘤一下', '来嘤'])
async def _(session: CommandSession):
    await session.send('嘤嘤嘤')
