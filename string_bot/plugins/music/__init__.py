from nonebot import CommandGroup, CommandSession
from .data_source import *

cmd_qq = ['qq点歌']
cmd_163 = ['网易云点歌', '点歌']
cmd = cmd_qq + cmd_163

__plugin_name__ = '点歌'
__plugin_usage__ = fr"""点歌服务
默认为网易云

指令: {' / '.join(cmd)}"""

cg = CommandGroup('music', only_to_me=False)


@cg.command('qq_song', aliases=cmd_qq)
async def music_qq_song(session: CommandSession):
    keyword = session.get('keyword', prompt='你想点播哪首歌')
    song_id = await search_song_qq(keyword)
    if not song_id:
        session.finish('发生未知错误或歌曲不存在')
    await session.send(f'[CQ:music,type=qq,id={song_id}]')


@cg.command('163_song', aliases=cmd_163)
async def music_163_song(session: CommandSession):
    # session.finish('遇到未知错误, 无法分享')
    keyword = session.get('keyword', prompt='你想点播哪首歌')
    song_id = await search_song_163(keyword)
    if not song_id:
        session.finish('发生未知错误或歌曲不存在')
    await session.send(f'[CQ:music,type=163,id={song_id}]')


# 点歌的参数处理器
@music_qq_song.args_parser
@music_163_song.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['keyword'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('点什么?')

    session.state[session.current_key] = stripped_arg
