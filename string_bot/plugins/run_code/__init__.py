from nonebot import CommandGroup, CommandSession
import os
import random
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
    await session.send(f'[CQ:image,file={filename}]')


# 暂时重复写, 大概以后会用类重写

@cg.command('assembly_run', aliases=['assembly_run'])
async def code_assembly_run(session: CommandSession):
    assembly_code = session.get('assembly_code', prompt='show me your code')
    msg = await code_run(assembly_code, 'assembly')
    await session.send(msg)


# assembly_run的参数处理器
@code_assembly_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['assembly_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('ats_run', aliases=['ats_run'])
async def code_ats_run(session: CommandSession):
    ats_code = session.get('ats_code', prompt='show me your code')
    msg = await code_run(ats_code, 'ats')
    await session.send(msg)


# ats_run的参数处理器
@code_ats_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['ats_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('assembly_run', aliases=['assembly_run'])
async def code_assembly_run(session: CommandSession):
    assembly_code = session.get('assembly_code', prompt='show me your code')
    msg = await code_run(assembly_code, 'assembly')
    await session.send(msg)


# assembly_run的参数处理器
@code_assembly_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['assembly_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('ats_run', aliases=['ats_run'])
async def code_ats_run(session: CommandSession):
    ats_code = session.get('ats_code', prompt='show me your code')
    msg = await code_run(ats_code, 'ats')
    await session.send(msg)


# ats_run的参数处理器
@code_ats_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['ats_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('bash_run', aliases=['bash_run'])
async def code_bash_run(session: CommandSession):
    bash_code = session.get('bash_code', prompt='show me your code')
    msg = await code_run(bash_code, 'bash')
    await session.send(msg)


# bash_run的参数处理器
@code_bash_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['bash_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('c_run', aliases=['c_run'])
async def code_c_run(session: CommandSession):
    c_code = session.get('c_code', prompt='show me your code')
    msg = await code_run(c_code, 'c')
    await session.send(msg)


# c_run的参数处理器
@code_c_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['c_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('clojure_run', aliases=['clojure_run'])
async def code_clojure_run(session: CommandSession):
    clojure_code = session.get('clojure_code', prompt='show me your code')
    msg = await code_run(clojure_code, 'clojure')
    await session.send(msg)


# clojure_run的参数处理器
@code_clojure_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['clojure_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('cobol_run', aliases=['cobol_run'])
async def code_cobol_run(session: CommandSession):
    cobol_code = session.get('cobol_code', prompt='show me your code')
    msg = await code_run(cobol_code, 'cobol')
    await session.send(msg)


# cobol_run的参数处理器
@code_cobol_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['cobol_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('coffeescript_run', aliases=['coffeescript_run'])
async def code_coffeescript_run(session: CommandSession):
    coffeescript_code = session.get('coffeescript_code', prompt='show me your code')
    msg = await code_run(coffeescript_code, 'coffeescript')
    await session.send(msg)


# coffeescript_run的参数处理器
@code_coffeescript_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['coffeescript_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('cpp_run', aliases=['cpp_run'])
async def code_cpp_run(session: CommandSession):
    cpp_code = session.get('cpp_code', prompt='show me your code')
    msg = await code_run(cpp_code, 'cpp')
    await session.send(msg)


# cpp_run的参数处理器
@code_cpp_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['cpp_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('crystal_run', aliases=['crystal_run'])
async def code_crystal_run(session: CommandSession):
    crystal_code = session.get('crystal_code', prompt='show me your code')
    msg = await code_run(crystal_code, 'crystal')
    await session.send(msg)


# crystal_run的参数处理器
@code_crystal_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['crystal_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('csharp_run', aliases=['csharp_run'])
async def code_csharp_run(session: CommandSession):
    csharp_code = session.get('csharp_code', prompt='show me your code')
    msg = await code_run(csharp_code, 'csharp')
    await session.send(msg)


# csharp_run的参数处理器
@code_csharp_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['csharp_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('d_run', aliases=['d_run'])
async def code_d_run(session: CommandSession):
    d_code = session.get('d_code', prompt='show me your code')
    msg = await code_run(d_code, 'd')
    await session.send(msg)


# d_run的参数处理器
@code_d_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['d_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('elixir_run', aliases=['elixir_run'])
async def code_elixir_run(session: CommandSession):
    elixir_code = session.get('elixir_code', prompt='show me your code')
    msg = await code_run(elixir_code, 'elixir')
    await session.send(msg)


# elixir_run的参数处理器
@code_elixir_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['elixir_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('elm_run', aliases=['elm_run'])
async def code_elm_run(session: CommandSession):
    elm_code = session.get('elm_code', prompt='show me your code')
    msg = await code_run(elm_code, 'elm')
    await session.send(msg)


# elm_run的参数处理器
@code_elm_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['elm_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('erlang_run', aliases=['erlang_run'])
async def code_erlang_run(session: CommandSession):
    erlang_code = session.get('erlang_code', prompt='show me your code')
    msg = await code_run(erlang_code, 'erlang')
    await session.send(msg)


# erlang_run的参数处理器
@code_erlang_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['erlang_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('fsharp_run', aliases=['fsharp_run'])
async def code_fsharp_run(session: CommandSession):
    fsharp_code = session.get('fsharp_code', prompt='show me your code')
    msg = await code_run(fsharp_code, 'fsharp')
    await session.send(msg)


# fsharp_run的参数处理器
@code_fsharp_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['fsharp_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('go_run', aliases=['go_run'])
async def code_go_run(session: CommandSession):
    go_code = session.get('go_code', prompt='show me your code')
    msg = await code_run(go_code, 'go')
    await session.send(msg)


# go_run的参数处理器
@code_go_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['go_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('groovy_run', aliases=['groovy_run'])
async def code_groovy_run(session: CommandSession):
    groovy_code = session.get('groovy_code', prompt='show me your code')
    msg = await code_run(groovy_code, 'groovy')
    await session.send(msg)


# groovy_run的参数处理器
@code_groovy_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['groovy_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('haskell_run', aliases=['haskell_run'])
async def code_haskell_run(session: CommandSession):
    haskell_code = session.get('haskell_code', prompt='show me your code')
    msg = await code_run(haskell_code, 'haskell')
    await session.send(msg)


# haskell_run的参数处理器
@code_haskell_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['haskell_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('idris_run', aliases=['idris_run'])
async def code_idris_run(session: CommandSession):
    idris_code = session.get('idris_code', prompt='show me your code')
    msg = await code_run(idris_code, 'idris')
    await session.send(msg)


# idris_run的参数处理器
@code_idris_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['idris_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('java_run', aliases=['java_run'])
async def code_java_run(session: CommandSession):
    java_code = session.get('java_code', prompt='show me your code')
    msg = await code_run(java_code, 'java')
    await session.send(msg)


# java_run的参数处理器
@code_java_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['java_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('javascript_run', aliases=['javascript_run'])
async def code_javascript_run(session: CommandSession):
    javascript_code = session.get('javascript_code', prompt='show me your code')
    msg = await code_run(javascript_code, 'javascript')
    await session.send(msg)


# javascript_run的参数处理器
@code_javascript_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['javascript_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('julia_run', aliases=['julia_run'])
async def code_julia_run(session: CommandSession):
    julia_code = session.get('julia_code', prompt='show me your code')
    msg = await code_run(julia_code, 'julia')
    await session.send(msg)


# julia_run的参数处理器
@code_julia_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['julia_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('kotlin_run', aliases=['kotlin_run'])
async def code_kotlin_run(session: CommandSession):
    kotlin_code = session.get('kotlin_code', prompt='show me your code')
    msg = await code_run(kotlin_code, 'kotlin')
    await session.send(msg)


# kotlin_run的参数处理器
@code_kotlin_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['kotlin_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('lua_run', aliases=['lua_run'])
async def code_lua_run(session: CommandSession):
    lua_code = session.get('lua_code', prompt='show me your code')
    msg = await code_run(lua_code, 'lua')
    await session.send(msg)


# lua_run的参数处理器
@code_lua_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['lua_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('mercury_run', aliases=['mercury_run'])
async def code_mercury_run(session: CommandSession):
    mercury_code = session.get('mercury_code', prompt='show me your code')
    msg = await code_run(mercury_code, 'mercury')
    await session.send(msg)


# mercury_run的参数处理器
@code_mercury_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['mercury_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('nim_run', aliases=['nim_run'])
async def code_nim_run(session: CommandSession):
    nim_code = session.get('nim_code', prompt='show me your code')
    msg = await code_run(nim_code, 'nim')
    await session.send(msg)


# nim_run的参数处理器
@code_nim_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['nim_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('ocaml_run', aliases=['ocaml_run'])
async def code_ocaml_run(session: CommandSession):
    ocaml_code = session.get('ocaml_code', prompt='show me your code')
    msg = await code_run(ocaml_code, 'ocaml')
    await session.send(msg)


# ocaml_run的参数处理器
@code_ocaml_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['ocaml_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('perl_run', aliases=['perl_run'])
async def code_perl_run(session: CommandSession):
    perl_code = session.get('perl_code', prompt='show me your code')
    msg = await code_run(perl_code, 'perl')
    await session.send(msg)


# perl_run的参数处理器
@code_perl_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['perl_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('perl6_run', aliases=['perl6_run'])
async def code_perl6_run(session: CommandSession):
    perl6_code = session.get('perl6_code', prompt='show me your code')
    msg = await code_run(perl6_code, 'perl6')
    await session.send(msg)


# perl6_run的参数处理器
@code_perl6_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['perl6_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('php_run', aliases=['php_run'])
async def code_php_run(session: CommandSession):
    php_code = session.get('php_code', prompt='show me your code')
    msg = await code_run(php_code, 'php')
    await session.send(msg)


# php_run的参数处理器
@code_php_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['php_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('python_run', aliases=['python_run'])
async def code_python_run(session: CommandSession):
    python_code = session.get('python_code', prompt='show me your code')
    msg = await code_run(python_code, 'python')
    await session.send(msg)


# python_run的参数处理器
@code_python_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['python_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('ruby_run', aliases=['ruby_run'])
async def code_ruby_run(session: CommandSession):
    ruby_code = session.get('ruby_code', prompt='show me your code')
    msg = await code_run(ruby_code, 'ruby')
    await session.send(msg)


# ruby_run的参数处理器
@code_ruby_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['ruby_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('rust_run', aliases=['rust_run'])
async def code_rust_run(session: CommandSession):
    rust_code = session.get('rust_code', prompt='show me your code')
    msg = await code_run(rust_code, 'rust')
    await session.send(msg)


# rust_run的参数处理器
@code_rust_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['rust_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('scala_run', aliases=['scala_run'])
async def code_scala_run(session: CommandSession):
    scala_code = session.get('scala_code', prompt='show me your code')
    msg = await code_run(scala_code, 'scala')
    await session.send(msg)


# scala_run的参数处理器
@code_scala_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['scala_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('swift_run', aliases=['swift_run'])
async def code_swift_run(session: CommandSession):
    swift_code = session.get('swift_code', prompt='show me your code')
    msg = await code_run(swift_code, 'swift')
    await session.send(msg)


# swift_run的参数处理器
@code_swift_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['swift_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg


@cg.command('typescript_run', aliases=['typescript_run'])
async def code_typescript_run(session: CommandSession):
    typescript_code = session.get('typescript_code', prompt='show me your code')
    msg = await code_run(typescript_code, 'typescript')
    await session.send(msg)


# typescript_run的参数处理器
@code_typescript_run.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['typescript_code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('talk is cheap, again plz')

    session.state[session.current_key] = stripped_arg
