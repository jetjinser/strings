from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from sql_exe import *
from sqlite3 import OperationalError

import re

sql_create = (
    'CREATE TABLE cmd('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'user_id INT NOT NULL,'
    'user_nickname TEXT NOT NULL,'
    'user_card TEXT,'
    'group_id INT,'
    'Q TEXT NOT NULL,'
    'A TEXT NOT NULL'
    ');'
)
try:
    sql_exe(sql_create)
except OperationalError:
    pass


@on_command('add_cmd')
async def add_cmd(session: CommandSession):
    question = session.get('question')
    answer = session.get('answer')
    group_id = session.get('group_id')

    sender = session.ctx['sender']
    user_id = sender['user_id']
    user_nickname = sender['nickname']
    user_card = sender.get('user_card')

    # TODO
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

    if group_id == 1:
        await session.send(f'⬈全局添加成功➾\n<Q>{question}</Q>\n<A>{answer}</A>')
    else:
        await session.send(f'⬈添加成功➾\n<Q>{question}</Q>\n<A>{answer}</A>')


@on_command('empty_finish')
async def empty_finish(session: CommandSession):
    question = session.get('question')
    answer = session.get('answer')
    session.finish(f'⭷添加失败⇲\n<Q>{question}</Q>\n<A>{answer}</A>\n参数不能为空')


# @on_command('finish')
# async def finish(session: CommandSession):
#     session.finish('无权限')


@on_command('user_cmd')
async def user_cmd(session: CommandSession):
    answer = session.get('answer')
    await session.send(answer)


@on_natural_language(only_to_me=False)
async def _(session: NLPSession):
    msg = session.ctx.get('message')
    msg = str(msg)
    ctx_group_id = session.ctx.get('group_id')

    pattern = re.compile(r'^添加问(.*)答(.*)$')
    pattern_global = re.compile(r'^全局添加问(.*)答(.*)$')
    boo = pattern.match(str(msg))
    boo_global = pattern_global.match(str(msg))

    sql = (
        'SELECT Q, A, group_id FROM cmd;'
    )
    cmd_list = sql_exe(sql)

    for cmd in cmd_list:
        question = cmd[0]
        answer = cmd[1]
        group_id = cmd[2]
        if (msg == question) and (group_id == ctx_group_id or group_id == 1):
            return IntentCommand(100, 'user_cmd', args={'answer': answer})

    if boo:
        if boo.group(1) and boo.group(2):
            cmd = 'add_cmd'
        else:
            cmd = 'empty_finish'
        return IntentCommand(100, cmd,
                             args={'question': boo.group(1), 'answer': boo.group(2), 'group_id': ctx_group_id})

    if boo_global:
        user_id = session.ctx.get('sender').get('user_id')
        if user_id == 2301583973 or user_id == 963949236:
            if boo_global.group(1) and boo_global.group(2):
                cmd = 'add_cmd'
            else:
                cmd = 'empty_finish'
            return IntentCommand(100, cmd,
                                 args={'question': boo_global.group(1), 'answer': boo_global.group(2), 'group_id': 1})
        # else:
        #     return IntentCommand(100, 'finish')
