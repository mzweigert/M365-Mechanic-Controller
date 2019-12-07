from .base_display import BaseDisplay


class FontTooLargeException(Exception):
    pass


class ProgressBar(object):
    def __init__(self, display: BaseDisplay, font=None, top=0, start_percent=100):
        self._display = display
        self._width = 95
        self._height = 6
        self._font = font or display.get_font()
        (font_width, font_height) = self._font.getsize("100%")
        if font_width > display.get_width() - self._width - 4:
            raise FontTooLargeException
        self._top = top

        self.__draw(start_percent)

    def __get_last_percent(self):
        return self._last_percent

    def __set_last_percent(self, value):
        self._last_percent = value

    def __draw(self, start_percent):
        self.__set_last_percent(start_percent)
        self._display.prepare_rectangle_to_draw(0, self._top, self._width + 2, self._height)
        if start_percent > 0:
            fill_percents = int((self._width * start_percent) / 100)
            self._display.prepare_rectangle_to_draw(1, self._top + 1, fill_percents, self._height - 2,
                                                    outline=False, fill=True)

        self.__update_number(start_percent)
        self._display.show()

    def update(self, current_percent=None):
        if current_percent < 0 or current_percent > 100 or self._last_percent == current_percent:
            return

        start_x = int((self._width * current_percent) / 100)

        if start_x > self._width:
            return

        if current_percent < self._last_percent:
            self._display.prepare_rectangle_to_draw(start_x + 1, self._top + 2, self._width - start_x - 2, 2,
                                                    outline=False, fill=False)
        else:
            self._display.prepare_rectangle_to_draw(1, self._top + 1, start_x, self._height - 2,
                                                    outline=False, fill=True)

        self.__update_number(current_percent)
        self._display.show()

    def __update_number(self, current_percent):
        percent = str("%d%%" % current_percent)
        (font_width, font_height) = self._font.getsize(percent)
        self._display.prepare_rectangle_to_draw(self._width + 2, self._top, self._display.get_width() - self._width - 2,
                                                self._height, outline=False, fill=False)
        self._display.prepare_text_to_draw(self._display.get_width() - font_width, self._top, percent, self._font)
        self.__set_last_percent(current_percent)
