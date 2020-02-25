from nonebot import on_request, RequestSession
from nonebot import on_notice, NoticeSession
from .process import *
from sql_exe import *
from sqlite3 import OperationalError
import datetime

import asyncio

try:
    sql1 = (
        'CREATE TABLE token('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'token TEXT NOT NULL,'
        'duration INT NOT NULL'
        ');'
    )
    sql_exe(sql1)
except OperationalError:
    pass

try:
    sql2 = (
        'CREATE TABLE deadline('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'group_id INT NOT NULL,'
        'deadline TEXT NOT NULL'
        ');'
    )
    sql_exe(sql2)
except OperationalError:
    pass


# # 将函数注册为群请求处理器
# @on_request('group')
# async def _(session: RequestSession):
#     # 判断验证信息是否符合要求
#     if session.ctx['comment'] == '暗号':
#         # 验证信息正确，同意入群
#         await session.approve()
#         return
#     # 验证信息错误，拒绝入群
#     await session.reject('请说暗号')


@on_notice('group_increase')
async def _(session: NoticeSession):
    ctx = session.ctx
    if ctx['sub_type'] == 'invite' and ctx['user_id'] == ctx['self_id']:
        await session.send('大家好')

        bot = session.bot
        ctx = session.ctx
        group_id = ctx['group_id']

        sql = (
            'SELECT deadline FROM deadline WHERE group_id=?'
        )
        deadline = sql_exe(sql, (group_id,))
        now_date = timestamp2date_string(ctx['time'])

        if deadline:
            deadline = deadline[0][0]
            ny, nm, nd = map(int, now_date.split('-'))
            dy, dm, dd = map(int, deadline.split('-'))

            d1 = datetime.datetime(ny, nm, nd)
            d2 = datetime.datetime(dy, dm, dd)

            interval = d2 - d1

            if interval.days < 0:
                await session.send('试用期已过, 将在五分钟后退群, @我说 token ,并输入相应的token可延长使用时间, 详情请查看: '
                                   'https://jinser.xyz/2020/02/22/%E5%85%B3%E4%BA%8E%E6%94%B6%E8%B4%B9%E5%92%8Ctoken/')
                await asyncio.sleep(300)
                # 退群
                await bot.set_group_leave(group_id=group_id)
        else:
            sql_insert2 = (
                'INSERT OR IGNORE INTO deadline VALUES (NULL, ?, ?);'
            )
            # +3天
            add_date = datetime.timedelta(days=3)

            ny, nm, nd = map(int, now_date.split('-'))
            d1 = datetime.datetime(ny, nm, nd)
            deadline = d1 + add_date
            deadline = deadline.strftime("%Y-%m-%d")

            sql_exe(sql_insert2, (group_id, deadline))
            await session.send('目前正处于试用期, 将在三天后过期, 若要延长使用时间请访问 '
                               'https://jinser.xyz/2020/02/22/%E5%85%B3%E4%BA%8E%E6%94%B6%E8%B4%B9%E5%92%8Ctoken/ 来查看详情')
    else:
        await session.send('欢迎')


@on_notice('group_decrease')
async def _(session: NoticeSession):
    bot = session.bot
    ctx = session.ctx.copy()
    if ctx['sub_type'] == 'kick_me':
        group_id = ctx['group_id']
        operator_id = ctx['operator_id']
        f_time = timestamp2string(ctx['time'])
        await bot.send_private_msg(user_id=2301583973, message=f'I was kicked out of the group of 『{group_id}』, '
                                                               f'the operator is 『{operator_id}』, '
                                                               f'『{f_time}』')
    else:
        return


@on_request('friend')
async def _(session: RequestSession):
    bot = session.bot
    await session.approve()

    ctx = session.ctx.copy()
    user_id = ctx['user_id']
    comment = ctx['comment']
    f_time = timestamp2string(ctx['time'])
    if comment:
        await bot.send_private_msg(user_id=2301583973, message=f'I am friend with 『{user_id}』, '
                                                               f'the comment is 『{comment}』, '
                                                               f'『{f_time}』')
    else:
        await bot.send_private_msg(user_id=2301583973, message=f'I am friend with 『{user_id}』,'
                                                               f'『{f_time}』')
    return


@on_request('group')
async def _(session: RequestSession):
    bot = session.bot
    ctx = session.ctx.copy()
    if ctx['sub_type'] == 'invite':
        await session.approve()
        group_id = ctx['group_id']
        comment = ctx['comment']
        time = timestamp2string(ctx['time'])
        await bot.send_private_msg(user_id=2301583973, message=f'I was invited to join the 『{group_id}』 group, '
                                                               f'the comment is 『{comment}』, '
                                                               f'『{time}』')
    else:
        return
