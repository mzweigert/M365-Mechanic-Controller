from display import Display
from PIL import ImageFont

if __name__ == '__main__':
    # Load a font in 2 different sizes.
    font = ImageFont.truetype('/usr/share/fonts/truetype/orbitron/Orbitron-Bold.ttf', 20)
    display = Display(font=font)
    display.draw_text(0, 0, "Test", fill=1)
