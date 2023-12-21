"""Holds the Data Calsses for WeatherFlow Forecast Wrapper."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


def calculate_battery_percentage(voltage: float) -> int:
    if voltage is None:
        return None
    if voltage > 2.80:
        return 100
    elif voltage < 1.80:
        return 0
    return int((voltage - 1.8) * 100)


@dataclass
class WeatherFlowBaseData:
    datetime: datetime
    condition: str
    icon: str


@dataclass
class WeatherFlowForecastData(WeatherFlowBaseData):
    temperature: float
    humidity: int
    apparent_temperature: float
    precipitation: float
    pressure: float
    wind_bearing: int
    wind_gust_speed: float
    wind_speed: float
    uv_index: int
    timestamp: int
    forecast_daily: WeatherFlowForecastDaily | None = None
    forecast_hourly: WeatherFlowForecastHourly | None = None


@dataclass
class WeatherFlowForecastDaily(WeatherFlowBaseData):
    temperature: float
    temp_low: float
    precipitation_probability: int
    precipitation: float
    wind_bearing: int
    wind_speed: float
    timestamp: int


@dataclass
class WeatherFlowForecastHourly(WeatherFlowBaseData):
    temperature: float
    apparent_temperature: float
    humidity: int
    precipitation: float
    precipitation_probability: int
    pressure: float
    wind_bearing: float
    wind_gust_speed: int
    wind_speed: int
    uv_index: float
    timestamp: int


@dataclass
class WeatherFlowDeviceData:
    device_id: int
    voltage: float

    @property
    def battery(self) -> int:
        return calculate_battery_percentage(self.voltage)


@dataclass
class WeatherFlowStationData:
    station_name: str
    latitude: float
    longitude: float
    timezone: str
    device_id: int
    firmware_revision: str
    serial_number: str


@dataclass
class WeatherFlowSensorData:
    air_density: float
    air_temperature: float
    barometric_pressure: float
    brightness: int
    delta_t: float
    dew_point: float
    feels_like: float
    heat_index: float
    lightning_strike_count: int
    lightning_strike_count_last_1hr: int
    lightning_strike_count_last_3hr: int
    lightning_strike_last_distance: int
    lightning_strike_last_epoch: datetime.timestamp
    precip: float
    precip_accum_last_1hr: float
    precip_accum_local_day: float
    precip_accum_local_yesterday: float
    precip_minutes_local_day: int
    precip_minutes_local_yesterday: int
    pressure_trend: str
    relative_humidity: int
    sea_level_pressure: float
    solar_radiation: float
    station_pressure: float
    timestamp: int
    uv: float
    voltage: float
    wet_bulb_globe_temperature: float
    wet_bulb_temperature: float
    wind_avg: float
    wind_chill: float
    wind_direction: int
    wind_gust: float
    wind_lull: float
    precip_accum_local_day_final: float
    precip_accum_local_yesterday_final: float
    precip_minutes_local_day_final: int
    precip_minutes_local_yesterday_final: int
    elevation: float
    station_name: str
