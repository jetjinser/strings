from nonebot import CommandGroup, CommandSession
from .data_source import *

time_line_cmd = ['武汉肺炎最新动态', '新肺炎最新动态', '最新动态']
statistics_cmd = ['武汉肺炎', '武汉肺炎情况', '新肺炎', '新肺炎情况', '最新情况']
area_stat_cmd = ['省份情况', '地区情况']
rumor_cmd = ['最新辟谣', '辟谣动态', '新肺炎辟谣']
recommend_cmd = ['最新防护知识', '防护知识']
temp1_cmd = ['诊疗信息']
temp2_cmd = ['肺炎wiki', '诊疗百科', '医疗百科', 'wiki']
donate_cmd = ['捐赠信息', '捐赠']


def f_cmd(*args: list):
    cmd_list = []
    for cmd in args:
        cmd_str = ' / '.join(cmd)
        cmd_list.append(cmd_str)
    return ' | '.join(cmd_list)


__plugin_name__ = '新肺炎动态'
__plugin_usage__ = fr"""获取新肺炎动态
来自 https://juejin.im/post/5e2c6a6e51882526b757cf2e

指令: {f_cmd(time_line_cmd, statistics_cmd, area_stat_cmd, rumor_cmd, temp1_cmd, temp2_cmd, donate_cmd)}"""

cg = CommandGroup('fast', only_to_me=False)


@cg.command('time_line', aliases=time_line_cmd)
async def fast_time_line(session: CommandSession):
    msg = await get_time_line_one()
    await session.send(msg)


@cg.command('statistics', aliases=statistics_cmd)
async def fast_statistics(session: CommandSession):
    bot = session.bot
    boo = await bot.can_send_image()
    boo = boo['yes']

    msg = await get_statistics(boo)
    await session.send(msg)


@cg.command('area_stat', aliases=area_stat_cmd)
async def fast_area_stat(session: CommandSession):
    province = session.get('province', prompt='要查询哪个省份?')

    try:
        msg, cities_name, cities_dict_list = await get_area_stat(province)
        city = session.get('city', prompt=msg)

        if city in cities_name:
            city_msg = await get_area_stat_2(cities_name, cities_dict_list, city)
            await session.send(city_msg)
        else:
            await session.send("城市名不存在，会话结束")
    except TypeError:
        session.finish('无数据, 请确认输入是否正确')


@cg.command('rumor', aliases=rumor_cmd)
async def fast_rumor(session: CommandSession):
    # 怪怪怪, 傻傻傻
    next_cmd = ['next', '下一条']
    msg_list = await get_rumor_list()
    m = f'\n回复{" / ".join(next_cmd)}来查看下一条⎘'
    whether_next = session.get('whether_next', prompt=msg_list[0] + m)
    if whether_next in next_cmd:
        whether_next2 = session.get('whether_next2', prompt=msg_list[1] + m)
        if whether_next2 in next_cmd:
            whether_next3 = session.get('whether_next3', prompt=msg_list[2] + m)
            if whether_next3 in next_cmd:
                session.finish('暂时没有更多了')
            else:
                return
        else:
            return
    else:
        return


@cg.command('recommend', aliases=recommend_cmd)
async def fast_recommend(session: CommandSession):
    msg = await get_recommend_list()
    f_msg = '\n'.join(msg)
    await session.send(f_msg)


@cg.command('temp1', aliases=temp1_cmd)
async def fast_temp1(session: CommandSession):
    msg = '''全国发热门诊: 
https://assets.dxycdn.com/gitrepo/tod-assets/output/default/pneumonia/index.htm
在线义诊: 
https://ask.dxy.com/ama/index#/activity-share?activity_id=111&dxa_adplatform=yqdtyz'''
    await session.send(msg)


@cg.command('temp2', aliases=temp2_cmd)
async def fast_temp2(session: CommandSession):
    msg = await get_wiki()
    f_msg = '\n'.join(msg)
    await session.send(f_msg)

@cg.command('donate', aliases=donate_cmd)
async def fast_donate(session: CommandSession):
    msg = '''湖北抗疫物资+捐赠信息汇总（持续更新）
    https://shimo.im/docs/wDtQpGCgghWkgVxD/read'''
    await session.send(msg)
