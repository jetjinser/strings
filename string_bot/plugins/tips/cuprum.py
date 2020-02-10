import sqlite3


async def cuprum(user_id, num=None):
    try:
        coon = sqlite3.connect('./data/data.db')
        cursor = coon.cursor()

        sql_select = (
            'SELECT user_coin FROM user WHERE user_id=?;'
        )

        cursor.execute(sql_select, (user_id,))
        values = cursor.fetchall()[0][0]

        if values - num < 0:
            cursor.close()
            coon.commit()
            coon.close()
            return False
        else:
            updated_num = values - num
            sql_update = (
                'UPDATE user SET user_coin=? WHERE user_id=?;'
            )

            cursor.execute(sql_update, (updated_num, user_id))

            cursor.close()
            coon.commit()
            coon.close()

            return num
    except IndexError:
        return '请先注册'


async def get_cuprum(user_id):
    try:
        coon = sqlite3.connect('./data/data.db')
        cursor = coon.cursor()

        sql_select = (
            'SELECT user_coin FROM user WHERE user_id=?;'
        )

        cursor.execute(sql_select, (user_id,))
        coin = cursor.fetchall()[0][0]

        cursor.close()
        coon.commit()
        coon.close()

        return coin
    except IndexError:
        return

