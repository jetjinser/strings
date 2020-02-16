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
    question = session.get('question')
    answer = session.get('answer')

    sender = session.ctx['sender']
    user_id = sender['user_id']
    user_nickname = sender['nickname']
    user_card = sender.get('user_card')

    group_id = session.ctx.get('group_id')

    # TODO
    #  判断数据库和原代码中是否已存在 ✔
    #  设置群内命令 ✔
    #  ~~设置全局命令~~ 暂时否决
    #  @ (和图片) 优化

    base_cmd = ['yyy', '嘤一下', '嘤一个', '来嘤', 'kusa', '草', 'robot', '机屑人', 'string', '五十弦', 'mua', 'mua~',
                'zaima', 'nihao', 'wei,zaima', 'wei，zaima', 'nihao', '你好', '泥嚎', 'help', '怎么用', '怎么玩']
    if question in base_cmd:
        session.finish('与内置指令冲突🔧')

    sql_select = (
        'SELECT Q FROM cmd WHERE group_id=?;'
    )
    q_list = sql_exe(sql_select, (group_id,))
    if q_list:
        if (question,) in q_list:
            session.finish('该指令已存在💾')

    sql_insert = (
        'INSERT INTO cmd VALUES (NULL, ?, ?, ?, ?, ?, ?);'
    )
    sql_exe(sql_insert, (user_id, user_nickname, user_card, group_id, question, answer))

    demo = f'''\n\n@on_command('{question}', aliases=('{question}',), only_to_me=False)
async def _(session: CommandSession):
    group_id = session.ctx.get('group_id')
    sql = (
        'SELECT group_id, A FROM cmd WHERE Q=?'
    )
    cmd_group = sql_exe(sql, ('{question}',))
    cmd_group_dict = {{}}
    for i in cmd_group:
        cmd_group_dict[i[0]] = i[1]
    if group_id in cmd_group_dict.keys():
        await session.send(cmd_group_dict.get(group_id))\n'''

    with open('plugins/user_cmd.py', 'a', encoding='utf-8') as f:
        f.write(demo)
    importlib.reload(module=plugins.user_cmd)

    await session.send(f'⬈添加成功➾\n<Q>{question}</Q>\n<A>{answer}</A>')


@on_command('finish', only_to_me=False)
async def finish(session: CommandSession):
    question = session.get('question')
    answer = session.get('answer')

    session.finish(f'⭷添加失败⇲\n<Q>{question}</Q>\n<A>{answer}</A>\n参数不能为空')


@on_natural_language(only_to_me=False)
async def _(session: NLPSession):
    msg = session.ctx.get('message')
    pattern = re.compile(r'^添加问(.*)答(.*)$')
    boo = pattern.match(str(msg))
    if boo:
        if boo.group(1) and boo.group(2):
            cmd = 'add_cmd'
        else:
            cmd = 'finish'
        confidence = 100
        return IntentCommand(confidence, cmd, args={'question': boo.group(1), 'answer': boo.group(2)})
