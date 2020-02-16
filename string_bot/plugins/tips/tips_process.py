from sql_exe import *
from datetime import datetime
from .cuprum import *


async def submit_ust(tips, user_id):
    if await cuprum(user_id, 20):
        try:
            sql_select = (
                'SELECT * FROM user WHERE user_id=?;'
            )

            data = sql_exe(sql_select, (user_id,))[0]

            user_nickname = data[2]
            user_card = data[3]

            sql_insert = (
                'INSERT INTO ust VALUES (NULL, ?, ?, ?, ?, ?, ?)'
            )

            params = (user_id, user_nickname, user_card, tips, datetime.today().strftime("%Y-%m-%d"), 0)

            sql_exe(sql_insert, params)
        except IndexError:
            return '提交失败, 请先注册(输入"注册")'

        return '提交成功, 审核中'
    else:
        return '铜币不足'


async def modify_ust(tips, user_id, tips_id):
    if await cuprum(user_id, 5):
        try:
            sql_select = (
                'SELECT * FROM ust WHERE user_id=?'
            )

            user_id_for_verify = sql_exe(sql_select, (user_id,))
            user_id_for_verify = [i[0] for i in user_id_for_verify]

            if int(tips_id) in user_id_for_verify:
                sql_select2 = (
                    'SELECT * FROM ust WHERE id=?'
                )
                values = sql_exe(sql_select2, (tips_id,))[0]
                before = values[4]

                sql_update = (
                    'UPDATE ust SET tips=? WHERE id = ?;'
                )
                sql_exe(sql_update, (tips, tips_id))

                return f'修改成功, {before} -> {tips}'
            else:
                return '请检查id是否正确'
        except sqlite3.OperationalError:
            return '当前没有审核中的tips'
    else:
        return '铜币不足'


async def move_in_tips(tips_id):
    sql_select = (
        'SELECT tips FROM ust WHERE id=?;'
    )
    tip = sql_exe(sql_select, (tips_id,))[0][0]

    sql_insert = (
        'INSERT INTO tips VALUES (NULL, ?)'
    )

    sql_exe(sql_insert, (tip,))


async def get_ust(user_id, tips_id):
    sql_select = (
        'SELECT * FROM ust WHERE id=? and user_id=?'
    )
    values = sql_exe(sql_select, (tips_id, user_id))[0]

    return values[4]


async def get_ust_msg(user_id, nah=True):
    try:
        if nah:
            sql_select = (
                'SELECT * FROM ust WHERE user_id=? and audit=?;'
            )
            data = sql_exe(sql_select, (user_id, 0))
        else:
            sql_select = (
                'SELECT * FROM ust WHERE user_id=?;'
            )
            data = sql_exe(sql_select, (user_id,))

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
        sql_select = (
            'select ? from ust where id=? limit 1;'
        )
        values = sql_exe(sql_select, (tips_id, tips_id))

        if values:
            sql_delete = (
                'DELETE FROM ust WHERE user_id=? and id=?;'
            )
            sql_exe(sql_delete, (user_id, tips_id))
            return '删除成功'
        else:
            return '失败, id不存在'
    else:
        return '铜币不足'


async def audit_ust():
    try:
        sql_select = (
            'select * from ust where audit=0 limit 1;'
        )

        values = sql_exe(sql_select)[0]

        aud_id = values[0]
        values = 'id: ' + str(aud_id) + '  ' + values[4] + '  ' + values[5]

        return values, aud_id
    except IndexError:
        return '', None


async def audit(tips_id, audit_bool):
    if audit_bool == '好':
        sql_update = (
            'UPDATE ust SET audit=1 WHERE id=?;'
        )

        sql_exe(sql_update, (tips_id,))

        return True
    else:
        sql_update = (
            'DELETE FROM ust WHERE id=?;'
        )

        sql_exe(sql_update, (tips_id,))

        return False


async def already_exists(submit_tip):
    sql = (
        'SELECT tips FROM tips;'
    )
    tips = sql_exe(sql)

    sql2 = (
        'SELECT tips FROM ust;'
    )
    tips2 = sql_exe(sql2)

    if submit_tip in tips or submit_tip in tips2:
        return False
    else:
        return True
