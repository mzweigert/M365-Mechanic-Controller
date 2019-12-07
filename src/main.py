from display.base_display import BaseDisplay
from display.progress_bar import ProgressBar
from PIL import ImageFont

from time import sleep

if __name__ == '__main__':
    # Load a font in 2 different sizes.
    font = ImageFont.truetype('/usr/share/fonts/truetype/orbitron/Orbitron-Bold.ttf', 9)
    display = BaseDisplay(font=font)
    bar = ProgressBar(display, start_percent=0)
    percent = 0
    while percent <= 100:
        percent += 1
        bar.update(percent)
        sleep(0.1)

    percent = 100
    while percent >= 0:
        percent -= 1
        bar.update(percent)
        sleep(0.1)