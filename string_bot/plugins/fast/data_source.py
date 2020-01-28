import requests


async def get_time_line_one():
    url = 'http://49.232.173.220:3001/data/getTimelineService'

    resp = requests.get(url)

    data = resp.json()[0]

    pub_date_str = data['pubDateStr']
    title = data['title']
    summary = data['summary']
    info_source = data['infoSource']
    source_url = data['sourceUrl']
    province_name = data['provinceName']

    msg = (title + '\n    <' + pub_date_str + '>    ' + province_name + '\n' + summary + '\n' + info_source + '  '
           + source_url)

    return msg


async def get_statistics(boo: bool):
    url = 'http://49.232.173.220:3001/data/getStatisticsService'

    resp = requests.get(url)

    data = resp.json()

    infect_source = data['infectSource']
    pass_way = data['passWay']
    count_remark = data['countRemark']
    virus = data['virus']

    general_remark = data['generalRemark']
    abroad_remark = data.get('abroadRemark')
    remark = [data.get(f'remark{i}') for i in range(1, 6)]
    remark.extend([general_remark, abroad_remark])

    while "" in remark:
        remark.remove("")

    img_url = data['imgUrl']

    msg1 = virus + '\n' + count_remark

    msg2 = '\n传播途径: ' + pass_way + '\n感染源: ' + infect_source + '\n'.join(remark)

    # 中间插入图片
    if boo:
        msg = msg1 + f'[CQ:image,file={img_url}]' + msg2
    else:
        msg = msg1 + img_url + msg2

    return msg


async def get_area_stat(province='福建'):
    url = f'http://49.232.173.220:3001/data/getAreaStat/{province}'

    resp = requests.get(url)
    if not resp.json():
        return
    data = resp.json()[0]

    province_name = data['provinceShortName']
    confirmed_count = data['confirmedCount']
    suspected_count = data['suspectedCount']

    cured_count = data['curedCount']
    dead_count = data['deadCount']

    comment = data['comment']

    cities_dict_list = data['cities']

    cities_name = [cities_name.get('cityName') for cities_name in cities_dict_list]

    msg = (province_name + '\n确认感染人数: ' + str(confirmed_count) + '\n疑似感染人数: ' + str(suspected_count)
           + '\n治愈人数: ' + str(cured_count) + '\n死亡人数: ' + str(dead_count) + '\n' + comment
           + '\n回复下辖区可查看详情(支持: ' + ', '.join(cities_name) + ')')

    return msg, cities_name, cities_dict_list


async def get_area_stat_2(cities_name, cities_dict_list, city):
    index = len(cities_name) - 1
    cities_confirmed_count = cities_dict_list[index].get('confirmedCount')
    cities_suspected_count = cities_dict_list[index].get('suspectedCount')
    cities_cured_count = cities_dict_list[index].get('curedCount')
    cities_dead_count = cities_dict_list[index].get('deadCount')

    city_msg = (city + '\n确认感染人数: ' + str(cities_confirmed_count) + '\n疑似感染人数: ' + str(cities_suspected_count)
                + '\n治愈人数: ' + str(cities_cured_count) + '\n死亡人数: ' + str(cities_dead_count))

    return city_msg


async def get_rumor_list():
    url = 'http://49.232.173.220:3001/data/getIndexRumorList'

    resp = requests.get(url)

    data = resp.json()

    rumor_list = []
    for i in data:
        title = i['title'] + '    ' + i['mainSummary'] + '\n' + i['summary'] + i['body']
        rumor_list.append(title)

    return rumor_list


async def get_recommend_list():
    url = 'http://49.232.173.220:3001/data/getIndexRecommendList'

    resp = requests.get(url)

    data = resp.json()

    rumor_list = []
    for i in data:
        title = i['title'] + '\n' + i['linkUrl']
        rumor_list.append(title)

    return rumor_list


async def get_wiki():
    url = 'http://49.232.173.220:3001/data/getWikiList'
    resp = requests.get(url)

    data = resp.json()['result']

    wiki_list = []
    for wiki in data:
        msg = wiki['title'] + '\n' + wiki['linkUrl']
        wiki_list.append(msg)

    return wiki_list
