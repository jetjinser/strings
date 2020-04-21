"""
a sql execute module
"""
import sqlite3
from typing import Union, List


def sql_exe(sql, args: tuple = None) -> Union[List[set], None]:
    """
    a sql execute function
    :param sql: sql language sentence
    :param args: sql language args
    :return: fetched value or None
    """
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

    cursor.close()
    coon.commit()
    coon.close()

    if values:
        return values
    else:
        return None
