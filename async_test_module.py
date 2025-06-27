# ruff: noqa: F401
"""This module is only used to run some realtime data tests using the async functions, while developing the module.

Create a .env file and add STATION_ID with the id of your station and API_TOKEN with the personal Token.
"""
from __future__ import annotations

from dotenv import load_dotenv
import os
import asyncio
import aiohttp
import logging
import time

from pyweatherflow_forecast import (
    WeatherFlow,
    WeatherFlowStationData,
    WeatherFlowForecastData,
    WeatherFlowSensorData,
)

_LOGGER = logging.getLogger(__name__)

async def main() -> None:
    """Async test module."""

    logging.basicConfig(level=logging.DEBUG)
    start = time.time()

    load_dotenv()
    station_id = os.getenv("STATION_ID")
    api_token = os.getenv("API_TOKEN")
    elevation = 60

    session = aiohttp.ClientSession()
    weatherflow = WeatherFlow(station_id=station_id, api_token=api_token, elevation=elevation, session=session, forecast_hours=12)

    try:
        station_data: WeatherFlowStationData = await weatherflow.async_get_station()
        print("###########################################")
        print("STATION NAME: ", station_data.station_name)
        print("DEVICE ID: ", station_data.device_id)
        print("FIRMWARE: ", station_data.firmware_revision)
        print("SERIAL: ", station_data.serial_number)

    except Exception as err:
        print(err)

    try:
        sensor_data: WeatherFlowSensorData = await weatherflow.async_fetch_sensor_data()
        print("###########################################")
        print("DATA AVAILABLE:", sensor_data.data_available)
        print("TEMPERATURE:", sensor_data.air_temperature)
        print("APPARENT:", sensor_data.feels_like)
        print("WIND GUST:", sensor_data.wind_gust)
        print("LAST LIGHTNING:", sensor_data.lightning_strike_last_epoch)
        print("WIND DIRECTION: ", sensor_data.wind_direction)
        print("WIND CARDINAL: ", sensor_data.wind_cardinal)
        print("PRECIP CHECKED: ", sensor_data.precip_accum_local_day_final)
        print("ABSOLUTE HUMIDITY: ", sensor_data.absolute_humidity)
        print("VISIBILITY: ", sensor_data.visibility)
        print("BEAUFORT: ", sensor_data.beaufort)
        print("BEAUFORT: ", sensor_data.beaufort_description)
        print("FREEZING ALT: ", sensor_data.freezing_altitude)
        print("VOLTAGE: ", sensor_data.voltage)
        print("BATTERY: ", sensor_data.battery)
        print("POWER SAVE MODE: ", sensor_data.power_save_mode)
        print("IS FREEZING: ", sensor_data.is_freezing)
        print("IS LIGHTNING: ", sensor_data.is_lightning)
        print("IS RAINING: ", sensor_data.is_raining)
        print("UV INDEX: ", sensor_data.uv)
        print("UV DESCRIPTION: ", sensor_data.uv_description)
        print("STATION NAME: ", sensor_data.station_name)
        print("PRECIP INTENSITY: ", sensor_data.precip_intensity)
        print("PRECIP: ", sensor_data.precip)
        print("PRECIP LAST HOUR: ", sensor_data.precip_accum_last_1hr)
        print("PRECIP TYPE: ", sensor_data.precip_type)

    except Exception as err:
        print(err)


    try:
        data: WeatherFlowForecastData = await weatherflow.async_get_forecast()
        print("TEMPERATURE: ", data.temperature)
        print("***** DAILY DATA *****")
        for item in data.forecast_daily:
            print(item.temperature, item.temp_low, item.icon, item.condition, item.precipitation_probability, item.precip_icon, item.precip_type, item.precipitation, item.wind_bearing, item.wind_speed, item.wind_gust)
        print("***** HOURLY DATA *****")
        cnt = 1
        for item in data.forecast_hourly:
            print("**", cnt, "** ", item.datetime, item.temperature, item.apparent_temperature, item.icon, item.condition, item.precipitation, item.precipitation_probability, item.precip_icon, item.precip_type)
            cnt += 1
    except Exception as err:
        print(err)


    if session is not None:
        await session.close()

    end = time.time()

    _LOGGER.info("Execution time: %s seconds", end - start)

asyncio.run(main())
