import requests


async def get_image(user_id: str) -> str:
    url = f'http://q1.qlogo.cn/g?b=qq&nk={user_id}&s=5'
    response = requests.get(url)
    with open('./chick_image_cache/demo.jpg', 'wb') as f:
        f.write(response.content)
    return './chick_image_cache/demo.jpg'
