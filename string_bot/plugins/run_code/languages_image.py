from PIL import Image, ImageDraw, ImageFont


class LanguagesImage:
    """
    支持语言的图片处理
    glot.io
    """

    def __init__(self, image, text):
        """
        初始化
        :param image:背景图片地址
        :param text: 图片上的文字
        """
        self._image = Image.open(image)
        self._text = text

    def __text_target(self):
        """
        写入文字
        和框 -- 下次再做
        """
        image = self._image.copy()

        pix = (0, 0, 0)
        image_size_width, image_size_height = self._image.size

        font = ImageFont.truetype('data/SourceCodeVariable-Italic.ttf', 28)

        text = self._text.split('\n')
        count = 0
        for i in text:
            text_size = font.getsize(i)
            where = (
                (image_size_width - text_size[0]) // 2, (image_size_height - text_size[1]) // 2 + 40 * count - 80)

            # 写入文字
            draw = ImageDraw.Draw(image)
            draw.text(where, i, pix, font=font)

            # 框
            # txt_frame = Image.new('RGBA', (540, 80), (0, 0, 0, 190))
            # image.paste(txt_frame, (50, 425), txt_frame)

            count += 1

        return image

    def save(self, filename):
        """
        保存图片
        """
        self.__text_target().save(filename)
