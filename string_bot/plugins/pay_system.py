from nonebot import CommandGroup, CommandSession
from nonebot.permission import SUPERUSER
from sql_exe import *
from sqlite3 import OperationalError
import datetime

import os
import base64

__plugin_name__ = '收费系统'
__plugin_usage__ = r"""收费系统
为了填补授权和~~服务器~~的资金
https://jinser.xyz/2020/02/22/%E5%85%B3%E4%BA%8E%E6%94%B6%E8%B4%B9%E5%92%8Ctoken/"""

cg = CommandGroup('pay', only_to_me=True)


@cg.command('token_j', aliases=['token'])
def pay_token_j(session: CommandSession):
    token = session.get('token', prompt='请输入token')
    group_id = session.ctx['group_id']

    sql = (
        'SELECT duration FROM token WHERE token=?;'
    )
    duration = sql_exe(sql, (token,))
    if duration:  # 天数(31)
        duration = duration[0][0]
        try:
            sql_select = (
                'SELECT deadline FROM deadline WHERE group_id=?;'
            )
            deadline = sql_exe(sql_select, (group_id,))[0][0]
            add_date = datetime.timedelta(days=duration)

            dy, dm, dd = map(int, deadline.split('-'))
            d_deadline = datetime.datetime(dy, dm, dd)

            now = datetime.datetime.now()
            interval = d_deadline - now

            if interval.days < 0:
                deadline = now + add_date
            else:
                deadline = d_deadline + add_date

            deadline = deadline.strftime('%Y-%m-%d')

            sql_update = (
                'UPDATE deadline SET deadline=? WHERE group_id=?;'
            )
            sql_exe(sql_update, (deadline, group_id))

            sql_delete = (
                'DELETE FROM token WHERE token=?;'
            )
            sql_exe(sql_delete, (token,))

            session.finish(f'已延长, 到期时间: {deadline}')
        except OperationalError:
            session.finish('为保证群号正确, 请将机器人邀请入群再进行token验证')
    else:
        session.finish('token不存在')


@cg.command('token', aliases=['get_token'], permission=SUPERUSER)
def pay_token(session: CommandSession):
    duration = session.get('duration', prompt='时长(日)?')
    a = os.urandom(32)
    token = base64.b64encode(a)
    token = str(token, encoding="utf-8")

    sql = (
        'INSERT INTO token VALUES (NULL, ?, ?);'
    )
    sql_exe(sql, (token, duration))

    session.finish(token)


@cg.command('check_token', aliases=['查询到期', '查询到期时间'], only_to_me=False)
async def pay_check_token(session: CommandSession):
    group_id = session.ctx.get('group_id')

    sql_select = (
        'SELECT deadline FROM deadline WHERE group_id=?;'
    )
    deadline = sql_exe(sql_select, (group_id,))[0][0]
    await session.send(f'到期日期为: {deadline}')
