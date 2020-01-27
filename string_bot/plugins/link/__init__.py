from nonebot import CommandGroup, CommandSession
from nonebot.permission import SUPERUSER


__plugin_name__ = 'link'
__plugin_usage__ = r"""test"""

cg = CommandGroup('link', only_to_me=False)


@cg.command('share', aliases=['test'], permission=SUPERUSER)
async def link_share(session: CommandSession):
    url = 'https://jinser.xyz/'
    title = 'TEST'
    content = 'test_content'
    image = 'https://images-assets.nasa.gov/image/PIA17669/PIA17669~orig.jpg'
    await session.send(f'[CQ:share,url={url},title={title},content={content},image={image}]')
