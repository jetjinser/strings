from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from sql_exe import *
from sqlite3 import OperationalError

import re
import importlib

from plugins.user_cmd import *
import plugins.user_cmd

sql_create = (
    'CREATE TABLE draw('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'user_id INT NOT NULL,'
    'user_nickname TEXT NOT NULL,'
    'user_card TEXT,'
    'group_id INT,'
    'Q TEXT NOT NULL,'
    'A TEXT NOT NULL,'
    ');'
)
try:
    sql_exe(sql_create)
except OperationalError:
    pass


@on_command('add_cmd', only_to_me=False)
async def add_cmd(session: CommandSession):
    question = session.get('question', prompt='要添加的指令是什么?')
    answer = session.get('answer', prompt='想要我回答什么?')

    sender = session.ctx['sender']
    user_id = sender['user_id']
    user_nickname = sender['nickname']
    user_card = sender.get('user_card')

    group_id = session.ctx.get('group_id')

    # TODO
    #  判断数据库和原代码中是否已存在 ✔
    #  设置群内命令和全局命令
    #  @ (和图片) 优化
    #  bug: 无论是否同一个群, 命令名相同, 仅会执行最后一条

    base_cmd = ['yyy', '嘤一下', '嘤一个', '来嘤', 'kusa', '草', 'robot', '机屑人', 'string', '五十弦', 'mua', 'mua~',
                'zaima', 'nihao', 'wei,zaima', 'wei，zaima', 'nihao', '你好', '泥嚎', 'help', '怎么用', '怎么玩']
    if question in base_cmd:
        session.finish('与内置指令冲突')

    sql_select = (
        'SELECT Q FROM cmd WHERE group_id=?;'
    )
    q_list = sql_exe(sql_select, (group_id,))
    if (question,) in q_list:
        session.finish('该指令已存在')

    sql_insert = (
        'INSERT INTO cmd VALUES (NULL, ?, ?, ?, ?, ?, ?);'
    )
    sql_exe(sql_insert, (user_id, user_nickname, user_card, group_id, question, answer))

    demo = f'''\n\n@on_command('{question}', aliases=('{question}',), only_to_me=False)
async def _(session: CommandSession):
    group_id = session.ctx.get('group_id')
    cmd_group = {[group_id]}
    if group_id in cmd_group:
        await session.send('{answer}')\n'''

    with open('plugins/user_cmd.py', 'a', encoding='utf-8') as f:
        f.write(demo)
    importlib.reload(module=plugins.user_cmd)

    await session.send(f'成功\n<Q>{question}</Q>\n<A>{answer}</A>')


@on_natural_language(only_to_me=False)
async def _(session: NLPSession):
    msg = session.ctx.get('message')
    pattern = re.compile(r'^添加问(.*)答(.*)$')
    boo = pattern.match(str(msg))
    if boo:
        confidence = 100
        return IntentCommand(confidence, 'add_cmd', args={'question': boo.group(1), 'answer': boo.group(2)})
