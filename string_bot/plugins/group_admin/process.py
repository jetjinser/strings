import datetime
from sql_exe import *


def timestamp2string(timestamp):
    try:
        d = datetime.datetime.fromtimestamp(timestamp)
        str1 = d.strftime("%Y-%m-%d %H:%M:%S")
        return str1
    except Exception as e:
        return e


def timestamp2date_string(timestamp):
    try:
        d = datetime.datetime.fromtimestamp(timestamp)
        str2 = d.strftime("%Y-%m-%d")
        return str2
    except Exception as e:
        return e


def verify(token):
    sql = (
        'SELECT duration FROM token WHERE token=?;'
    )
    boo = sql_exe(sql, (token,))

    # TODO 入群验证token
    #  1. 入群前验证 content
    #  2. 私聊回复token后向分享群 机器人主动加入 被邀请的全部拒绝

    if boo:
        return boo
    else:
        return
