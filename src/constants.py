# CONSTANTS

# VARIABLES
# Database in Postgres.
SQL_SCRIPT_GET_ALL_DEPARTURES = (
    "SELECT * FROM departures ORDER BY fl_date ASC LIMIT 1000"
)
USERNAME = "postgres"
PASSWORD = "mysecretpass"
HOST = "localhost"
PORT = "5439"
DATABASE = "departures_db"

# File Names
ACTIVE_WEATHER_FILENAME = "ActiveWeather.csv"
CANCELLATION_FILENAME = "Cancellation.csv"
CARRIERS_FILENAME = "Carriers.csv"
AIRPORTS_FILENAME = "stations_data.json"

# Staging Dataframe Names
ACTIVE_WEATHER_STG = "stg_active_weather"
CANCELLATION_STG = "stg_cancellation"
CARRIERS_STG = "stg_carriers"
AIRPORTS_STG = "stg_airports"
AIRCRAFT_STG = "stg_aircraft"
DEPARTURES_STG = "stg_departures"

# Dataframe Types
df_active_weather_types = {
    "id_weather": "int64",
    "status": "int64",
    "weather_description": "string",  # We could also use astype('|S') which will by default set the length to the max len it encounters.
}

df_cancellation_types = {
    "id_cancellation": "int64",
    "status": "int64",
    "cancellation_reason": "string",
}

df_carriers_types = {
    "id_carriers": "int64",
    "code": "string",
    "description": "string",
}

df_airports_types = {
    "id_airport": "int64",
    "airport_code": "string",
    "airport_name": "string",
    "airport_complete_name": "string",
    "us_state": "category",
    "us_state_abbr": "category",
    "latitude": "float64",
    "longitude": "float64",
    "elevation": "int64",
    "icao_code": "string",
    "iata_code": "string",
    "mesonet_code": "string",
}

df_departures_types = {
    "id_departure": "int64",
    "flight_date": "datetime64[ns]",
    "dep_hour": "int64",
    "mkt_carrier_fl_num": "int64",
    "op_carrier_fl_num": "int64",
    "dep_time": "datetime64[ns]",
    "crs_dep_time": "datetime64[ns]",
    "taxi_out": "int64",
    "dep_delay": "int64",
    "air_time": "int64",
    "distance": "float64",
    "wind_dir": "float64",
    "wind_speed": "float64",
    "wind_gust": "float64",
    "visibility": "float64",
    "temperature": "float64",
    "dew_point": "float64",
    "rel_humidity": "float64",
    "low_level_cloud": "bool",
    "mid_level_cloud": "bool",
    "high_level_cloud": "bool",
    "mkt_unique_carrier": "string",
    "op_unique_carrier": "string",
    "origin": "string",
    "dest": "string",
    "cancelled": "int64",
    "mesonet_station": "string",
    "active_weather": "int64",
}

df_aircraft_types = {
    "id_aircraft": "int64",
    "year_of_manufacture": "int64",
    "manufacturer": "category",
    "icao_type": "string",
    "range": "category",
    "width": "category",
}

# Columns
df_aircraft_columns = [
    "year_of_manufacture",
    "manufacturer",
    "icao_type",
    "range",
    "width",
]

df_departures_columns = [
    "id_departure",
    "flight_date",
    "dep_hour",
    "mkt_carrier_fl_num",
    "op_carrier_fl_num",
    "dep_time",
    "crs_dep_time",
    "taxi_out",
    "dep_delay",
    "air_time",
    "distance",
    "wind_dir",
    "wind_speed",
    "wind_gust",
    "visibility",
    "temperature",
    "dew_point",
    "rel_humidity",
    "low_level_cloud",
    "mid_level_cloud",
    "high_level_cloud",
    "mkt_unique_carrier",
    "op_unique_carrier",
    "origin",
    "dest",
    "cancelled",
    "mesonet_station",
    "active_weather",
]

# Rename Columns
df_airports_rename_columns = {
    "AIRPORT_ID": "id_airport",
    "AIRPORT": "airport_code",
    "DISPLAY_AIRPORT_NAME": "airport_name",
    "DISPLAY_AIRPORT_CITY_NAME_FULL": "airport_complete_name",
    "AIRPORT_STATE_NAME": "us_state",
    "AIRPORT_STATE_CODE": "us_state_abbr",
    "LATITUDE": "latitude",
    "LONGITUDE": "longitude",
    "ELEVATION": "elevation",
    "ICAO": "icao_code",
    "IATA": "iata_code",
    # "FAA": "faa",
    "MESONET_STATION": "mesonet_code",
}

df_departures_rename_columns = {
    "wind_spd": "wind_speed",
    "fl_date": "flight_date"
}