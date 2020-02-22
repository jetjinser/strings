import datetime


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
