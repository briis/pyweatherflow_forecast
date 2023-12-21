import dataclasses
from dataclasses import dataclass, field
from typing import List
import json


@dataclass
class APIStatus:
    status_code: int
    status_message: str


@dataclass
class StationMeta:
    elevation: float
    share_with_wf: bool
    share_with_wu: bool


@dataclass
class DeviceMeta:
    agl: float
    name: str
    environment: str
    wifi_network_name: str


@dataclass
class Device:
    device_id: int
    serial_number: str
    device_meta: DeviceMeta
    device_type: str
    hardware_revision: str
    firmware_revision: str
    notes: str


@dataclass
class StationItem:
    location_item_id: int
    station_id: int
    device_id: int
    item: str


@dataclass
class Station:
    station_id: int
    name: str
    public_name: str
    latitude: float
    longitude: float
    station_meta: StationMeta
    devices: List[Device] = field(default_factory=list)
    station_items: List[StationItem] = field(default_factory=list)


@dataclass
class StationsResponse:
    status: APIStatus
    locations: List[Station]


def json_to_dataclass(json_str: str, data_class: Type) -> Any:
    """
    Convert a JSON string to a data class instance.

    Args:
    json_str (str): The JSON string to be converted.
    data_class (Type): The data class type to which the JSON string will be converted.

    Returns:
    Any: An instance of the specified data class.
    """
    data = json.loads(json_str)  # Parse JSON string into a Python dictionary

    def convert_field(data: Any, field_type: Type) -> Any:
        """
        Convert a field to the specified type, handling nested data classes and lists.

        Args:
        data (Any): The data to be converted.
        field_type (Type): The type to which the data should be converted.

        Returns:
        Any: The converted data.
        """
        # Check if the field type is a data class and create an instance of it
        if dataclasses.is_dataclass(field_type):
            return field_type(**data)
        # Handle lists of data classes
        if isinstance(data, list) and len(data) > 0 and dataclasses.is_dataclass(data[0]):
            return [convert_field(item, field_type[0]) for item in data]
        return data

    # Iterate over fields in the data class and convert each field
    for field in dataclasses.fields(data_class):
        if field.name in data and isinstance(data[field.name], (dict, list)):
            data[field.name] = convert_field(data[field.name], field.type)

    return data_class(**data)


# Example usage for /stations
json_str_stations = '{"status": {"status_code": 0, "status_message": "SUCCESS"}, "locations": [...]}'
stations_response = json_to_dataclass(json_str_stations, StationsResponse)

# Example usage for /stations/{station_id}
json_str_station = '{"status": {"status_code": 0, "status_message": "SUCCESS"}, "locations": [...]}'
single_station_response = json_to_dataclass(json_str_station, StationsResponse)
