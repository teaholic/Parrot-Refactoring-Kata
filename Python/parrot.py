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
        return self.base_speed()


class MyAfricanParrot(MyParrot):

    def cry(self) -> str:
        return "Sqaark!"

    def speed(self) -> int:
        return 0


class MyNorwegianBlueParrot(MyParrot):

    def __init__(self, voltage):
        self.voltage = voltage

    def cry(self) -> str:
        return "Bzzzzzz" if self.voltage > 0 else "..."

    def speed(self) -> int:
        return 0


class Parrot:

    def __init__(self, type_of_parrot, number_of_coconuts, voltage, nailed):
        self._type = type_of_parrot
        self._number_of_coconuts = number_of_coconuts
        self._voltage = voltage
        self._nailed = nailed

    def speed(self):
        match self._type:
            case ParrotType.EUROPEAN:
                return MyEuropeanParrot(self._base_speed).speed()
            case ParrotType.AFRICAN:
                return max(0, self._base_speed() - self._load_factor() * self._number_of_coconuts)
            case ParrotType.NORWEGIAN_BLUE:
                return 0 if self._nailed else self._compute_base_speed_for_voltage(self._voltage)

    def cry(self):
        match self._type:
            case ParrotType.EUROPEAN:
                return MyEuropeanParrot(self._base_speed()).cry()
            case ParrotType.AFRICAN:
                return MyAfricanParrot().cry()
            case ParrotType.NORWEGIAN_BLUE:
                return MyNorwegianBlueParrot(self._voltage).cry()

    def _compute_base_speed_for_voltage(self, voltage):
        return min([24.0, voltage * self._base_speed()])

    def _load_factor(self):
        return 9.0

    def _base_speed(self):
        return 12.0
