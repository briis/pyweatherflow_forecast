"""System Wide constants for WeatherFlow Forecast Wrapper."""
from __future__ import annotations
import logging
_LOGGER = logging.getLogger(__name__)

CACHE_MINUTES = 30

FORECAST_TYPE_DAILY = 0
FORECAST_TYPE_HOURLY = 1

WEATHERFLOW_BASE_URL = "https://swd.weatherflow.com/swd/rest"
WEATHERFLOW_DEVICE_URL = f"{WEATHERFLOW_BASE_URL}/observations/device/"
WEATHERFLOW_FORECAST_URL = f"{WEATHERFLOW_BASE_URL}/better_forecast?station_id="
WEATHERFLOW_SENSOR_URL = f"{WEATHERFLOW_BASE_URL}/observations/station/"
WEATHERFLOW_STATION_URL = f"{WEATHERFLOW_BASE_URL}/stations/"

ICON_LIST = {
    "clear-day": "sunny",
    "clear-night": "clear-night",
    "cloudy": "cloudy",
    "foggy": "fog",
    "partly-cloudy-day": "partlycloudy",
    "partly-cloudy-night": "partlycloudy",
    "possibly-rainy-day": "rainy",
    "possibly-rainy-night": "rainy",
    "possibly-sleet-day": "snowy-rainy",
    "possibly-sleet-night": "snowy-rainy",
    "possibly-snow-day": "snowy",
    "possibly-snow-night": "snowy",
    "possibly-thunderstorm-day": "lightning-rainy",
    "possibly-thunderstorm-night": "lightning-rainy",
    "rainy": "rainy",
    "sleet": "snowy-rainy",
    "snow": "snowy",
    "thunderstorm": "lightning",
    "windy": "windy"
}
