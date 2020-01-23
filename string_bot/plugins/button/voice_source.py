import random


async def get_aqua_button_url():
    voice_list1 = [f'a-{a}' for a in range(1, 220)]
    voice_list2 = [f'a0616-{b}' for b in range(1, 30)]
    voice_list3 = [f'a0930-{c}' for c in range(1, 4)]

    voice_list = voice_list1 + voice_list2 + voice_list3

    random_voice = random.choice(voice_list)
    url = f'https://aquaminato.moe/voices/{random_voice}.mp3'

    return url
