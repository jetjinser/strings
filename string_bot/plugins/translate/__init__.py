from nonebot import CommandGroup, CommandSession
import urllib.request
import urllib.parse
import json

__plugin_name__ = '翻译'
__plugin_usage__ = r"""翻译服务

指令: 翻译 ([翻译内容])"""


cg = CommandGroup('translate', only_to_me=False)


@cg.command('youdao', aliases=['翻译', '有道翻译', 'fanyi', 'translate'])
async def translate_youdao(session: CommandSession):
    content = session.get('content', prompt='你想翻译什么?')
    msg = await get_translate(content)
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


async def get_translate(content):
    youdao_url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data = {'i': content, 'from': 'AUTO', 'to': 'AUTO', 'smartresult': 'dict', 'client': 'fanyideskweb',
            'salt': '1525141473246', 'sign': '47ee728a4465ef98ac06510bf67f3023', 'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web', 'action': 'FY_BY_CLICKBUTTION', 'typoResult': 'false'}

    data = urllib.parse.urlencode(data).encode('utf-8')

    youdao_response = urllib.request.urlopen(youdao_url, data)
    youdao_html = youdao_response.read().decode('utf-8')
    target = json.loads(youdao_html)

    trans = target['translateResult']
    ret = ''
    for i in range(len(trans)):
        line = ''
        for j in range(len(trans[i])):
            line = trans[i][j]['tgt']
        ret += '译文：' + line

    return ret
