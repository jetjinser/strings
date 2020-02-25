import datetime
import sqlite3
from sqlite3 import OperationalError

from nonebot import CommandSession, CommandGroup
from nonebot.permission import SUPERUSER

from random import randint
import time

from plugins.group_admin import timestamp2date_string
from sql_exe import sql_exe

__plugin_name__ = '回应'
__plugin_usage__ = r"""应激反应"""

cg = CommandGroup('response', only_to_me=False)


@cg.command('yyy', aliases=['嘤一下', '嘤一个', '来嘤'])
async def response_yyy(session: CommandSession):
    await session.send('嘤嘤嘤')


@cg.command('meow', aliases=['喵一下', '喵一个', '来喵'])
async def response_meow(session: CommandSession):
    await session.send('喵~')


@cg.command('kusa', aliases=['草'])
async def response_kusa(session: CommandSession):
    if randint(1, 10) > 8:
        await session.send('草')
    else:
        return


@cg.command('robot', aliases=['机屑人'])
async def response_robot(session: CommandSession):
    if randint(1, 10) > 5:
        await session.send('你才是机屑人')
    else:
        return


@cg.command('init', aliases=['init'], permission=SUPERUSER)
async def response_init(session: CommandSession):
    try:

        sql = (
            'CREATE TABLE subscription('
            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'group_id INT NOT NULL,'
            'platform TEXT NOT NULL,'
            'live_id INT NOT NULL'
            ');'
        )
        sql_exe(sql)

        init_bot = session.bot
        init_group_id_list = await init_bot.get_group_list()
        init_now_date = time.time()
        init_now_date = timestamp2date_string(init_now_date)
        for init_group_id in init_group_id_list:
            sql_insert = (
                'INSERT OR IGNORE INTO deadline VALUES (NULL, ?, ?);'
            )
            # +3天
            i_add_date = datetime.timedelta(days=3)

            i_ny, i_nm, i_nd = map(int, init_now_date.split('-'))
            i_d1 = datetime.datetime(i_ny, i_nm, i_nd)
            i_deadline = i_d1 + i_add_date
            i_deadline = i_deadline.strftime("%Y-%m-%d")

            sql_exe(sql_insert, (init_group_id.get('group_id'), i_deadline))
    except OperationalError:
        pass

    coon = sqlite3.connect(r'.\data\data.db')
    cursor = coon.cursor()

    sql = (
        'select group_id, deadline from deadline;'
    )
    cursor.execute(sql)

    values = cursor.fetchall()

    sql_drop = (
        'DROP TABLE deadline;'
    )
    cursor.execute(sql_drop)

    sql_create = (
        'CREATE TABLE deadline('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'group_id INT NOT NULL,'
        'deadline TEXT NOT NULL,'
        'UNIQUE (group_id)'
        ');'
    )
    cursor.execute(sql_create)

    for value in values:
        group_id = value[0]
        deadline = value[1]

        sql = (
            'INSERT OR IGNORE INTO deadline VALUES (NULL, ?, ?);'
        )
        cursor.execute(sql, (group_id, deadline))

    cursor.close()
    coon.commit()
    coon.close()


@cg.command('mua', aliases=['mua', 'mua~'])
async def response_mua(session: CommandSession):
    num = randint(1, 10)
    if num >= 5:
        await session.send('mua')
    elif num < 5:
        await session.send('呕呕!谁想和死肥宅亲亲啊!kimo!')
    else:
        return


@cg.command('zaima', aliases=['zaima', 'wei,zaima', 'wei，zaima'])
async def response_zaima(session: CommandSession):
    if randint(1, 10) > 2:
        await session.send('buzai,cnm')
    else:
        return


@cg.command('nihao', aliases=['你好', '泥嚎'])
async def response_nihao(session: CommandSession):
    if randint(1, 10) > 6:
        await session.send('泥嚎,我很阔爱,请给我钱')
    else:
        return


@cg.command('help', aliases=['help', '怎么用', '怎么玩'])
async def response_help(session: CommandSession):
    if randint(1, 10) > 5:
        await session.send('@我说 帮助 查看功能')
    else:
        return
