import json
from random import randint
import time

def user_registration(ctx):
    with open('./data/user.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    user_id = ctx['sender']['user_id']
    user_nickname = ctx['sender']['nickname']
    user_card = ctx['sender']['card']

    data[str(user_id)] = {
        "user_nickname": user_nickname,
        "user_card": user_card,
        "user_coin": 0,
        "user_favorability": 0,
        "check_in_days": 0,
        "last_check_in_time": ""
    }

    file = open('./data/user.json', 'w', encoding='utf-8')
    json.dump(data, file, ensure_ascii=False, indent=4)

def favor_algorithm(CID: int, favor: int):  # check_in_days, favorability
    if CID <= 10:
        return favor + randint(1, 2)
    elif 10 < CID <= 20:
        return favor + randint(2, 3)
    elif 20 < CID == 30:
        return favor + randint(3, 4)
    elif CID == 30:
        return favor + 30
    elif 30 < CID <= 40:
        return favor + randint(4, 5)
    elif 40 < CID <= 50:
        return favor + randint(5, 6)
    else:
        return favor + randint(5, 10)

def coin_algorithm(favor:int, coin: int):   # favorability
    if favor <= 10:
        return coin + randint(10, 20)
    elif 10 < favor <= 20:
        return coin + randint(20, 30)
    elif 20 < favor == 30:
        return coin + randint(30, 40)
    elif favor == 30:
        return coin + 300
    elif 30 < favor <= 40:
        return coin + randint(40, 50)
    elif 40 < favor <= 50:
        return coin + randint(50, 60)
    else:
        return coin + randint(50, 100)

def chick_in(user_id: str):
    with open('./data/user.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    details = data[str(user_id)]

    details['user_coin'] = coin_algorithm(details['user_favorability'], details['user_coin'])
    details['user_favorability'] = favor_algorithm(details['check_in_days'], details['user_favorability'])
    details['check_in_days'] = details['check_in_days'] + 1

    data[str(user_id)] = details

    file = open('./data/user.json', 'w', encoding='utf-8')
    json.dump(data, file, ensure_ascii=False, indent=4)

def check_in_interval_judgment(user_id: str):
    with open('./data/user.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    details = data[user_id]

    if details['last_check_in_time'][0: 10] != time.asctime(time.localtime(time.time()))[0: 10]:
        details['last_check_in_time'] = time.asctime(time.localtime(time.time()))

        data[user_id] = details

        file = open('./data/user.json', 'w', encoding='utf-8')
        json.dump(data, file, ensure_ascii=False, indent=4)
        return 1
    else:
        return 0

def get_chick_info(user_id: str):
    with open('./data/user.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data[str(user_id)]

def get_user_info():
    with open('./data/user.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data

if __name__ == '__main__':
    chick_in('2301583973')
