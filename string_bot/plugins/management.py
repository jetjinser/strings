from nonebot import CommandGroup, CommandSession

__plugin_name__ = ''

cg = CommandGroup('', only_to_me=False)


@cg.command('', aliases=[''])
async def _(session: CommandSession):
    pass


@_.args_parser
async def _(session: CommandSession):
    pass