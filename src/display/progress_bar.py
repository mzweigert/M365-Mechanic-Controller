from .base_display import BaseDisplay


class FontTooLargeException(Exception):
    pass


class ProgressBar(object):
    def __init__(self, display: BaseDisplay, draw_on_start=False, font=None, top=0, start_percent=100):
        self._display = display
        self._width = 95
        self._height = 6
        self._font = font or display.get_font()
        (font_width, font_height) = self._font.getsize("100%")
        if font_width > display.get_width() - self._width - 4:
            raise FontTooLargeException
        self._top = top

        self.__last_percent = start_percent
        self.__draw_on_start = draw_on_start
        if draw_on_start:
            self.__draw(start_percent)

    def __draw(self, start_percent):
        self._display.prepare_rectangle_to_draw(0, self._top, self._width + 2, self._height)
        if start_percent > 0:
            fill_percents = int((self._width * start_percent) / 100)
            self._display.prepare_rectangle_to_draw(1, self._top + 1, fill_percents, self._height - 2,
                                                    outline=False, fill=True)

        self.__update_number(start_percent)
        self._display.show()

    def update(self, current_percent=None):
        if current_percent < 0 or current_percent > 100 or self.__last_percent == current_percent:
            return

        start_x = int((self._width * current_percent) / 100)

        if start_x > self._width:
            return

        if not self.__draw_on_start:
            self.__draw(current_percent)

        if current_percent < self.__last_percent:
            self._display.prepare_rectangle_to_draw(start_x + 1, self._top + 2, self._width - start_x - 1, 2,
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
        self.__last_percent = current_percent
