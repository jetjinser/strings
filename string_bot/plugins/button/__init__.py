"""
button plugin __init__.py
"""
from nonebot import CommandGroup, CommandSession
from .voice_source import *


__plugin_name__ = 'button'
__plugin_usage__ = r"""voice按钮

指令: 夸按钮"""

cg = CommandGroup('button', only_to_me=False)


@cg.command('aqua', aliases=['aqua_button', '夸按钮', '夸叫'])
async def button_aqua(session: CommandSession):
    voice = await get_aqua_voice_url()
    await session.send(f'[CQ:record,file={voice}]')


@cg.command('mea', aliases=['mea_button', '咩按钮', '咩叫'])
async def button_mea(session: CommandSession):
    voice = await get_mea_voice_url()
    await session.send(f'[CQ:record,file={voice}]')
