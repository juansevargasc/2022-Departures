import pandera as pa
from pandera.typing import Series
from pandera import dtypes


class stg_active_weather_schema(pa.DataFrameModel):
    id_weather: Series[int] = pa.Field(ge=0, nullable=False)
    status: Series[int] = pa.Field(ge=0)
    weather_description: Series[str] = pa.Field()


class stg_cancellation_schema(pa.DataFrameModel):
    id_cancellation: Series[int] = pa.Field(ge=0, nullable=False)
    status: Series[int] = pa.Field(ge=0)
    cancellation_reason: Series[str] = pa.Field()


class stg_carriers_schema(pa.DataFrameModel):
    id_carriers: Series[int] = pa.Field(ge=0, nullable=False)
    code: Series[str] = pa.Field()
    description: Series[str] = pa.Field()


class stg_airports_schema(pa.DataFrameModel):
    id_airport: Series[int] = pa.Field(ge=0, nullable=False)
    airport_code: Series[str] = pa.Field()
    airport_name: Series[str] = pa.Field()
    airport_complete_name: Series[str] = pa.Field()
    us_state: Series[dtypes.Category] = pa.Field()
    us_state_abbr: Series[dtypes.Category] = pa.Field()
    latitude: Series[float] = pa.Field()
    longitude: Series[float] = pa.Field()
    elevation: Series[int] = pa.Field()
    icao_code: Series[str] = pa.Field()
    iata_code: Series[str] = pa.Field()
    mesonet_code: Series[str] = pa.Field()


class stg_departures_schema(pa.DataFrameModel):
    id_departure: Series[int] = pa.Field(ge=0, nullable=False)
    flight_date: Series[dtypes.DateTime] = pa.Field()
    dep_hour: Series[int] = pa.Field(ge=0)
    mkt_carrier_fl_num: Series[int] = pa.Field(ge=0)
    op_carrier_fl_num: Series[int] = pa.Field(ge=0)
    dep_time: Series[dtypes.DateTime] = pa.Field()
    crs_dep_time: Series[dtypes.DateTime] = pa.Field()
    taxi_out: Series[int] = pa.Field(ge=0)
    dep_delay: Series[int] = pa.Field()
    air_time: Series[int] = pa.Field(ge=0)
    distance: Series[float] = pa.Field(ge=0)
    wind_dir: Series[float] = pa.Field(nullable=True)
    wind_speed: Series[float] = pa.Field(nullable=True)
    wind_gust: Series[float] = pa.Field(nullable=True)
    visibility: Series[float] = pa.Field(nullable=True)
    temperature: Series[float] = pa.Field(nullable=True)
    dew_point: Series[float] = pa.Field(nullable=True)
    rel_humidity: Series[float] = pa.Field(nullable=True)
    low_level_cloud: Series[bool] = pa.Field(nullable=True)
    mid_level_cloud: Series[bool] = pa.Field(nullable=True)
    high_level_cloud: Series[bool] = pa.Field(nullable=True)
    mkt_unique_carrier: Series[str] = pa.Field()
    op_unique_carrier: Series[str] = pa.Field()
    origin: Series[str] = pa.Field()
    dest: Series[str] = pa.Field()
    id_cancelled: Series[int] = pa.Field(ge=0)
    mesonet_station: Series[str] = pa.Field()
    id_active_weather: Series[int] = pa.Field(nullable=False)


class stg_aircraft_schema(pa.DataFrameModel):
    id_aircraft: Series[int] = pa.Field(ge=0, nullable=False)
    year_of_manufacture: Series[int] = pa.Field(ge=0)
    manufacturer: Series[dtypes.Category] = pa.Field()
    icao_type: Series[str] = pa.Field()
    range: Series[dtypes.Category] = pa.Field()
    width: Series[dtypes.Category] = pa.Field()
