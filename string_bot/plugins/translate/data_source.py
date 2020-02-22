from .getReqSign import get_req_sign
import time
import requests
from urllib.parse import quote


async def get_translate(content, app_key):
    url = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_texttranslate'

    t = str(time.time())
    nonce_str = t

    boo = await is_contain_chinese(content)
    if boo:
        target = 'zh'
    else:
        target = 'en'

    content = quote(content, safe='')

    params = {'app_id': '2127385692', 'time_stamp': t, 'nonce_str': nonce_str,
              'sign': '', 'text': content, 'source': 'auto', 'target': target}

    sign = await get_req_sign(params, app_key)
    params['sign'] = sign

    resp = requests.get(url, params)

    print(resp.json())

    return resp.json()['data']['target_text']


async def is_contain_chinese(check_str):
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            print('\n\n\n')
            return True
    return False
