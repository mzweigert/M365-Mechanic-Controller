import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306


class Display(object):

    def __init__(self, font):
        reset_pin = digitalio.DigitalInOut(board.D4)
        self._oled = adafruit_ssd1306.SSD1306_I2C(128, 64, board.I2C(), addr=0x3c, reset=reset_pin)
        self._image = Image.new('1', (self._oled.width, self._oled.height))
        self._draw = ImageDraw.Draw(self._image)
        self._font = font

    def clear_display(self):
        self._oled.fill(0)
        self._oled.show()

    def draw_text(self, x, y, text, font=None, fill=255):
        self._draw.text((x, y), text, font=font or self._font, fill=fill)
        self._oled.image(self._image)
        self._oled.show()
