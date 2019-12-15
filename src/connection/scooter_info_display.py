from connection_fake import XiaomiBLEBaseConnection
# from py9b.connection.xiaomi_ble_connection import XiaomiBLEBaseConnection, RecoveryEnergyMode
from py9b.link.base import LinkTimeoutException, NoDeviceFoundException
from .parameters_display import ParametersDisplay

import traceback
import sys
import select


def is_enter_pressed():
    i, o, e = select.select([sys.stdin], [], [], 0.0001)
    for s in i:
        if s == sys.stdin:
            sys.stdin.readline()
            return True
    return False


class ScooterInfoDisplay:
    def __init__(self):
        self.__connection = XiaomiBLEBaseConnection()
        self.__retries = 5
        self.__parameters_display = ParametersDisplay(self.__connection)

    def show(self):
        with self.__connection:
            while self.__retries > 0 and not is_enter_pressed():
                self.__update()

    def __update(self):
        try:
            self.__parameters_display.show()
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
