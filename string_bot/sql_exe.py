import sqlite3


def sql_exe(sql, args: tuple = None):
    coon = sqlite3.connect('./data/data.db')
    cursor = coon.cursor()
    if isinstance(sql, list):
        for s in sql:
            if args:
                cursor.execute(s, args)
            else:
                cursor.execute(s)
    else:
        if args:
            cursor.execute(sql, args)
        else:
            cursor.execute(sql)

    values = cursor.fetchall()

    if values:
        cursor.close()
        coon.commit()
        coon.close()
        return values
    else:
        cursor.close()
        coon.commit()
        coon.close()
        return
