import nonebot

bot = nonebot.get_bot()


@bot.server_app.route('/admin')
async def admin():
    # 不知道能做啥
    await bot.send_private_msg(user_id=2301583973, message='你的主页被访问了')
    return '欢迎来到管理页面'


# @bot.server_app.before_serving
# async def init_db():
#     # 这会在 NoneBot 启动后立即运行
#     print('\n\n\n')
