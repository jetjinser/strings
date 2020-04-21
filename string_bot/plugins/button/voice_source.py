"""
get button voice's module
"""
import random


async def get_aqua_voice_url():
    """
    get aqua voice url
    :return: aqua voice url
    """
    voice_list1 = [f'a-{a}' for a in range(1, 220)]
    voice_list2 = [f'a0616-{b}' for b in range(1, 30)]
    voice_list3 = [f'a0930-{c}' for c in range(1, 4)]

    voice_list = voice_list1 + voice_list2 + voice_list3

    random_voice = random.choice(voice_list)
    url = f'https://aquaminato.moe/voices/{random_voice}.mp3'

    return url


async def get_mea_voice_url():
    """
    get mea voice url
    :return: mea voice url
    """
    voice_list0 = [f'0{e}-1' for e in range(1, 10)]
    voice_list1 = [f'{a}-1' for a in range(10, 71)] + ['71']
    voice_list2 = [f'm0614-{b}' for b in range(1, 160)]
    voice_list3 = [f'm0629-{c}' for c in range(1, 33)]

    voice_list = voice_list0 + voice_list1 + voice_list2 + voice_list3

    random_voice = random.choice(voice_list)
    url = f'https://meamea.moe/voices/{random_voice}.mp3'

    return url
