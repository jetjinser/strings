from nonebot import CommandGroup, CommandSession
from sql_exe import *
from sqlite3 import OperationalError
import os
import random

try:
    sql_init = (
        'CREATE TABLE draw('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'user_id INT NOT NULL,'
        'user_nickname TEXT NOT NULL,'
        'user_card TEXT,'
        'cards TEXT'
        ');'
    )
    sql_exe(sql_init)
except OperationalError:
    pass

__plugin_name__ = '抽卡'
__plugin_usage__ = """借用塔罗, 图一乐

指令: 单抽 / 十连 / 仓库"""

cg = CommandGroup('_card', only_to_me=False)


@cg.command('choice', aliases=['单抽'])
async def card_choice(session: CommandSession):
    path = 'data/image'

    file_list = os.listdir(path)

    ch = random.choice(file_list)

    ch_id = ch.split('_')[0]

    sql = (
        'INSERT INTO draw VALUES (NULL, ?, ?, ?, ?);'
    )

    ctx = session.ctx
    user_id = ctx['sender']['user_id']
    user_nickname = ctx['sender']['nickname']
    card = ctx.get('sender').get('_card')

    args = (user_id, user_nickname, card, ch_id)
    sql_exe(sql, args)
    # TODO 第一次抽卡时用 INSERT, 后续需要 UPDATE

    await session.send(ch)
