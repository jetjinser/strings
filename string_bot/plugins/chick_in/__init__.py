"""
check in
"""
from sqlite3 import OperationalError
from typing import Dict, Union, List

from nonebot import CommandGroup, CommandSession
from .check_in_system import *
from .check_in_image import ImageProcessing
from .data_source import get_image
from nonebot.permission import SUPERUSER

import base64
from aiocqhttp import MessageSegment

__plugin_name__ = '签到'
__plugin_usage__ = r"""签到服务

指令: 签到 / 注册"""

cg = CommandGroup('chick_in', only_to_me=False)

try:
    init = (
        'CREATE TABLE setting('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'group_id INT NOT NULL, '
        'function TEXT NOT NULL,'
        'bool INT NOT NULL'
        ');'
    )
    sql_exe(init)
except OperationalError:
    pass

off_dict: Dict[int, bool] = {}


def enable_group() -> Union[List[set], None]:
    sql_check = (
        'SELECT group_id FROM setting WHERE bool=?;'
    )
    enable_group_list = sql_exe(sql_check, (0,))
    if enable_group_list:
        return enable_group_list
    else:
        return


def update():
    global off_dict
    on_off_list = enable_group()
    if on_off_list:
        off_dict = {}
        for i in on_off_list:
            group_id = i[0]
            if not off_dict.get(group_id):
                off_dict[group_id] = False


update()


@cg.command('enable', aliases=['签到开关'], permission=SUPERUSER)
async def enable(session: CommandSession):
    enable_str = session.get('enable_str', prompt='开/关')

    group_id = session.ctx.get('group_id')

    enable_i = 0
    if enable_str == '开':
        enable_i = 1
        await session.send('已开启')
    elif enable_str == '关':
        enable_i = 0
        await session.send('已关闭')
    else:
        session.finish()

    sql_disable = (
        'REPLACE INTO setting VALUES (?, ?, ?, ?);'
    )
    sql_exe(sql_disable, (None, group_id, 'live', enable_i))
    update()


@cg.command('chick_in_cmd', aliases=['签到'])
async def chick_in_cmd(session: CommandSession):
    group_id = session.ctx.get('group_id')

    off = off_dict.get(int(group_id))

    if isinstance(off, bool):
        if not off:
            return

    async def _chick_in():
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

            image = ImageProcessing(image, text, 256, 'send')
            await image.save()

            bot = session.bot
            boo = await bot.can_send_image()
            boo = boo['yes']

            if not boo:
                await session.send(text)
            else:
                with open('./chick_image_cache/send.png', 'rb') as f:
                    base = base64.b64encode(f.read())
                img = MessageSegment.image(f'base64://{base.decode()}')
                await session.send(img)
        else:
            await session.send('您今天已经签到过了')

    try:
        await _chick_in()
    except (IndexError, TypeError):
        user_registration(session.ctx)
        await _chick_in()


@cg.command('chick_in_check', aliases=['查询', '个人信息'])
async def chick_in_check(session: CommandSession):
    group_id = session.ctx.get('group_id')

    off = off_dict.get(int(group_id))
    if isinstance(off, bool):
        if not off:
            return

    user_id = session.ctx['sender']['user_id']

    try:
        if not check_in_interval_judgment(user_id):
            msg = get_chick_in_check(user_id, '今日已签到✔')
        else:
            msg = get_chick_in_check(user_id, '今日未签到❌')
        await session.send(msg)
    except IndexError:
        await session.send('您还没有注册👀')


@enable.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['enable_str'] = stripped_arg
        return

    if not stripped_arg:
        session.pause()
    session.state[session.current_key] = stripped_arg
