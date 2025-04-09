## Release 1.2.0

**Date**: `2025-04-09`

### Changes

- Fixing "Failed setup, will retry" with "Updated failed: 'time'". Closing [WeatherFlow Forecast #99](https://github.com/briis/weatherflow_forecast/issues/99)


## Release 1.1.2

**Date**: `2024-01-13`

### Changes

- Fixing "Failed setup, will retry" with "Updated failed: 'time'". Closing [WeatherFlow Forecast #99](https://github.com/briis/weatherflow_forecast/issues/99)

## Release 1.1.1

**Date**: `2024-01-07`

### Changes

- Bumped Python to 3.13 in Devcontainer
- Added `precip_type` and `precip_icon` to Daily and Hourly Forecast.

## Release 1.1.0

**Date**: `2024-09-18`

### Changes

- Bumped Python to 3.12 in Devcontainer
- Added `precip_type_text` sensor, which describes what type of precipitation is measured. (No Rain, Rain or Heavy Rain/Hail)


## Release 1.0.11

**Date**: `2024-01-27`

### Changes

- Added the option of supplying number of hours we want to show for the Hourly Forecast. Default is set to 48 hours.


## Release 1.0.10

**Date**: `2024-01-22`

### Changes

- Added better error handling if the Station ID is not found. The module will now raise the `WeatherFlowForecastWongStationId` error, which then can be handled.

## Release 1.0.9

**Date**: `2024-01-21`

### Changes

- Adding voltage to the empty sensor dataset, resulting in valid data for voltage, battery and power save mode even with an empty dayaset from WeatherFlow

## Release 1.0.8

**Date**: `2024-01-21`

### Changes

- Handling if the station is offline or there are no recent observations. Returning and empty dataset with the field `data_available` set to False if no data can be retrieved.

## Release 1.0.7

**Date**: `2024-01-20`

### Changes

- Fixed the issue where a wrong value was used to calculate the UV Description sensor.

## Release 1.0.5

**Date**: `2024-01-06`

### Changes

- Reverting changes done by `mypy` that seems to have caused problems for some people.

## Release 1.0.3

**Date**: `2024-01-04`

### Changes

- Added `wind_gust` to Daily Forecast

## Release 1.0.2

**Date**: `2023-12-23`

### Changes

- Added new sensor `Precip Type` exposing an integer with the type of precipitation, if any. Possible values are: 0 = none, 1 = rain, 2 = hail and 3 = rain+hail (Experimental)

## Release 1.0.1

**Date**: `2023-12-04`

### Changes

- Added new sensor `Precip Intensity` exposing a text string with the intensity of the current rain

## Release 1.0.0

**Date**: `2023-11-18`

### Changes

- Added new binary_sensor `Is Lightning` showing if there is currently a lightning storm
- Added new sensor `UV Description`, detailing the current UV value
- Added new sensor `Staton Information`, detailing data about the Tempest Station

## Release 0.6.4

**Date**: `2023-10-18`

### Changes

- Added new sensor `Power Save Mode` that shows the Power Mode of a Tempest device. Attributes of the sensor gives a textual explanation. For more information [read here](https://help.weatherflow.com/hc/en-us/articles/360048877194-Solar-Power-Rechargeable-Battery)

## Release 0.6.3

**Date**: `2023-10-17`

### Changes

- Added check for None values in all calculated sensors, to ensure they will not throw an error.

## Release 0.6.2

**Date**: `2023-10-15`

### Changes

- Ensuring that the sensor function still works with AIR and SKY devices, even though we do not add Voltage and battery values.

## Release 0.6.1

**Date**: `2023-10-15`

### Changes

- Optimizing the *Fetch Sensor Data* by removing 1 call to the API per cycle.

## Release 0.6.0

**Date**: `2023-10-14`

### Changes

- Rewritten the Request modules to simplify code base.
- Merged all API request needed for getting sensor data, into one function.

## Release 0.5.1

**Date**: `2023-10-13`

### Changes

- Fixing loop when retreiving device information - used for the voltage data.

## Release 0.5.0

**Date**: `2023-10-12`

### Changes

- Added Voltage sensor. This will only be available for Tempest devices. AIR and SKY will not be supported-
- Added calculated battery sensor, that show the % full. Calculated sensor based on the voltage value.


## Release 0.4.7

**Date**: `2023-10-09`

### Changes

- Fix wrong value in Absolute Humidity
- Added Beaufort sensor
- Added Freezing Altitude sensor