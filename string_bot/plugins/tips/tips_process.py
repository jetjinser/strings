import sqlite3
from datetime import datetime
from .cuprum import *


async def submit_ust(tips, user_id):
    if await cuprum(user_id, 20):
        try:
            coon = sqlite3.connect(r'.\data\data.db')
            cursor = coon.cursor()

            sql_select = (
                'SELECT * FROM user WHERE user_id=?;'
            )

            cursor.execute(sql_select, (user_id,))
            data = cursor.fetchall()[0]

            user_nickname = data[2]
            user_card = data[3]

            sql_insert = (
                'INSERT INTO ust VALUES (NULL, ?, ?, ?, ?, ?, ?)'
            )

            params = (user_id, user_nickname, user_card, tips, datetime.today().strftime("%Y-%m-%d"), 0)

            cursor.execute(sql_insert, params)

            cursor.close()
            coon.commit()
            coon.close()
        except IndexError:
            return '提交失败, 请先注册(输入"注册")'

        return '提交成功, 审核中'
    else:
        return '铜币不足'


async def modify_ust(tips, user_id, tips_id):
    if await cuprum(user_id, 5):
        try:
            coon = sqlite3.connect(r'.\data\data.db')
            cursor = coon.cursor()

            sql_select = (
                'SELECT * FROM ust WHERE user_id=?'
            )

            cursor.execute(sql_select, (user_id,))
            user_id_for_verify = cursor.fetchall()
            user_id_for_verify = [i[0] for i in user_id_for_verify]

            if int(tips_id) in user_id_for_verify:
                sql_select2 = (
                    'SELECT * FROM ust WHERE id=?'
                )
                cursor.execute(sql_select2, (tips_id,))
                values = cursor.fetchall()[0]
                before = values[4]

                sql_update = (
                    'UPDATE ust SET tips=? WHERE id = ?;'
                )

                cursor.execute(sql_update, (tips, tips_id))

                cursor.close()
                coon.commit()
                coon.close()

                return f'修改成功, {before} -> {tips}'

            else:
                cursor.close()
                coon.commit()
                coon.close()

                return '请检查id是否正确'
        except sqlite3.OperationalError:
            return '当前没有审核中的tips'
    else:
        return '铜币不足'


async def move_in_tips(tips_id):
    coon = sqlite3.connect(r'.\data\data.db')
    cursor = coon.cursor()

    sql_select = (
        'SELECT tips FROM ust WHERE id=?;'
    )

    cursor.execute(sql_select, (tips_id,))
    tip = cursor.fetchall()[0][0]

    sql_insert = (
        'INSERT INTO tips VALUES (NULL, ?)'
    )

    cursor.execute(sql_insert, (tip,))

    cursor.close()
    coon.commit()
    coon.close()


async def get_ust(user_id, tips_id):
    coon = sqlite3.connect(r'.\data\data.db')

    cursor = coon.cursor()

    sql_select = (
        'SELECT * FROM ust WHERE id=? and user_id=?'
    )

    cursor.execute(sql_select, (tips_id, user_id))
    values = cursor.fetchall()[0]

    return values[4]


async def get_ust_msg(user_id, nah=True):
    try:
        coon = sqlite3.connect(r'.\data\data.db')
        cursor = coon.cursor()

        if nah:
            sql_select = (
                'SELECT * FROM ust WHERE user_id=? and audit=?;'
            )

            cursor.execute(sql_select, (user_id, 0))
            data = cursor.fetchall()
        else:
            sql_select = (
                f'SELECT * FROM ust WHERE user_id=?;'
            )

            cursor.execute(sql_select, (user_id,))
            data = cursor.fetchall()

        cursor.close()
        coon.commit()
        coon.close()

        data = [i for i in data]

        user_nickname = data[0][2]

        msg = ['id: ' + str(x[0]) + '  ' + x[4] + '  ' + x[5] for x in data]
        msg = [''.join(y) for y in msg]

        text = '\n'.join(msg)
        text = user_nickname + '\n' + text

        return text
    except IndexError:
        return '审核队列中无数据'


async def delete_ust(user_id, tips_id):
    if await cuprum(user_id, 1):
        coon = sqlite3.connect(r'.\data\data.db')
        cursor = coon.cursor()

        sql_select = (
            'select ? from ust where id=? limit 1;'
        )

        cursor.execute(sql_select, (tips_id, tips_id))
        values = cursor.fetchall()

        if values:
            sql_delete = (
                'DELETE FROM ust WHERE user_id=? and id=?;'
            )

            cursor.execute(sql_delete, (user_id, tips_id))

            cursor.close()
            coon.commit()
            coon.close()

            return '删除成功'
        else:
            cursor.close()
            coon.commit()
            coon.close()

            return '失败, id不存在'
    else:
        return '铜币不足'


async def audit_ust():
    try:
        coon = sqlite3.connect(r'.\data\data.db')
        cursor = coon.cursor()

        sql_select = (
            'select * from ust where audit=0 limit 1;'
        )

        cursor.execute(sql_select)
        values = cursor.fetchall()[0]

        aud_id = values[0]
        values = 'id: ' + str(aud_id) + '  ' + values[4] + '  ' + values[5]

        return values, aud_id
    except IndexError:
        return '', None


async def audit(tips_id, audit_bool):
    coon = sqlite3.connect(r'.\data\data.db')
    cursor = coon.cursor()

    if audit_bool == '好':
        sql_update = (
            'UPDATE ust SET audit=1 WHERE id=?;'
        )

        cursor.execute(sql_update, (tips_id,))

        cursor.close()
        coon.commit()
        coon.close()

        return True
    else:
        sql_update = (
            'DELETE FROM ust WHERE id=?;'
        )

        cursor.execute(sql_update, (tips_id,))

        cursor.close()
        coon.commit()
        coon.close()

        return False
