from main import *

# VARIABLES
# Database in Postgres.
SQL_SCRIPT_GET_ALL_DEPARTURES = "SELECT * FROM departures LIMIT 10000"
USERNAME = "postgres"
PASSWORD = "mysecretpass"
HOST = "localhost"
PORT = "5439"
DATABASE = "departures_db"

def _clean_departure_flights(df_departures: pd.DataFrame) -> pd.DataFrame:
    """
    Cleaning departures flights.

    Arguments:
        df_departures -- pandas dataframe with departures flights.

    Returns:
        pd.DataFrame -- pandas dataframe with departures flights cleaned.
    """
    # 1. Drop columns
    print ( df_departures.head(10) )
    print( df_departures.info() )
    
    
    
    
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
    df_active_weather.head(10)
    
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
    all_files = ["Cancellation.csv", "Carriers.csv", "ActiveWeather.csv", "stations_data.json"]
    list_dfs = read_files(all_files)
    
    # 3. Cleaning active weather.
    
    _clean_active_weather(df_active_weather)

    