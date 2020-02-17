from nonebot import CommandSession, CommandGroup
from nonebot.command.argfilter import controllers
from nonebot.permission import *
from .tips_process import *
from .cuprum import get_cuprum

__plugin_name__ = 'tips'
__plugin_usage__ = r"""通过消耗铜币(Cuprum)来 提交 / 删除 / 修改 /查询 tips

tips即签到图下的小字, 会在经审核后加入数据库, 每次修改消耗 5 铜币, 提交消耗 20 铜币, 删除消耗 1 铜币"""

cg = CommandGroup('tips', only_to_me=False)


@cg.command('submit', aliases=['提交tips', 'tips提交', '提交'])
async def tips_submit(session: CommandSession):
    sub_tips = session.get('sub_tips', prompt='请输入你要提交的tips', arg_filters=[controllers.handle_cancellation(session)])

    user_id = session.ctx['sender']['user_id']

    if already_exists(sub_tips):
        msg = await submit_ust(sub_tips, user_id)
        coin = await get_cuprum(user_id)
        await session.send(msg + f'  当前铜币:{coin}')
    else:
        session.finish('该tips已存在')


@cg.command('modify', aliases=['修改tips', 'tips修改', '修改'])
async def tips_modify(session: CommandSession):
    tips_id = session.get('tips_id', prompt='请输入要修改的tips的id')

    user_id = session.ctx['sender']['user_id']
    before = await get_ust(user_id, tips_id)

    mod_tips = session.get('tips', prompt=f'请输入修改后的tips, 原tips：{before}')

    msg = await modify_ust(mod_tips, user_id, tips_id)
    coin = await get_cuprum(user_id)
    await session.send(msg + f'  当前铜币:{coin}')


@cg.command('check', aliases=['check', '查询tips', 'tips查询'])
async def tips_check(session: CommandSession):
    user_id = session.ctx['sender']['user_id']

    msg = await get_ust_msg(user_id)

    if len(msg) > 277:
        await session.finish('消息过长, 请私聊查询')

    await session.send(str(msg))


@cg.command('hs', aliases=['历史提交tips', 'tips历史提交', '历史提交'])
async def tips_hs(session: CommandSession):
    user_id = session.ctx['sender']['user_id']

    msg = await get_ust_msg(user_id, False)

    if len(msg) > 277:
        await session.finish('消息过长, 请私聊查询')

    await session.send(str(msg))


@cg.command('delete', aliases=['删除tips', 'tips删除', '删除'])
async def tips_delete(session: CommandSession):
    user_id = session.ctx['sender']['user_id']

    del_tips_id = session.get('del_tips_id', prompt='请输入要删除的tips的id')

    msg = await delete_ust(user_id, del_tips_id)
    coin = await get_cuprum(user_id)
    await session.send(msg + f'  当前铜币:{coin}')


@cg.command('audit', aliases=['审核'], permission=SUPERUSER)
async def tips_audit(session: CommandSession):
    value, aud_id = await audit_ust()
    if value:
        aud = session.get('aud', prompt=value)
        audit_bool = await audit(aud_id, aud)

        if audit_bool:
            await session.send('好')
            await move_in_tips(aud_id)
        else:
            await session.send('ok')
    else:
        await session.send('没了')


# 提交tips的参数处理器
@tips_submit.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['sub_tips'] = str(stripped_arg)
        return

    if not stripped_arg:
        session.pause('请输入要提交的tips')

    session.state[session.current_key] = stripped_arg


# 修改tips的参数处理器
@tips_modify.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['tips_id'] = stripped_arg.split()[0]
            session.state['mod_tips'] = ''.join(stripped_arg.split()[1:])
        return

    if not stripped_arg:
        if session.state.get('tips_id'):
            session.pause('id不能为空，请重新输入')

        session.pause('要修改的tips不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg


# 删除tips的参数处理器
@tips_delete.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['del_tips_id'] = stripped_arg.split()[0]
        return

    if not stripped_arg:
        session.pause('请输入要删除的tips')

    session.state[session.current_key] = stripped_arg


# 审核tips的参数处理器
@tips_audit.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['aud'] = stripped_arg.split()[0]
        return

    if not stripped_arg:
        session.pause('好吗')

    session.state[session.current_key] = stripped_arg
