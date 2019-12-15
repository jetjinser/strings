import requests


async def get_random_things() -> str:
    url = 'http://www.boredapi.com/api/activity/'
    response = requests.get(url)
    r = response.json()
    formatted = '你可以:\n\t' + r['activity'] + '\n可行性:\n\t' + str(r['accessibility']) + '\n类型:\n\t' + r['type']
    return formatted
