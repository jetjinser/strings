import urllib.request
import urllib.parse
import json


async def get_translate(content):
    youdao_url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data = {'i': content, 'from': 'AUTO', 'to': 'AUTO', 'smartresult': 'dict', 'client': 'fanyideskweb',
            'salt': '1525141473246', 'sign': '47ee728a4465ef98ac06510bf67f3023', 'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web', 'action': 'FY_BY_CLICKBUTTION', 'typoResult': 'false'}

    data = urllib.parse.urlencode(data).encode('utf-8')

    youdao_response = urllib.request.urlopen(youdao_url, data)
    youdao_html = youdao_response.read().decode('utf-8')
    target = json.loads(youdao_html)

    trans = target['translateResult']
    ret = ''
    for i in range(len(trans)):
        line = ''
        for j in range(len(trans[i])):
            line = trans[i][j]['tgt']
        ret += '译文：' + line

    return ret
