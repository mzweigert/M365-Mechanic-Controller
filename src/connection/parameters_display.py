from display.base_display import BaseDisplay
from display.progress_bar import ProgressBar
from PIL import ImageFont

from connection_fake import XiaomiBLEBaseConnection

# from py9b.connection.xiaomi_ble_connection import XiaomiBLEBaseConnection, RecoveryEnergyMode

font_path = '/usr/share/fonts/truetype/orbitron/Orbitron-Black.ttf'
info_font = ImageFont.truetype(font_path, 15)
speed_font = ImageFont.truetype(font_path, 35)
battery_info_font = ImageFont.truetype(font_path, 9)


class ParametersDisplay:
    def __init__(self, connection: XiaomiBLEBaseConnection):
        self.__display = BaseDisplay()
        self.__battery_info_bar = ProgressBar(self.__display, font=battery_info_font, top=58)
        self.__connection = connection

        self.__speed_info_top = 20
        self.__speed_template_printed = False

    def show(self):
        self.__show_speed()
        self.__show_battery_info()

    def __show_speed(self):
        (width, height) = speed_font.getsize("88")
        dot_width = speed_font.getsize(".")[0]

        if not self.__speed_template_printed:
            self.__display.prepare_text_to_draw(width + 2, self.__speed_info_top, '.', speed_font)
            speed_measure_width = info_font.getsize('km')[0]
            self.__display.prepare_text_to_draw(self.__display.get_width() - speed_measure_width,
                                                self.__speed_info_top, 'km\n /h', info_font)
            self.__speed_template_printed = True

        speed = round(self.__connection.get_speed(), 1)
        self.__display.clear_area(0, self.__speed_info_top, width, height)
        self.__display.clear_area(width + dot_width + 4, self.__speed_info_top, width / 2, height)

        speed_txt = str(speed).split(".")
        index_width = speed_font.getsize(speed_txt[0])[0]

        self.__display.prepare_text_to_draw(width - index_width, self.__speed_info_top, speed_txt[0], speed_font)
        self.__display.prepare_text_to_draw(width + dot_width + 4, self.__speed_info_top, speed_txt[1], speed_font)

        self.__display.show()

    def __show_battery_info(self):
        battery = self.__connection.get_battery_level()
        self.__battery_info_bar.update(battery)
