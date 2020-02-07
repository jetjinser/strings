import nonebot
from nonebot import on_command, CommandSession


@on_command('usage', aliases=['使用帮助', '帮助', '使用方法', 'readme', '手册', '帮助手册', '使用手册'])
async def _(session: CommandSession):
    # 获取设置了名称的插件列表
    plugins = list(filter(lambda p: p.name, nonebot.get_loaded_plugins()))

    arg = session.current_arg_text.strip().lower()
    if not arg:
        # 如果用户没有发送参数，则发送功能列表
        await session.send(
            '我现在支持的功能有：\n\n' + '\n'.join(p.name for p in plugins) +
            '\n\n详情请输入 帮助 [指令], 如  帮助 信息' +
            '\n了解更多请访问 https://jinser.xyz/')
        return

    # 如果发了参数则发送相应命令的使用帮助
    for p in plugins:
        if p.name.lower() == arg:
            await session.send(p.usage)
