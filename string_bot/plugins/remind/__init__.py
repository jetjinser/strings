import nonebot
from aiocqhttp.exceptions import Error as CQHttpError


__plugin_name__ = '报时'
__plugin_usage__ = r"""零点报时"""


@nonebot.scheduler.scheduled_job('cron', hour='23', minute='59', second='59')
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

