from abc import ABC
from enum import Enum


class ParrotType(Enum):
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3


class MyParrot(ABC):

    def cry(self) -> str:
        pass

    def speed(self) -> int:
        pass


class MyEuropeanParrot(MyParrot):

    def __init__(self, base_speed):
        self.base_speed = base_speed

    def cry(self) -> str:
        return "Sqoork!"

    def speed(self) -> int:
        return self.base_speed


class MyAfricanParrot(MyParrot):

    def __init__(self, base_speed, load_factor, number_of_coconuts):
        self.base_speed = base_speed
        self.load_factor = load_factor
        self.number_of_coconuts = number_of_coconuts

    def cry(self) -> str:
        return "Sqaark!"

    def speed(self) -> int:
        return max(0, self.base_speed - self.load_factor * self.number_of_coconuts)


class MyNorwegianBlueParrot(MyParrot):

    def __init__(self, voltage, nailed, base_speed):
        self.voltage = voltage
        self.nailed = nailed
        self.base_speed = base_speed

    def cry(self) -> str:
        return "Bzzzzzz" if self.voltage > 0 else "..."

    def speed(self) -> int:
        return 0 if self.nailed else self._compute_base_speed_for_voltage(self.voltage)

    def _compute_base_speed_for_voltage(self, voltage):
        return min([24.0, voltage * self.base_speed])


class Parrot:

    def __init__(self, type_of_parrot, number_of_coconuts, voltage, nailed):
        self._type = type_of_parrot
        self._number_of_coconuts = number_of_coconuts
        self._voltage = voltage
        self._nailed = nailed
        self._base_speed = 12.0
        self._load_factor = 9.0

    def factory(self) -> MyParrot:
        match self._type:
            case ParrotType.EUROPEAN:
                return MyEuropeanParrot(self._base_speed)
            case ParrotType.AFRICAN:
                return MyAfricanParrot(self._base_speed, self._load_factor, self._number_of_coconuts)
            case ParrotType.NORWEGIAN_BLUE:
                return MyNorwegianBlueParrot(self._voltage, self._nailed, self._base_speed)

    def speed(self):
        return self.factory().speed()

    def cry(self):
        return self.factory().cry()

