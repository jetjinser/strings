from nonebot import CommandSession, on_command, get_bot
from nonebot.permission import *

__plugin_name__ = '遥控'
__plugin_usage__ = r'''暂不开放'''


class ops:
    @staticmethod
    async def send_to_x(session: CommandSession, msg_type: str, boo: bool = False):
        bot = get_bot()
        param = session.get('param')
        param_split = param.split(' ', 1)
        if not boo:
            target_id, to_send = param_split[0], ''.join(param_split[1:])
        else:
            target_id, to_send = None, ''.join(param_split[0:])
        count = 0

        try:
            if msg_type == 'group':
                await bot.send_group_msg(group_id=target_id, message=to_send)
            elif msg_type == 'private':
                await bot.send_private_msg(user_id=target_id, message=to_send)
            elif msg_type == 'all_group':
                group_id_list = await bot.get_group_list()
                group_id_list = [gid['group_id'] for gid in group_id_list]
                for group_id in group_id_list:
                    count += 1
                    await bot.send_group_msg(group_id=group_id, message=to_send)
                await session.send(f'正在向{count}个群发送消息')
            elif msg_type == 'all_friends':
                session.finish('该功能暂时不可用')
                friend_id_list = await bot.get_friend_list()
                print(friend_id_list)
                friend_id_list = [fid['user_id'] for fid in friend_id_list]
                for friend_id in friend_id_list:
                    count += 1
                    await bot.send_private_msg(user_id=friend_id, message=to_send)
                await session.send(f'正在向{count}名好友发送消息')
            await session.send('success!')
        except CQHttpError as exc:
            await session.send(str(exc))

    @staticmethod
    async def arg_parser_x(session: CommandSession):
        stripped_arg = session.current_arg.strip()
        if stripped_arg:
            session.state['param'] = stripped_arg
        else:
            await session.send('用法：\n发送到群/好友 [群号/QQ] [内容]\n或\n发送到所有群/好友 [内容]')
            session.finish()


@on_command('发送到群', permission=SUPERUSER)
async def send_to_group(session: CommandSession):
    await ops.send_to_x(session, 'group')


@on_command('发送到好友', permission=SUPERUSER)
async def send_to_private(session: CommandSession):
    await ops.send_to_x(session, 'private')


@on_command('发送到所有群', permission=SUPERUSER)
async def send_to_all_groups(session: CommandSession):
    await ops.send_to_x(session, 'all_group', True)


@on_command('发送到所有好友', permission=SUPERUSER)
async def send_to_all_friends(session: CommandSession):
    await ops.send_to_x(session, 'all_friends', True)


@send_to_group.args_parser
@send_to_private.args_parser
async def group_arg_parse(session: CommandSession):
    await ops.arg_parser_x(session)


@send_to_all_groups.args_parser
async def all_group_arg_parse(session: CommandSession):
    await ops.arg_parser_x(session)


@send_to_all_friends.args_parser
async def all_friends_arg_parse(session: CommandSession):
    await ops.arg_parser_x(session)
