import requests


async def get_bili_live(bid):
    """
    获取bilibili直播间状态
    :param bid: 直播间id
    :return: 0: 没开播 1: 开播 2: 房间不存在 dict: {}
    """
    url = f'https://api.live.bilibili.com/xlive/web-room/v1/index/getInfoByRoom?room_id={bid}'

    resp = requests.get(url)

    data = resp.json().get('data')
    if data:
        room_info = data['room_info']
        base_info = data['anchor_info']['base_info']

        img = room_info['keyframe']
        title = room_info['title']

        uname = base_info['uname']

        live_dict = {'img': img, 'title': title, 'uname': uname}

        status = room_info.get('live_status')

        if status == 1:
            return 1, live_dict
        else:
            return 0, live_dict
    else:
        return 2, None


async def get_bili_uname_by_room_id(room_id):
    url = 'https://api.live.bilibili.com/room_ex/v1/RoomNews/get'
    params = {'roomid': room_id}

    resp = requests.get(url, params)

    uname = resp.json().get('data').get('uname')

    return uname
