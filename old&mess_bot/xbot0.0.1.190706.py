from pprint import pprint
import random, time, sys
from plugins import *
from urllib import parse
from check_in_system import chick_in, get_chick_info, check_in_interval_judgment, user_registration, get_user_info

from translate import youdao_tdayranslate

from image_processing import ImageProcessing

from cqhttp import CQHttp

import tuling

bot = CQHttp(api_root='http://127.0.0.1:5700')


count = set()
commands = {}



def commond(name):
    def decorator(func):
        commands[name] = func
        return func

    return decorator


@commond('echo')
def _(ctx, arg):
    bot.send(ctx, arg)
#
@commond('嘤一个')
def _(ctx, arg):
    bot.send(ctx, '嘤嘤嘤')

@commond('随机数')
def _(ctx, arg):
    bot.send(ctx, str(random.randint(0,1000)))

# @commond('计算')
# def _(ctx, arg):
#     expression = arg.strip()
#     bot.send(ctx, message=str(eval(expression)))

@commond('百度')
def _(ctx, arg):
    bot.send(ctx, shortlink('https://nbhbdm.cn/?s={urlcode}'.format(urlcode=parse.quote(arg))))

@commond('bing')
def _(ctx, arg):
    bot.send(ctx, shortlink('https://cn.bing.com/search?q={}&qs=n&form=QBLH&sp=-1&pq={}&sc=9-1&sk=&cvid=615CA68D005E42A9BEC68D49246C1C11'.format(parse.quote(arg),parse.quote(arg))))

@commond('翻译')
def _(ctx, arg):
    bot.send(ctx, youdao_translate(arg))

@commond('天气')
def _(ctx, arg):
    try:
        city, date = arg.split()
        if date == '明天':
            date = 1
        elif date == '后天':
            date = 2
        elif date ==  '大后天':
            date = 3
        elif date == '大大后天':
            date = 4
        bot.send(ctx, weather(city, int(date)))
    except ValueError:
        bot.send(ctx, weather(arg))

@commond('日历')
def _(ctx, arg):
    bot.send(ctx, today(arg))

@commond('bpi')
def _(ctx, arg):
    bot.send(ctx, bitcoin())

# @commond('bookadd')
# def _(ctx, arg):
#     try:
#         a, b = arg.split(' ')
#         bot.send(ctx, add(a, b))
#     except:
#         bot.send(ctx, 'error')
#
# @commond('书摘')
# def _(ctx, arg):
#     bot.send(ctx, book())
#
# @commond('delete')
# def _(ctx, arg):
#     try:
#         bot.send(ctx, delete(int(arg)))
#     except:
#         bot.send(ctx, 'error')
#
# @commond('booklist')
# def _(ctx, arg):
#     try:
#         bot.send(ctx, booklist())
#     except:
#         bot.send(ctx, 'error')

@commond('色图来')
def _(ctx, arg):
    try:
        try:
            bot.send(ctx, '[CQ:image,file=%s.jpg]' % arg)
        except:
            try:
                bot.send(ctx, '[CQ:image,file=%s.png]' % arg)
            except:
                bot.send(ctx, '[CQ:image,file=%s.gif]' % arg)
    except:
        bot.send(ctx, '莫得%s' % arg)

@commond('英名性别')
def _(ctx, arg):
    bot.send(ctx, gender(arg))

@commond('找点乐子')
def _(ctx, arg):
    bot.send(ctx, ramdom_things())

@commond('生成二维码')
def _(ctx, arg):
    bot.send(ctx, QR(arg))

@commond('添加')
def _(ctx, arg):
    if ctx['sender']['user_id'] == 2301583973:
        number = tips_writer(arg)
        bot.send(ctx, '写入成功, 当前已有 %d 条' % (number + 1))
    else:
        bot.send(ctx, '权限不足')

@commond('say')
def _(ctx, arg):
    if ctx['sender']['user_id'] == 2301583973:
        content, group = arg.split()
        ctx = {'anonymous': None,
 'font': 44291352,
 'group_id': group,
 'message': '',
 'message_id': 21146,
 'message_type': 'group',
 'post_type': 'message',
 'raw_message': '',
 'self_id': 3289927080,
 'sender': {'age': 15,
            'area': '',
            'card': '黄盈',
            'level': '活跃',
            'nickname': 'Echo.',
            'role': 'member',
            'sex': 'female',
            'title': '',
            'user_id': 2311699891},
 'sub_type': 'normal',
 'time': 1574339412,
 'user_id': 2311699891}
        bot.send(ctx, content)


@bot.on_message()
def handle_msg(ctx):
    # pprint(ctx)
    msg: str = ctx['message']
    sp = msg.split(maxsplit=1)
    if not sp:
        return

    cmd, *args = sp
    arg = ''.join(args)

    handler = commands.get(cmd)

    if handler:
        return handler(ctx, arg)


    if '机屑人' in msg and random.randint(0, 10) < 5:
        bot.send(ctx, '你才是机屑人')
    elif msg == '草' and random.randint(0, 10) < 6:
        bot.send(ctx, '草')
    elif '五十弦' in msg:
        bot.send(ctx, '干嘛')
    elif 'mua' in msg:
        if random.randint(0,1000) < 500:
            bot.send(ctx, '呕呕!谁想和死肥宅亲亲啊!kimo!')
        else:
            bot.send(ctx, 'mua')
    elif 'zaima' in msg:
        bot.send(ctx, 'buzai,cnm')
    elif msg == '你好':
        bot.send(ctx, '泥嚎，我很阔爱，请给我钱')
    elif msg == '每日一句':
        bot.send(ctx, daily())
    elif msg == '我是谁' or msg == '我是谁？' or msg == '1':
        bot.send(ctx, ctx['sender']['nickname'])
    elif msg == 'five语录':
        bot.send(ctx, five())
    elif msg.endswith('是什么垃圾') or msg.endswith('属于什么垃圾'):
        bot.send(ctx, laji(msg[:-5]))
    elif (msg.startswith('！') or msg.startswith('!')) and len(msg) >= 4:
        try:
            if msg[1:] == '一个顶俩':
                bot.send(ctx, '一个顶俩鲨了')
            else:
                bot.send(ctx, jielong(msg[1:]))
        except:
            bot.send(ctx, '莫得')
    elif msg == '历史上的今天':
        bot.send(ctx, his())
    elif msg == '今日历':
        bot.send(ctx, today())
    elif msg == '段子':
        bot.send(ctx, joke())
    elif msg == '新闻':
        bot.send(ctx, news())
    elif '？' in msg and random.randint(0,10) > 8:
        bot.send(ctx, '嗯')

    elif (('色图' in msg or '涩图' in msg or '瑟图' in msg) and random.randint(0, 10) < 6 and not
    (msg == '瑟图在线' or msg == '涩图在线' or msg == '色图在线')) \
            or msg == '色图魔法':
        n = random.randint(1, 134)
        try:
            try:
                bot.send(ctx, '[CQ:image,file=%d.jpg]' % n)
            except:
                try:
                    bot.send(ctx, '[CQ:image,file=%d.png]' % n)
                except:
                    bot.send(ctx, '[CQ:image,file=%d.gif]' % n)
        except:
            bot.send(ctx, '我已经一滴都没有了')
    elif msg == '色图在线' or msg == '涩图在线' or msg == '瑟图在线':
        import time
        try:
            start = time.time()
            bot.send(ctx, '在线搜寻中......这个过程将会耗费一些时间')
            # bot.send(ctx, 'pid: {}'.format(setu()[0]))
            bot.send(ctx, '[CQ:image,file={}]'.format(setu()))
            end = time.time()
            time = end - start
            bot.send(ctx, '用时%.3fs' % time)
        except:
            bot.send(ctx, 'error')
    elif msg == 'mito':
        bot.send(ctx, '[CQ:image,file=https://nijisanji.ichikara.co.jp/wp-content/uploads/elementor/thumbs/%E6%9C%88%E3%'
                      '83%8E%E7%BE%8E%E5%85%8E%E9%80%9A%E5%B8%B8_1-e1549528387192-o35s233kw988aand6zwc8avw4x228z5dhh21ea'
                      'xe6c.png]')

    elif msg == '林檎':
        bot.send(ctx, '[CQ:record,file=爱小姐我老婆.amr]')
    elif msg == '熊猫人唱歌':
        bot.send(ctx, '[CQ:record,file=熊猫人唱歌啦.mp3]')
    elif msg == 'baka' or msg == '笨蛋':
        bot.send(ctx, '[CQ:record,file=baka.mp3]')


    elif msg == '来了' and random.randint(0, 10) > 3:
        bot.send(ctx, '[CQ:image,file=来了.gif]')
    elif msg == 'hso' and random.randint(0, 10) > 8:
        bot.send(ctx, '[CQ:image,file=hso.jpg]')
    elif '好看' in msg and random.randint(0, 10) > 6:
        if random.randint(0, 10) > 2:
            bot.send(ctx, '[CQ:image,file=好看.jpg]')
        elif random.randint(0, 10) > 4:
            bot.send(ctx, '[CQ:image,file=别的女人好看.jpg]')
        else:
            bot.send(ctx, '[CQ:image,file=看别的女人.jpg]')
    elif '冲' in msg and random.randint(0, 10) > 6:
        if random.randint(0, 10) > 3:
            bot.send(ctx, '[CQ:image,file=来冲.jpg]')
        elif random.randint(0, 10) > 6:
            bot.send(ctx, '[CQ:image,file=冲.jpg]')
        else:
            bot.send(ctx, '[CQ:image,file=打手冲.jpg]')
    elif '可爱' in msg and random.randint(0, 10) > 8:
        bot.send(ctx, '[CQ:image,file=她好可爱.jpg]')
    elif '攻击' in msg and random.randint(0, 10) > 6:
        bot.send(ctx, '[CQ:image,file=攻击.jpg]')
    elif msg == '理解理解' and random.randint(0, 10) > 5:
        bot.send(ctx, '[CQ:image,file=理解理解.jpg]')
    elif ('性癖' in msg or 'xp' in msg) and random.randint(0, 10) > 4:
        bot.send(ctx, '[CQ:image,file=性癖.jpg]')
    elif '素质屌差' in msg and random.randint(0, 10) > 3:
        bot.send(ctx, '[CQ:image,file=素质屌差.jpg]')
    elif '爆肝' in msg and random.randint(0, 10) > 6:
        bot.send(ctx, '[CQ:image,file=爆肝.jpg]')

    elif '晚安' == msg:
        bot.send(ctx, '嗯,晚安')

    elif msg == '注册':
        user_id = ctx['sender']['user_id']
        data = get_user_info()
        if user_id not in data.keys():
            user_registration(ctx)
            bot.send(ctx, '注册成功!')
        else:
            bot.send(ctx, '您已经注册过了')

    elif msg == '签到':
        try:
            user_id = ctx['sender']['user_id']
            if check_in_interval_judgment(str(user_id)):
                # 获取对象QQ头像
                image = get_image(user_id)

                chick_in(user_id)

                data = get_chick_info(str(user_id))
                coin = data['user_coin']
                CID = data['check_in_days']
                favor = data['user_favorability']

                card = ctx['sender']['card']
                if card:
                    text = '{}\n签 到 成 功\nCuprum {}\n签到天数    {}     好感度    {}'.format(card, coin, CID, favor)
                else:
                    nickname = ctx['sender']['nickname']
                    text = '{}\n签 到 成 功\nCuprum {}\n签到天数:   {}     好感度:   {}'.format(nickname, coin, CID, favor)

                # 实例化图片对象
                image = ImageProcessing(image, text, 256, 'send')
                image.save()
                try:
                    bot.send(ctx, '[CQ:image,file={}]'.format('send.jpg'))
                except:
                    bot.send(ctx, '{}\n签 到 成 功\nCuprum {}\n签到天数    {}     好感度    {}'.format(card, coin, CID, favor))
                print('success')
            else:
                bot.send(ctx, '您今天已经签到过了')
        except KeyError:
            bot.send(ctx, '请发送"注册"  来完成注册!')

bot.run('127.0.0.1',8080)