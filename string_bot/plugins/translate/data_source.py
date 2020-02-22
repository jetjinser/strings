from .getReqSign import get_req_sign
import time
import requests
from jieba import posseg


async def get_translate(content, app_key):
    url = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_texttranslate'

    t = str(time.time())
    nonce_str = t

    lan = posseg.lcut(content)
    for i in lan:
        if i.flag not in ('eng', 'x'):
            target = 'zh'
            break
    else:
        target = 'en'

    params = {'app_id': '2127385692', 'time_stamp': t, 'nonce_str': nonce_str,
              'sign': '', 'text': content, 'source': 'zh', 'target': target}

    sign = get_req_sign(params, app_key)
    params['sign'] = sign

    resp = requests.get(url, params)

    return resp.json()['data']['target_text']
