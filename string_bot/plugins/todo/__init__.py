import datetime

import cn2an
import re

from apscheduler.triggers.date import DateTrigger  # 一次性触发器
from nonebot import CommandGroup, scheduler, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from aiocqhttp import MessageSegment

cg = CommandGroup('todo', only_to_me=False)


# @cg.command('赖床')
# async def _(session: CommandSession):
#     await session.send('我会在5分钟后再喊你')
#
#     # 制作一个“5分钟后”触发器
#     delta = datetime.timedelta(minutes=5)
#     trigger = DateTrigger(
#         run_date=datetime.datetime.now() + delta
#     )
#
#     # 添加任务
#     scheduler.add_job(
#         func=session.send,  # 要添加任务的函数，不要带参数
#         trigger=trigger,  # 触发器
#         args=('不要再赖床啦！',),  # 函数的参数列表，注意：只有一个值时，不能省略末尾的逗号
#         # kwargs=None,
#         misfire_grace_time=60,  # 允许的误差时间，建议不要省略
#         # jobstore='default',  # 任务储存库，在下一小节中说明
#     )


@cg.command('add')
async def todo_add(session: CommandSession):
    seconds = session.get('seconds')  # unit: s
    something = session.get('something')
    o_time = session.get('o_time')

    user_id = session.ctx.get('user_id')

    delta = datetime.timedelta(seconds=seconds)

    trigger = DateTrigger(
        run_date=datetime.datetime.now() + delta
    )

    something = MessageSegment.at(user_id) + ' ' + something

    scheduler.add_job(
        func=session.send,
        trigger=trigger,
        args=(something,),
        misfire_grace_time=60
    )

    await session.send(f'好的，我会在{o_time}提醒你{something}')


@cg.command('cancel')
async def todo_cancel(session: CommandSession):
    error = session.get('error')
    session.finish(error)


@on_natural_language(only_to_me=False)
async def _(session: NLPSession):
    unit_dict = {'秒': 1, '分钟': 60, '分': 60, '小时': 3600}

    pattern = re.compile(r'^(.*)(秒|分钟|分|小时)后提醒我(.*)$')

    todo_something = pattern.match(session.msg_text)

    if todo_something:
        o_time = todo_something.group(1)
        unit = todo_something.group(2)
        something = todo_something.group(3)

        try:
            lt = int(o_time)
        except ValueError:
            try:
                lt = cn2an.cn2an(o_time)
            except ValueError:
                return IntentCommand(75.0, ('todo', 'cancel'), args={'error': '时间设定错误'})

        unit_time = unit_dict.get(unit)
        if unit_time:
            scheduler_time = unit_time * lt
            return IntentCommand(75.0, ('todo', 'add'), args={
                'seconds': scheduler_time, 'something': something, 'o_time': o_time + unit + '后'})
