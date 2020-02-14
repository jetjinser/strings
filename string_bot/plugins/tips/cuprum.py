from sql_exe import *


async def cuprum(user_id, num=None):
    try:
        sql_select = (
            'SELECT user_coin FROM user WHERE user_id=?;'
        )

        values = sql_exe(sql_select, (user_id,))[0][0]

        if values - num < 0:
            return False
        else:
            updated_num = values - num
            sql_update = (
                'UPDATE user SET user_coin=? WHERE user_id=?;'
            )

            sql_exe(sql_update, (updated_num, user_id))

            return num
    except IndexError:
        return '请先注册'


async def get_cuprum(user_id):
    try:
        sql_select = (
            'SELECT user_coin FROM user WHERE user_id=?;'
        )

        coin = sql_exe(sql_select, (user_id,))[0][0]

        return coin
    except IndexError:
        return
