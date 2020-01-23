from nonebot import CommandGroup, CommandSession
from .voice_source import *


__plugin_name__ = 'button'
__plugin_usage__ = fr"""voice按钮

指令: 夸按钮"""

cg = CommandGroup('button', only_to_me=False)


@cg.command('aqua', aliases=['aqua_button', '夸按钮'])
async def button_aqua(session: CommandSession):
    voice = await get_aqua_button_url()
    await session.send(f'[CQ:record,file={voice}]')
