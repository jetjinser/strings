from nonebot import CommandSession, CommandGroup
from nonebot.permission import SUPERUSER

cg = CommandGroup('response', only_to_me=False)


@cg.command('super_admin', aliases=['上报'], permission=SUPERUSER)
async def response_yyy(session: CommandSession):
    msg = session.ctx
    await session.send(str(msg))
