import nonebot
from .live_state import *
from sql_exe import *
import asyncio

live_cache = {}


@nonebot.scheduler.scheduled_job('interval', minutes=3)
async def _():
    bot = nonebot.get_bot()

    sql_select = (
        'SELECT group_id, live_id, platform FROM subscription;'
    )
    lis = sql_exe(sql_select)

    for i in lis:
        group_id = i[0]
        live_id = i[1]
        platform = i[2]

        state, live_dict = await get_bili_live(live_id)

        if not live_cache.get(group_id):
            live_cache[group_id] = []

        # 如果直播间在直播且不在直播缓存列表中
        if state == 1 and live_id not in live_cache.get(group_id):
            live_cache.get(group_id).append(live_id)  # 加入直播缓存列表

            # 格式化msg 并发送
            title = live_dict['title']
            img = live_dict['img']
            uname = live_dict['uname']

            msg = f'{title}\n{uname} 开播了\n{platform} | https://live.bilibili.com/{live_id}'

            boo = await bot.can_send_image()
            boo = boo['yes']

            if boo:
                msg = f'[CQ:image,file={img}]' + msg
            else:
                msg = img + '\n' + msg

            await bot.send_group_msg(group_id=group_id, message=msg)
        # 如果不在直播
        elif state == 0:
            try:
                # 尝试从直播缓存列表中删除该直播间
                live_cache.get(group_id).remove(live_id)
            except (ValueError, AttributeError):
                pass

        await asyncio.sleep(2)
