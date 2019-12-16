import enum
import random


def pp_distance(dist):
    if dist < 1000:
        return '%dm' % dist
    return '%dkm %dm' % (dist / 1000.0, dist % 1000)


class RecoveryEnergyMode(enum.Enum):
    Weak = 0
    Medium = 1
    Strong = 2

    def next_val(self):
        if self == RecoveryEnergyMode.Weak:
            return RecoveryEnergyMode.Medium
        elif self == RecoveryEnergyMode.Medium:
            return RecoveryEnergyMode.Strong
        else:
            return RecoveryEnergyMode.Weak


def randint(from_range, to_range):
    return random.randint(from_range, to_range)


class XiaomiBLEBaseConnection:
    def __init__(self):
        self.cruise = False
        self.tail_light = False
        self.mode = RecoveryEnergyMode.Weak
        self.address = "Fake address"

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def get_total_mileage(self):
        return pp_distance(randint(1, 100000))

    def get_total_runtime(self):
        return pp_distance(randint(1, 100000))

    def get_total_riding(self):
        return pp_distance(randint(1, 100000))

    def get_chassis_temp(self):
        return randint(1, 100)

    def get_battery_level(self):
        return randint(1, 100)

    def get_speed(self):
        return round(random.uniform(0, 27), 2)

    def set_cruise_control(self, enable):
        self.cruise = enable

    def is_cruise_control_on(self):
        return self.cruise

    def set_tail_light(self, enable):
        self.tail_light = enable

    def is_tail_light_on(self):
        return self.tail_light

    def set_recovery_energy(self, mode):
        self.mode = mode

    def get_recovery_energy(self):
        return self.mode
