from nonebot import on_command, CommandSession


@on_command('签到')
async def _(session: CommandSession):
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
