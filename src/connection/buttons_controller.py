from scooter_connection import XiaomiBLEBaseConnection, RecoveryEnergyMode

import RPi.GPIO as GPIO
from threading import Timer
from display.base_display import BaseDisplay
from PIL import ImageFont

font_path = '/usr/share/fonts/truetype/orbitron/Orbitron-Medium.ttf'
info_font = ImageFont.truetype(font_path, 14)


def bool_to_switch(bool_val):
    if bool_val:
        return "On"
    else:
        return "Off"


class ButtonsController:
    def __init__(self, connection: XiaomiBLEBaseConnection, display: BaseDisplay):
        self.__connection = connection
        self.__cruise_status = connection.is_cruise_control_on()
        self.__tail_light_on = connection.is_tail_light_on()
        self.__recovery_energy = connection.get_recovery_energy()
        self.__display = display
        self.__display_blocked = False
        self.__action_btn = None

        self.__buttons = self.pins_with_actions()
        GPIO.setmode(GPIO.BCM)
        for pin in self.__buttons.keys():
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(pin, GPIO.RISING, callback=self.__on_btn_press)

    def pins_with_actions(self):
        return {
            6: self.__set_cruise_control,
            12: self.__set_tail_light,
            13: self.__set_recovery_energy_mode,
            16: self.__show_total_millage
        }

    def __on_btn_press(self, pin):
        if self.__display_blocked or GPIO.input(pin) == GPIO.LOW:
            return
        self.__display_blocked = True
        self.__action_btn = self.__buttons.get(pin)

    def __set_cruise_control(self):
        self.__cruise_status = not self.__cruise_status
        self.__connection.set_cruise_control(self.__cruise_status)
        self.__show_info("Cruise control:",  "%s" % bool_to_switch(self.__cruise_status))

    def __set_tail_light(self):
        self.__tail_light_on = not self.__tail_light_on
        self.__connection.set_tail_light(self.__tail_light_on)
        self.__show_info("Tail light:",  "%s" % bool_to_switch(self.__tail_light_on))

    def __set_recovery_energy_mode(self):
        self.__recovery_energy = self.__recovery_energy.next_val()
        self.__connection.set_recovery_energy(self.__recovery_energy)
        self.__show_info("Recovery mode:", "%s" % self.__recovery_energy.name)

    def __show_total_millage(self):
        self.__show_info("Total millage:", "%s" % self.__connection.get_total_mileage())

    def __show_info(self, label, status):
        self.__display.clear_display()
        (label_width, label_height) = info_font.getsize(label)
        status_width = info_font.getsize(status)[0]

        self.__display.prepare_text_to_draw((self.__display.get_width() - label_width) / 2, 20, label, info_font)
        self.__display.prepare_text_to_draw((self.__display.get_width() - status_width) / 2, 25 + label_height, status,
                                            info_font)
        self.__display.show()

    def is_display_blocked(self):
        return self.__display_blocked

    def invoke_action_and_unlock_display(self):
        if not self.__action_btn:
            return
        self.__action_btn()
        self.__action_btn = None
        Timer(1.5, self.__unlock_display).start()

    def __unlock_display(self):
        self.__display.clear_display()
        self.__display_blocked = False

