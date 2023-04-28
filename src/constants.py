# CONSTANTS

# VARIABLES
# Database in Postgres.
SQL_SCRIPT_GET_ALL_DEPARTURES = "SELECT * FROM departures LIMIT 10000"
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

df_stations_types = {
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
    "low_level_cloud": "Boolean",
    "mid_level_cloud": "Boolean",
    "high_level_cloud": "Boolean",
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
