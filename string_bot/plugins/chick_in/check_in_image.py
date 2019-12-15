from PIL import Image, ImageDraw, ImageFilter, ImageFont
from random import randint
import json


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
        self._image = Image.open(im).convert('RGBA')
        self._txt = txt
        self._small_size = small_size
        self._name = name

    def gaussian_blur(self):
        """
        高斯模糊处理
        :return: 模糊后的图片
        """
        img = self._image.filter(ImageFilter.GaussianBlur(radius=6))
        return img

    def circle(self):
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

    def alpha_circle(self):
        """
        小图标的圆形处理
        :return: 变为圆形的RGBA图片
        """
        size = self._small_size
        img = self._image.copy()
        img = img.resize((size, size))
        img.putalpha(self.circle())

        return img

    def coloring(self, where):
        """
        取反色
        :param where: 所取的位置
        :return: 反色(RGB)
        """
        # 取rgb值
        pix = self._image.getpixel(where)
        r, g, b, _ = pix

        # 取反色
        pix = list(pix)
        pix[0] = 255 - r
        pix[1] = 255 - g
        pix[2] = 255 - b
        pix[3] = 255

        return tuple(pix)

    def process(self):
        """
        合并处理图片
        创建文字框架
        写入文字信息
        嵌入图标框架
        :return: 处理后的图片
        """
        w, _ = self._image.size
        size = self._small_size

        # 创建白色画布
        target = Image.new('RGBA', self._image.size, (0, 0, 0, 0))
        # 贴上高斯模糊后的图片
        target.paste(self.gaussian_blur())

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
        target.paste(self.alpha_circle(),
                     (w // 2 - size // 2, w // 2 - size // 2 - 50),
                     self.alpha_circle())

        # 创建文字框架
        txt_frame = Image.new('RGBA', (540, 160), (0, 0, 0, 190))
        # 贴上文字框架
        target.paste(txt_frame, (50, 425), txt_frame)

        # 指定文字, 文字的字体和位置
        txt = self._txt.split('\n')
        font = ImageFont.truetype('./data/REEJI-HonghuangLiGB-SemiBold-2.ttf', 24)
        count = 0
        for i in txt:
            text_size = font.getsize(i)
            where = (
                (self._image.size[0] - text_size[0]) / 2, (self._image.size[1] - text_size[1]) / 2 + 125 + 30 * count)

            pix = (255, 255, 255)

            # 写入文字
            draw = ImageDraw.Draw(target)
            draw.text(where, i, pix, font=font)

            count += 1

        # 打开tips json文件, 选取tips
        with open('./data/tips.json', 'r', encoding='utf-8') as file:
            data = json.load(file)[0]

            num = list(data.keys())[-1]
            ram = str(randint(0, int(num)))
            writer = data[ram]

        # 写入tips
        draw = ImageDraw.Draw(target)
        font = ImageFont.truetype('./data/REEJI-HonghuangLiGB-SemiBold-2.ttf', 18)
        writer_size = font.getsize(writer)
        pix = (230, 230, 230)
        draw.text(((self._image.size[0] - writer_size[0]) / 2, 585 - 26), writer, pix, font=font)

        return target

    def save(self):
        """
        保存图片
        """
        self.process().save('./data/' + self._name + '.png')
