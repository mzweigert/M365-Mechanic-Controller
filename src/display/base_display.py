import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306


class BaseDisplay(object):

    def __init__(self, font):
        reset_pin = digitalio.DigitalInOut(board.D4)
        self._oled = adafruit_ssd1306.SSD1306_I2C(128, 64, board.I2C(), addr=0x3c, reset=reset_pin)
        self._image = Image.new('1', (self._oled.width, self._oled.height))
        self._draw = ImageDraw.Draw(self._image)
        self._font = font

    def get_width(self):
        return self._oled.width

    def get_height(self):
        return self._oled.height

    def get_font(self):
        return self._font

    def clear_display(self):
        self._oled.fill(0)
        self._oled.show()

    def prepare_rectangle_to_draw(self, x, y, width, height, outline=True, fill=False):
        bar_width = x + width - 1
        bar_height = y + height - 1
        if bar_width <= 0 or bar_height <= 0:
            return

        self._draw.rectangle([(x, y), (bar_width,bar_height)], outline=outline, fill=fill)

    def show(self):
        self._oled.image(self._image)
        self._oled.show()

    def prepare_text_to_draw(self, x, y, text, font=None, fill=255):
        self._draw.text((x, y), text, font=font or self._font, fill=fill)
