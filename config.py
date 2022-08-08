from environs import Env

env = Env()
env.read_env()

USE_ROUNDED_COORDS = True
OPEN_WEATHER_API = env.str('OPEN_WEATHER_API')
OPEN_WEATHER_URL = (
        'https://api.openweathermap.org/data/2.5/weather?'
        'lat={latitude}&lon={longitude}&'
        'appid=' + OPEN_WEATHER_API + '&lang=ru&'
        'units=metric'
        )


if __name__ == '__main__':
    print(OPEN_WEATHER_API)

