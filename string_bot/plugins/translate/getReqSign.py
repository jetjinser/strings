import hashlib
from urllib.parse import quote_plus


async def get_req_sign(params, appkey):
    a_list = []
    for key, value in sorted(params.items()):
        if value != '':
            value = quote_plus(value, safe='')
            a_list.append(key + '=' + value + '&')

    a_list.append('app_key=' + appkey)

    a_str = ''.join(a_list)

    sign = await md5(a_str)
    sign = sign.upper()
    return sign


async def md5(b_str):
    m = hashlib.md5()
    m.update(b_str.encode("utf-8"))
    return m.hexdigest()
