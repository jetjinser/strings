import nonebot
from aiocqhttp.exceptions import Error as CQHttpError


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

