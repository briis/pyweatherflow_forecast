from dataclasses import dataclass, field
from typing import List, Optional
import json
import enum


class Condition(str, enum.Enum):
    CLEAR = "Clear"
    RAIN_LIKELY = "Rain Likely"
    RAIN_POSSIBLE = "Rain Possible"
    SNOW = "Snow"
    SNOW_POSSIBLE = "Snow Possible"
    WINTRY_MIX_LIKELY = "Wintry Mix Likely"
    WINTRY_MIX_POSSIBLE = "Wintry Mix Possible"
    THUNDERSTORMS_LIKELY = "Thunderstorms Likely"
    THUNDERSTORMS_POSSIBLE = "Thunderstorms Possible"
    WINDY = "Windy"
    FOGGY = "Foggy"
    CLOUDY = "Cloudy"
    PARTLY_CLOUDY = "Partly Cloudy"
    VERY_LIGHT_RAIN = "Very Light Rain"


class Icon(str, enum.Enum):
    CLEAR_DAY = "clear-day"
    CLEAR_NIGHT = "clear-night"
    CLOUDY = "cloudy"
    FOGGY = "foggy"
    PARTLY_CLOUDY_DAY = "partly-cloudy-day"
    PARTLY_CLOUDY_NIGHT = "partly-cloudy-night"
    POSSIBLY_RAINY_DAY = "possibly-rainy-day"
    POSSIBLY_RAINY_NIGHT = "possibly-rainy-night"
    POSSIBLY_SLEET_DAY = "possibly-sleet-day"
    POSSIBLY_SLEET_NIGHT = "possibly-sleet-night"
    POSSIBLY_SNOW_DAY = "possibly-snow-day"
    POSSIBLY_SNOW_NIGHT = "possibly-snow-night"
    POSSIBLY_THUNDERSTORM_DAY = "possibly-thunderstorm-day"
    POSSIBLY_THUNDERSTORM_NIGHT = "possibly-thunderstorm-night"
    RAINY = "RAINY"
    SLEET = "sleet"
    SNOW = "snow"
    THUNDERSTORM = "thunderstorm"
    WINDY = "windy"


class WindDirectionCardinal(str, enum.Enum):
    N = "N"  # North
    NNE = "NNE"  # North-Northeast
    NE = "NE"  # Northeast
    ENE = "ENE"  # East-Northeast
    E = "E"  # East
    ESE = "ESE"  # East-Southeast
    SE = "SE"  # Southeast
    SSE = "SSE"  # South-Southeast
    S = "S"  # South
    SSW = "SSW"  # South-Southwest
    SW = "SW"  # Southwest
    WSW = "WSW"  # West-Southwest
    W = "W"  # West
    WNW = "WNW"  # West-Northwest
    NW = "NW"  # Northwest
    NNW = "NNW"  # North-Northwest


class PrecipType(str, enum.Enum):
    RAIN = "rain"
    SNOW = "snow"
    SLEET = "sleet"
    STORM = "storm"


class PrecipIcon(str, enum.Enum):
    CHANCE_RAIN = "chance-rain"
    CHANCE_SNOW = "chance-snow"
    CHANCE_SLEET = "chance-sleet"


class PressureTrend(str, enum.Enum):
    FALLING = "falling"
    STEADY = "steady"
    RISING = "rising"
    UNKNOWN = "unknown"


@dataclass
class APIStatus:
    status_code: int
    status_message: str


@dataclass
class CurrentConditions:
    time: int
    conditions: Condition
    icon: Icon
    air_temperature: int
    sea_level_pressure: float
    station_pressure: float
    pressure_trend: PressureTrend
    relative_humidity: int
    wind_avg: float
    wind_direction: int
    wind_direction_cardinal: WindDirectionCardinal
    wind_gust: float
    solar_radiation: int
    uv: int
    brightness: int
    feels_like: float
    dew_point: int
    wet_bulb_temperature: int
    delta_t: int
    air_density: float
    lightning_strike_count_last_1hr: int
    lightning_strike_count_last_3hr: int
    lightning_strike_last_distance: int
    lightning_strike_last_epoch: int
    precip_accum_local_day: int
    precip_accum_local_yesterday: int
    precip_minutes_local_day: int
    precip_minutes_local_yesterday: int
    is_precip_local_day_rain_check: bool
    is_precip_local_yesterday_rain_check: bool


@dataclass
class ForecastDaily:
    day_start_local: int
    day_num: int
    month_num: int
    conditions: Condition
    icon: Icon
    sunrise: int
    sunset: int
    air_temp_high: int
    air_temp_low: int
    precip_probability: int
    precip_icon: PrecipIcon
    precip_type: PrecipType


@dataclass
class ForecastHourly:
    time: int
    conditions: Condition
    icon: Icon
    air_temperature: int
    sea_level_pressure: float
    relative_humidity: int
    precip: int
    precip_probability: int
    wind_avg: float
    wind_direction: int
    wind_direction_cardinal: WindDirectionCardinal
    wind_gust: float
    uv: int
    feels_like: float
    local_hour: int
    local_day: int


@dataclass
class Units:
    units_temp: str
    units_wind: str
    units_precip: str
    units_pressure: str
    units_distance: str
    units_brightness: str
    units_solar_radiation: str
    units_other: str
    units_air_density: str


@dataclass
class ForecastResponse:
    status: APIStatus
    current_conditions: CurrentConditions
    forecast: dict[str, list[ForecastDaily | ForecastHourly]]
    units: Units
    latitude: float
    longitude: float
    timezone: str
    timezone_offset_minutes: int
