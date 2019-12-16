from scooter_connection import XiaomiBLEBaseConnection
from py9b.link.base import LinkTimeoutException, NoDeviceFoundException
from .parameters_display import ParametersDisplay
from .buttons_controller import ButtonsController
from display.base_display import BaseDisplay

import traceback
import sys
import select
from time import sleep


def is_enter_pressed():
    i, o, e = select.select([sys.stdin], [], [], 0.0001)
    for s in i:
        if s == sys.stdin:
            sys.stdin.readline()
            return True
    return False


class ScooterController:
    def __init__(self):
        self.__connection = XiaomiBLEBaseConnection()
        self.__retries = 5
        self.__parameters_display = None
        self.__buttons_controller = None
        self.__display = BaseDisplay()

    def handle(self):
        with self.__connection:
            self.__parameters_display = ParametersDisplay(self.__connection, self.__display)
            self.__buttons_controller = ButtonsController(self.__connection, self.__display)

            while self.__retries > 0 and not is_enter_pressed():
                self.__update()

    def __update(self):
        try:
            if not self.__buttons_controller.is_display_blocked():
                self.__parameters_display.show()
            else:
                self.__buttons_controller.invoke_action_and_unlock_display()
                self.__parameters_display = ParametersDisplay(self.__connection, self.__display)

            sleep(0.25)
            self.__retries = 5
        except LinkTimeoutException:
            traceback.print_exc()
            print("Some problems with connection has been occurred.")
            print("Reconnecting to " + self.__connection.address)
        except NoDeviceFoundException:
            traceback.print_exc()
            self.__retries -= 1
            if self.__retries > 0:
                print("No devices found. Scanning again...")
        except TimeoutError:
            traceback.print_exc()
            self.__retries -= 1
