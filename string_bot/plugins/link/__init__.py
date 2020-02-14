from nonebot import CommandGroup, CommandSession
# from nonebot.permission import SUPERUSER


__plugin_name__ = 'link'
__plugin_usage__ = r"""根据链接自动返回相关信息

//TODO"""

cg = CommandGroup('link', only_to_me=False)


# 下次一定
# @cg.command('share', aliases=['test'], permission=SUPERUSER)
# async def link_share(session: CommandSession):
#     url = 'https://jinser.xyz/'
#     title = 'TEST'
#     content = 'test_content'
#     image = 'https://images-assets.nasa.gov/image/PIA17669/PIA17669~orig.jpg'
#     await session.send(f'[CQ:share,url={url},title={title},content={content},image={image}]')

# @cg.command('bili', aliases=['https://www.bilibili.com/video/av80215402/'])
# async def link_bili(session: CommandSession):
#     a = session.state
#     await session.send(str(a))
