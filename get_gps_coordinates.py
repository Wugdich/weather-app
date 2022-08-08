# Standatrd library imports.
from dataclasses import dataclass
from subprocess import Popen, PIPE

# Related third party imports.

# Local application/libarary specific imports.
from exceptions import CantGetDataFromPipeline
import config 


@dataclass(slots=True, frozen=True)
class Coordinates:
    longitude: float
    latitude: float


def get_gps_coordinates() -> Coordinates:
    """Return current device coordinates using web service ipinfo.io and
    terminal utilite curl
    """
    coordinates = _get_curl_coordinates()
    return _round_coordinates(coordinates)


def _get_curl_coordinates() -> Coordinates:
    curl_output = _get_curl_output()
    coordinates = _parse_coordinates(curl_output)
    return coordinates


def _get_curl_output() -> bytes:
    process = Popen(['curl', '--silent', 'ipinfo.io/loc'], stdout=PIPE)
    output, err = process.communicate()
    exit_code = process.wait()
    if err is not None or exit_code != 0:
        raise CantGetDataFromPipeline
    return output


def _parse_coordinates(curl_output: bytes) -> Coordinates:
    latitude, longitude= map(lambda c: float(c), 
            curl_output.decode().split(','))
    return Coordinates(longitude=longitude, latitude=latitude)


def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    if not config.USE_ROUNDED_COORDS:
        return coordinates
    return Coordinates(*map(lambda c: round(c, 1),
        [coordinates.longitude, coordinates.latitude]))


if __name__ == '__main__':
    print(get_gps_coordinates())

