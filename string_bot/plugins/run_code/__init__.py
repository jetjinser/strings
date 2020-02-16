from nonebot import CommandGroup, CommandSession
import os
import random
from shutil import copyfile
from .languages_image import LanguagesImage
from .run_source import *

__plugin_name__ = '代码'
__plugin_usage__ = r"""在线运行代码

指令: languages_list / java_run"""

cg = CommandGroup('code', only_to_me=False)


@cg.command('languages_list', aliases=['languages_list', '语言列表', 'languages列表', 'list'])
async def code_languages_list(session: CommandSession):
    text_out = ('Currently supported languages:\n'
                'assembly   ats   bash   c\n'
                'clojure   cobol   coffeescript   cpp\n'
                'crystal   csharp   d   elixir\n'
                'elm   erlang   fsharp   go\n'
                'groovy   haskell   idris   java\n'
                'javascript   julia   kotlin   lua\n'
                'mercury   nim   ocaml   perl\n'
                'perl6   php   python   ruby\n'
                'rust   scala   swift   typescript')
    li = os.listdir('data/image')
    im = 'data/image/' + random.choice(li)
    img = LanguagesImage(im, text_out)
    filename = 'data/language_list.png'
    img.save(filename)
    copyfile(filename, '/home/ubuntu/coolq-pro/data/' + f'{filename}.png')
    await session.send(f'[CQ:image,file={filename}]')


@cg.command('assembly_run', aliases=['assembly_run'])
async def code_assembly_run(session: CommandSession):
    code = session.get('code', prompt='show me your code')
    msg = await code_run(code, 'assembly')
    await session.send(msg)


@cg.command('ats_run', aliases=['ats_run'])
async def code_ats_run(session: CommandSession):
    code = session.get('code', prompt='show me your code')
    msg = await code_run(code, 'ats')
    await session.send(msg)


@cg.command('bash_run', aliases=['bash_run'])
async def code_bash_run(session: CommandSession):
    code = session.get('code', prompt='show me your code')
    msg = await code_run(code, 'bash')
    await session.send(msg)


@cg.command('cclojure_run', aliases=['cclojure_run'])
async def code_cclojure_run(session: CommandSession):
    code = session.get('code', prompt='show me your code')
    msg = await code_run(code, 'cclojure')
    await session.send(msg)


@cg.command('cobol_run', aliases=['cobol_run'])
async def code_cobol_run(session: CommandSession):
    code = session.get('code', prompt='show me your code')
    msg = await code_run(code, 'cobol')
    await session.send(msg)


@cg.command('coffeescript_run', aliases=['coffeescript_run'])
async def code_coffeescript_run(session: CommandSession):
    code = session.get('code', prompt='show me your code')
    msg = await code_run(code, 'coffeescript')
    await session.send(msg)


@cg.command('cppcrystal_run', aliases=['cppcrystal_run'])
async def code_cppcrystal_run(session: CommandSession):
    code = session.get('code', prompt='show me your code')
    msg = await code_run(code, 'cppcrystal')
    await session.send(msg)


@cg.command('csharp_run', aliases=['csharp_run'])
async def code_csharp_run(session: CommandSession):
    code = session.get('code', prompt='show me your code')
    msg = await code_run(code, 'csharp')
    await session.send(msg)


@cg.command('d_run', aliases=['d_run'])
async def code_d_run(session: CommandSession):
    code = session.get('code', prompt='show me your code')
    msg = await code_run(code, 'd')
    await session.send(msg)


@cg.command('elixirelm_run', aliases=['elixirelm_run'])
async def code_elixirelm_run(session: CommandSession):
    code = session.get('code', prompt='show me your code')
    msg = await code_run(code, 'elixirelm')
    await session.send(msg)


@cg.command('erlang_run', aliases=['erlang_run'])
async def code_erlang_run(session: CommandSession):
    code = session.get('code', prompt='show me your code')
    msg = await code_run(code, 'erlang')
    await session.send(msg)


@cg.command('fsharp_run', aliases=['fsharp_run'])
async def code_fsharp_run(session: CommandSession):
    code = session.get('code', prompt='show me your code')
    msg = await code_run(code, 'fsharp')
    await session.send(msg)


@cg.command('gogroovy_run', aliases=['gogroovy_run'])
async def code_gogroovy_run(session: CommandSession):
    code = session.get('code', prompt='show me your code')
    msg = await code_run(code, 'gogroovy')
    await session.send(msg)


@cg.command('haskell_run', aliases=['haskell_run'])
async def code_haskell_run(session: CommandSession):
    code = session.get('code', prompt='show me your code')
    msg = await code_run(code, 'haskell')
    await session.send(msg)


@cg.command('idris_run', aliases=['idris_run'])
async def code_idris_run(session: CommandSession):
    code = session.get('code', prompt='show me your code')
    msg = await code_run(code, 'idris')
    await session.send(msg)


@cg.command('javajavascript_run', aliases=['javajavascript_run'])
async def code_javajavascript_run(session: CommandSession):
    code = session.get('code', prompt='show me your code')
    msg = await code_run(code, 'javajavascript')
    await session.send(msg)


@cg.command('julia_run', aliases=['julia_run'])
async def code_julia_run(session: CommandSession):
    code = session.get('code', prompt='show me your code')
    msg = await code_run(code, 'julia')
    await session.send(msg)


@cg.command('kotlin_run', aliases=['kotlin_run'])
async def code_kotlin_run(session: CommandSession):
    code = session.get('code', prompt='show me your code')
    msg = await code_run(code, 'kotlin')
    await session.send(msg)


@cg.command('luamercury_run', aliases=['luamercury_run'])
async def code_luamercury_run(session: CommandSession):
    code = session.get('code', prompt='show me your code')
    msg = await code_run(code, 'luamercury')
    await session.send(msg)


@cg.command('nim_run', aliases=['nim_run'])
async def code_nim_run(session: CommandSession):
    code = session.get('code', prompt='show me your code')
    msg = await code_run(code, 'nim')
    await session.send(msg)


@cg.command('ocaml_run', aliases=['ocaml_run'])
async def code_ocaml_run(session: CommandSession):
    code = session.get('code', prompt='show me your code')
    msg = await code_run(code, 'ocaml')
    await session.send(msg)


@cg.command('perlperl6_run', aliases=['perlperl6_run'])
async def code_perlperl6_run(session: CommandSession):
    code = session.get('code', prompt='show me your code')
    msg = await code_run(code, 'perlperl6')
    await session.send(msg)


@cg.command('php_run', aliases=['php_run'])
async def code_php_run(session: CommandSession):
    code = session.get('code', prompt='show me your code')
    msg = await code_run(code, 'php')
    await session.send(msg)


@cg.command('python_run', aliases=['python_run'])
async def code_python_run(session: CommandSession):
    code = session.get('code', prompt='show me your code')
    msg = await code_run(code, 'python')
    await session.send(msg)


@cg.command('rubyrust_run', aliases=['rubyrust_run'])
async def code_rubyrust_run(session: CommandSession):
    code = session.get('code', prompt='show me your code')
    msg = await code_run(code, 'rubyrust')
    await session.send(msg)


@cg.command('scala_run', aliases=['scala_run'])
async def code_scala_run(session: CommandSession):
    code = session.get('code', prompt='show me your code')
    msg = await code_run(code, 'scala')
    await session.send(msg)


@cg.command('swift_run', aliases=['swift_run'])
async def code_swift_run(session: CommandSession):
    code = session.get('code', prompt='show me your code')
    msg = await code_run(code, 'swift')
    await session.send(msg)


@cg.command('typescript_run', aliases=['typescript_run'])
async def code_typescript_run(session: CommandSession):
    code = session.get('code', prompt='show me your code')
    msg = await code_run(code, 'typescript')
    await session.send(msg)


@code_assembly_run.args_parser
@code_ats_run.args_parser
@code_bash_run.args_parser
@code_cclojure_run.args_parser
@code_cobol_run.args_parser
@code_coffeescript_run.args_parser
@code_cppcrystal_run.args_parser
@code_csharp_run.args_parser
@code_d_run.args_parser
@code_elixirelm_run.args_parser
@code_erlang_run.args_parser
@code_fsharp_run.args_parser
@code_gogroovy_run.args_parser
@code_haskell_run.args_parser
@code_idris_run.args_parser
@code_javajavascript_run.args_parser
@code_julia_run.args_parser
@code_kotlin_run.args_parser
@code_luamercury_run.args_parser
@code_nim_run.args_parser
@code_ocaml_run.args_parser
@code_perlperl6_run.args_parser
@code_php_run.args_parser
@code_python_run.args_parser
@code_rubyrust_run.args_parser
@code_scala_run.args_parser
@code_swift_run.args_parser
@code_typescript_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg
