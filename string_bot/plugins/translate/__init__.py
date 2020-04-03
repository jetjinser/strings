from nonebot import CommandGroup, CommandSession
from plugins.translate.data_source import *

__plugin_name__ = '翻译'
__plugin_usage__ = r"""翻译服务

指令: 翻译 ([翻译内容])"""

cg = CommandGroup('translate', only_to_me=False)


@cg.command('youdao', aliases=['翻译', '腾讯翻译', 'fanyi', 'translate'])
async def translate_youdao(session: CommandSession):
    content = session.get('content', prompt='你想翻译什么?')
    # app_key
    msg = await get_translate(content, app_key='BK8bAiTcKH1BsMoW')
    await session.send(msg)


@translate_youdao.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['content'] = session.current_arg_text
        return

    if not stripped_arg:
        session.pause('要查询的内容不能为空')

    session.state[session.current_key] = stripped_arg
