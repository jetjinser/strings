from PIL import Image, ImageDraw, ImageFilter, ImageFont
from sql_exe import *
import os


class ImageProcessing:
    """
    签到图片的处理
    (高斯模糊)
    用于QQ机器人
    """

    def __init__(self, im, txt, small_size: int = 256, name: str = 'demo'):
        """
        初始化
        :param im:图片地址
        :param txt: 文字
        :param small_size: 小图标的尺寸(宽高)
        :param name: 处理后的图片名
        """
        _image = Image.open(im).convert('RGBA')
        self._txt = txt
        self._small_size = small_size
        self._name = name

        if _image.size != (640, 640):
            _image = _image.resize((640, 640))

        self._image = _image

    async def gaussian_blur(self):
        """
        高斯模糊处理
        :return: 模糊后的图片
        """
        img = self._image.filter(ImageFilter.GaussianBlur(radius=7))
        return img

    async def circle(self):
        """
        alpha圆框
        用于处理小图标
        :return: 处理后的圆框
        """
        size = self._small_size
        circle = Image.new('L', (size, size), 0)
        draw = ImageDraw.Draw(circle)
        draw.ellipse((0, 0, size, size), fill=255)

        return circle

    async def alpha_circle(self):
        """
        小图标的圆形处理
        :return: 变为圆形的RGBA图片
        """
        size = self._small_size
        img = self._image.copy()
        img = img.resize((size, size))
        img.putalpha(await self.circle())

        return img

    async def process(self):
        """
        合并处理图片
        创建文字框架
        写入文字信息
        嵌入图标框架
        :return: 处理后的图片
        """
        w = 640
        size = self._small_size

        # 创建白色画布
        target = Image.new('RGBA', (640, 640), (0, 0, 0, 0))
        # 贴上高斯模糊后的图片
        target.paste(await self.gaussian_blur())

        # 创建小图标的框架
        framework = Image.open('./data/framework.png').convert('L')
        framework = framework.resize((size + 30, size + 30))
        target_l = Image.new('RGBA', (size + 30, size + 30), (0, 0, 0, 0))
        target_l.putalpha(framework)

        # 贴上小图标的框架
        target.paste(target_l,
                     (w // 2 - size // 2 - 15, w // 2 - size // 2 - 50 - 15),
                     target_l)

        # 在原图中间 y-50 的位置贴上小图标
        target.paste(await self.alpha_circle(),
                     (w // 2 - size // 2, w // 2 - size // 2 - 50),
                     await self.alpha_circle())

        # 创建文字框架
        txt_frame = Image.new('RGBA', (540, 160), (0, 0, 0, 190))
        # 贴上文字框架
        target.paste(txt_frame, (50, 425), txt_frame)

        # 指定文字, 文字的字体和位置
        txt = self._txt.split('\n')
        font = ImageFont.truetype('./data/REEJI-HonghuangLiGB-SemiBold-2.ttf', 24)
        pix = (255, 255, 255)
        count = 0
        for i in txt:
            text_size = font.getsize(i)
            where = (
                (self._image.size[0] - text_size[0]) / 2, (self._image.size[1] - text_size[1]) / 2 + 125 + 30 * count)

            # 写入文字
            draw = ImageDraw.Draw(target)
            draw.text(where, i, pix, font=font)

            count += 1

        sql_select = (
            'SELECT tips FROM tips ORDER BY RANDOM() limit 1;'
        )

        values = sql_exe(sql_select)
        values = str(values[0][0])

        # 写入tips
        draw = ImageDraw.Draw(target)
        font = ImageFont.truetype('./data/REEJI-HonghuangLiGB-SemiBold-2.ttf', 18)
        writer_size = font.getsize(values)
        pix = (230, 230, 230)
        draw.text(((self._image.size[0] - writer_size[0]) / 2, 585 - 26), values, pix, font=font)

        return target

    async def save(self):
        """
        保存图片
        """
        output_img = await self.process()
        output_img.save('./cache/' + self._name + '.png')

    async def remove(self):
        os.remove('./cache/' + self._name + '.png')
