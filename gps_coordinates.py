# Standart library imports.
from typing import NamedTuple
from dataclasses import dataclass

# Related third party imports.
from pympler import asizeof

# Local application/library specific imports.


@dataclass(slots=True, frozen=True)
class CoordinateDT2:
    longitude: float
    latitude: float

coordinates_dt2 = CoordinateDT2(longitude=10.0, latitude=20.0)
print('Dataclass with slots and frozen:',
        asizeof.asized(coordinates_dt2).size)

