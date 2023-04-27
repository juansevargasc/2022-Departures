from main import *
from data_types import *
from exceptions import SchemaError
#from pandera import SchemaErrors

# VARIABLES
# Database in Postgres.
SQL_SCRIPT_GET_ALL_DEPARTURES = "SELECT * FROM departures LIMIT 10000"
USERNAME = "postgres"
PASSWORD = "mysecretpass"
HOST = "localhost"
PORT = "5439"
DATABASE = "departures_db"

# File Names
ACTIVE_WEATHER = 'ActiveWeather'


def _clean_departure_flights(df_departures: pd.DataFrame) -> pd.DataFrame:
    """
    Cleaning departures flights.

    Arguments:
        df_departures -- pandas dataframe with departures flights.

    Returns:
        pd.DataFrame -- pandas dataframe with departures flights cleaned.
    """
    # 1. Drop columns
    print(df_departures.head(10))
    print(df_departures.info())

    return None


def _clean_active_weather(df_active_weather: pd.DataFrame) -> pd.DataFrame:
    """
    Cleaning active weather.

    Arguments:
        df_active_weather -- pandas dataframe with active weather.

    Returns:
        pd.DataFrame -- pandas dataframe with active weather cleaned.
    """
    # 1. Drop columns
    
    df_active_weather['id_weather'] = df_active_weather.index
    df_active_weather.rename(columns={'WEATHER_DESCRIPTION': 'weather_description'}, inplace=True)
    
    print('TITLE', df_active_weather.name)
    print(df_active_weather.head(10))
    
    
    
    # Final Check. Does it comply with the schema?
    try:
        stg_active_weather_schema.validate(stg_active_weather, lazy=True)
    except Exception as e:
        logging.error("Validation error")
        logging.error("ERROR LINE 80: %s", e)
    
    return df_active_weather


if __name__ == "__main__":
    # EXTRACT
    # 1. Starting to read the DB containing the main table data.
    # df_departures = read_postgres_database(
    #     username=USERNAME,
    #     password=PASSWORD,
    #     host=HOST,
    #     port=PORT,
    #     database=DATABASE,
    #     sql_script=SQL_SCRIPT_GET_ALL_DEPARTURES,
    # )
    
    # 2. Read csv's
    all_files = [
        "Cancellation.csv",
        "Carriers.csv",
        "ActiveWeather.csv",
        "stations_data.json",
    ]
    list_dfs = read_files(all_files)
    
     # 4. Create dfs dictionary
    df_dictionary = create_df_dictionary_using_name(*list_dfs)
    df_names = list(df_dictionary.keys())

    # 5
    stg_active_weather = _clean_active_weather(df_dictionary[ACTIVE_WEATHER])
    
   
    
    # TODO: Use custom exceptions.
    # try:
    #     stg_active_weather_schema.validate(stg_active_weather, lazy=True)
    # except SchemaError as err:
    #     logging.error("Validation error")
    #     logging.error("ERROR LINE 80: %s", err)
    #     #logging.error("%s", err.failure_cases)
    #     #logging.error("%s", err.data)
    #       # dataframe of schema errors
    #       # invalid dataframe
        