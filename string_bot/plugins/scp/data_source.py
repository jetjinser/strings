import requests
import json
from pyquery import PyQuery as pq
import httpx


async def get_scp_daily(index):
    count = 1
    res = requests.get(
        'https://api.bilibili.com/x/space/article?mid=872507&pn=%s&ps=%s&sort=publish_time' % (index, count))
    article_dict = json.loads(res.text)
    first_article = article_dict['data']['articles'][0]
    link = 'https://www.bilibili.com/read/cv' + str(first_article['id'])
    title = first_article['title']
    full_summary = first_article['summary']
    summary = full_summary
    banner_url = first_article['banner_url']
    return {
        'title': title,
        'link': link,
        'summary': summary,
        'banner': banner_url
    }


async def get_latest_article(page_type, page_index):
    article_list = []
    type_str = "created-cn" if page_type == 0 else "created-translated"
    # doc = pq('http://scp-wiki-cn.wikidot.com/most-recently-created-cn/p/1')
    link_str = 'http://scp-wiki-cn.wikidot.com/most-recently-%s/p/%s' % (type_str, page_index)
    doc = pq(link_str)
    for i in list(doc('table>tr').items())[2:]:
        new_article = {}
        info_list = list(i('td').items())
        new_article['title'] = info_list[0]('a').text()
        new_article['link'] = info_list[0]('a').attr('href')
        new_article['created_time'] = info_list[1]('span').text()
        new_article['rank'] = info_list[2].text()
        article_list.append(new_article)
    return article_list


async def get_scp_by_num(scp_num) -> str:
    url = f'http://scp-wiki-cn.wikidot.com/scp-{scp_num}'
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
    html = pq(resp.text)
    page = html('#page-content')
    msg = page.text()
    return msg if len(msg <= 256) else ''
