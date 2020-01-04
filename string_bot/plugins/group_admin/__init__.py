from nonebot import on_request, RequestSession
from nonebot import on_notice, NoticeSession
from .process import *


# __plugin_name__ = '自动化管理'
# __plugin_usage__ = r"""自动同意
# """


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
    await session.send('欢迎')


@on_notice('group_decrease')
async def _(session: NoticeSession):
    bot = session.bot
    ctx = session.ctx.copy()
    if ctx['sub_type'] == 'kick_me':
        group_id = ctx['group_id']
        operator_id = ctx['operator_id']
        time = timestamp2string(ctx['time'])
        await bot.send_private_msg(user_id=2301583973, message=f'I was kicked out of the group of 『{group_id}』, '
                                                               f'the operator is 『{operator_id}』, '
                                                               f'『{time}』')
    else:
        return


@on_request('friend')
async def _(session: RequestSession):
    bot = session.bot
    await session.approve()

    ctx = session.ctx.copy()
    user_id = ctx['user_id']
    comment = ctx['comment']
    time = timestamp2string(ctx['time'])
    if comment:
        await bot.send_private_msg(user_id=2301583973, message=f'I am friend with 『{user_id}』, '
                                                               f'the comment is 『{comment}』, '
                                                               f'『{time}』')
    else:
        await bot.send_private_msg(user_id=2301583973, message=f'I am friend with 『{user_id}』,'
                                                               f'『{time}』')
    return


@on_request('group')
async def _(session: RequestSession):
    bot = session.bot
    ctx = session.ctx.copy()
    if ctx['sub_type'] == 'invite':
        await session.approve()
        await session.send('大家好')
        group_id = ctx['group_id']
        comment = ctx['comment']
        time = timestamp2string(ctx['time'])
        await bot.send_private_msg(user_id=2301583973, message=f'I was invited to join the 『{group_id}』 group, '
                                                               f'the comment is 『{comment}』, '
                                                               f'『{time}』')
    else:
        return
