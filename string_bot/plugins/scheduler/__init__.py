import datetime
import time
from sqlite3 import OperationalError

from aiocqhttp.exceptions import ActionFailed

import nonebot
from aiocqhttp.exceptions import Error as CQHttpError
from plugins.fast.data_source import *
from plugins.group_admin import timestamp2date_string
from plugins.info.data_source import get_edu_news
from sql_exe import *

__plugin_name__ = '报时'
__plugin_usage__ = r"""定点报时"""


@nonebot.scheduler.scheduled_job('cron', hour='0')
async def _():
    bot = nonebot.get_bot()
    group_list = await bot.get_group_list()
    try:
        for group in group_list:
            group_id = group['group_id']
            await bot.send_group_msg(group_id=group_id,
                                     message='🕛')
    except CQHttpError:
        pass


@nonebot.scheduler.scheduled_job('cron', hour='6')
async def _():
    bot = nonebot.get_bot()
    group_list = await bot.get_group_list()
    try:
        for group in group_list:
            group_id = group['group_id']
            await bot.send_group_msg(group_id=group_id,
                                     message='早')
    except CQHttpError:
        pass


@nonebot.scheduler.scheduled_job('cron', hour='9', minute=20)
async def _():
    bot = nonebot.get_bot()
    group_list = await bot.get_group_list()
    try:
        for group in group_list:
            group_id = group['group_id']

            msg = await get_time_line_one()

            await bot.send_group_msg(group_id=group_id,
                                     message=msg)
    except CQHttpError:
        pass


# 教育新闻专属
@nonebot.scheduler.scheduled_job('cron', hour='8-22/4', minute=0)
async def _():
    bot = nonebot.get_bot()
    try:
        msg = await get_edu_news()
        await bot.send_group_msg(group_id=324622296,
                                 message=msg)
    except CQHttpError:
        pass


@nonebot.scheduler.scheduled_job('cron', day='*', hour='*', minute='*')
async def _():
    sql = (
        'SELECT group_id, deadline FROM deadline;'
    )
    values = sql_exe(sql)

    now_date = timestamp2date_string(time.time())

    for value in values:
        group_id = value[0]
        deadline = value[1]

        ny, nm, nd = map(int, now_date.split('-'))
        dy, dm, dd = map(int, deadline.split('-'))

        d1 = datetime.datetime(ny, nm, nd)
        d2 = datetime.datetime(dy, dm, dd)

        interval = d2 - d1

        if interval.days < 0:
            bot = nonebot.get_bot()
            url = 'https://jinser.xyz/2020/02/22/%E5%85%B3%E4%BA%8E%E6%94%B6%E8%B4%B9%E5%92%8Ctoken/'
            await bot.send_group_msg(group_id=group_id, message=f'试用期已过, 如要延期请访问 {url} 查看详情')
            try:
                await bot.set_group_leave(group_id=group_id)
            except ActionFailed:
                pass
