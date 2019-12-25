from random import randint
from datetime import datetime
import sqlite3


# 用户注册函数
def user_registration(ctx):
    coon = sqlite3.connect('./data/data.db')
    cursor = coon.cursor()

    user_id = ctx['sender']['user_id']
    user_nickname = ctx['sender']['nickname']
    user_card = ctx.get('sender').get('card') if ctx.get('sender').get('card') else 'NULL'

    sql_insert = (
        'INSERT INTO user VALUES ('
        f'NULL, {user_id}, \'{user_nickname}\', {user_card}, {0}, {0}, {0}, \'2019-01-01\');'
    )

    cursor.execute(sql_insert)

    cursor.close()
    coon.commit()
    coon.close()


# 用户好感算法
def favor_algorithm(cid: int, favor: int):  # check_in_days, favor
    if cid <= 10:
        return favor + randint(1, 2)
    elif 10 < cid <= 20:
        return favor + randint(2, 3)
    elif 20 < cid == 30:
        return favor + randint(3, 4)
    elif cid == 30:
        return favor + 30
    elif 30 < cid <= 40:
        return favor + randint(4, 5)
    elif 40 < cid <= 50:
        return favor + randint(5, 6)
    else:
        return favor + randint(5, 10)


# 用户铜币算法
def coin_algorithm(favor: int, coin: int):  # favor
    if favor <= 10:
        return coin + randint(10, 20)
    elif 10 < favor <= 20:
        return coin + randint(20, 30)
    elif 20 < favor == 30:
        return coin + randint(30, 40)
    elif favor == 30:
        return coin + 300
    elif 30 < favor <= 40:
        return coin + randint(40, 50)
    elif 40 < favor <= 50:
        return coin + randint(50, 60)
    else:
        return coin + randint(50, 100)


# 签到函数
def chick_in(user_id: int):
    coon = sqlite3.connect('./data/data.db')
    cursor = coon.cursor()

    data = get_chick_info(user_id)
    user_coin = data[4]
    user_favor = data[5]
    chick_in_days = data[6]

    up_user_coin = coin_algorithm(user_favor, user_coin)
    up_user_favor = favor_algorithm(chick_in_days, user_favor)
    up_chick_in_days = chick_in_days + 1
    up_last_chick_in_time = datetime.today().strftime("%Y-%m-%d")

    sql_update = (
        'UPDATE user SET '
        'user_coin = ?,'
        f'user_favor = ?,'
        f'chick_in_days = ?,'
        f'last_chick_in_time = ? '
        f'WHERE user_id = ?;'
    )

    cursor.execute(sql_update, (up_user_coin, up_user_favor, up_chick_in_days, up_last_chick_in_time, user_id))

    cursor.close()
    coon.commit()
    coon.close()


# 验证是否在一天内重复签到
def check_in_interval_judgment(user_id: int):
    coon = sqlite3.connect('./data/data.db')
    cursor = coon.cursor()

    sql_select = (
        f'select * from user where user_id={user_id};'
    )

    cursor.execute(sql_select)

    data = cursor.fetchall()
    data = data[0]

    cursor.close()
    coon.commit()
    coon.close()

    if data[7] == datetime.today().strftime('%Y-%m-%d'):
        return False
    else:
        return True


def get_chick_info(user_id: int):
    coon = sqlite3.connect('./data/data.db')
    cursor = coon.cursor()

    sql_select = (
        f'select * from user where user_id={user_id};'
    )

    cursor.execute(sql_select)

    data = cursor.fetchall()

    cursor.close()
    coon.commit()
    coon.close()

    return data[0]


def user_registration_interval_judgment(user_id):
    coon = sqlite3.connect('./data/data.db')
    cursor = coon.cursor()

    sql_select = (
        f"select 1 from user where user_id = ? limit 1;"
    )

    cursor.execute(sql_select, (user_id,))
    values = cursor.fetchall()

    cursor.close()
    coon.commit()
    coon.close()

    if values:
        return False
    else:
        return True


def chick_in_text(user_id: int, name: str) -> str:
    data = get_chick_info(user_id)
    coin = data[4]
    favor = data[5]
    cid = data[6]
    text = f'{name}\n签 到 成 功\nCuprum {coin}\n签到天数    {cid}     好感度    {favor}'
    return text


def get_chick_in_check(user_id: int) -> str:
    data = get_chick_info(user_id)
    name = data[2]
    coin = data[4]
    favor = data[5]
    cid = data[6]
    text = f'{name}\nCuprum {coin}\n签到天数    {cid}     好感度    {favor}'
    return text
