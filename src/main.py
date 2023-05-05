import pandas as pd
from sqlalchemy import create_engine
import logging
import boto3
from pandera_schemas import *
from exceptions import SchemaError
from constants import *
from utils import *
import os
from transform_functions import (
    _standard_transform_in_df,
    _transform_aircrafts,
    _transform_airports,
    _transform_departure_flights,
)

# ------------------------------------------------
# LOGGING
# Configuration
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
)

# create a file handler
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.INFO)

# add the file handler to the logger
logger = logging.getLogger()
logger.addHandler(file_handler)

# ------------------------------------------------

# FUNCTIONS
def read_postgres_database(
    username: str, password: str, host: str, port: str, database: str, sql_script: str
) -> pd.DataFrame:
    """
    This function is used to read a postgres database through a connection.
    It executes a query and returns a pandas dataframe.
    Remember you can only execute a query that returns a table, this table
    will be managed as Pandas Dataframe.

    Arguments:
        username -- db username
        password -- db password
        host -- db host
        port -- db port
        database -- db name
        sql_script -- sql script you want to execute

    Returns:
        pd.DataFrame -- pandas dataframe with the result of the query
    """
    # Definning variables

    try:
        engine = create_engine(
            "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
                username, password, host, port, database
            )
        )
    except Exception as e:
        logging.debug("-- DB CONNECTION Line 55 --")
        logging.error("DB CONNECTION - Error connecting to the database: %s", e)
        return pd.DataFrame()

    try:
        df_departures = pd.read_sql(sql_script, engine)
        df_departures.name = database

        if len(df_departures) != 0:
            print("SUCCESS reading DB")
        else:
            print(":( Database is empty")

    except Exception as e:
        logging.debug("-- DB CONNECTION Line 63 --")
        logging.error("PANDAS READ SQL - Error reading the database: %s", e)
        return pd.DataFrame()
        # raise e

    return df_departures


def read_files(files_list: list) -> list:
    """
    This function is used to read a csv file and return a pandas dataframe.

    Arguments:
        csv_files_list -- list of csv files you want to read

    Returns:
        list(pd.DataFrame) -- list of pandas dataframes
    """
    df_list = []
    for file in files_list:
        # Using str.endswith() method to check extension.
        # Reading files if they have a csv extension.
        if file.endswith(".csv"):
            try:
                file = f"./data/csvFiles/{file}"
                df = pd.read_csv(file, sep=",")
            except Exception as e:
                logging.debug("-- CSV READ Line 91 --")
                logging.error("CSV READ - Error reading the csv file: %s", e)
                raise e
        # Reading files if they have a json extension.
        elif file.endswith(".json"):
            try:
                file = f"./data/jsonFiles/{file}"
                df = pd.read_json(file)
            except Exception as e:
                logging.debug("-- JSON READ Line 101 --")
                logging.error("JSON READ - Error reading the json file: %s", e)
                raise e
        # If the extension is not valid, it will return None immediately and therefore end the function.
        else:
            logging.error("EXTENSION IS NOT VALID - Only csv and json are admitted")
            return None

        # Adding the valid pandas dataframe to the list.
        df.name = file.split("/")[
            -1
        ]  # Obtaining the name of the file, with extension but without path. And assigning as the name of df.
        df_list.append(df)

    return df_list


def extract_and_transform_raw_files_and_convert_to_stg_tables() -> bool:
    result = False

    # EXTRACT
    try:
        # 1. Starting to read the DB containing the main table data.
        df_departures = read_postgres_database(
            username=USERNAME,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            database=DATABASE,
            sql_script=SQL_SCRIPT_GET_ALL_DEPARTURES,
        )
    except Exception as e:
        print("ERROR READING POSTGRES DATABASE")
        logging.error("ERROR READING POSTGRES DATABASE: %s", e)
        return result

    try:
        # 2. Read csv's or json's
        all_files = [
            ACTIVE_WEATHER_FILENAME,
            CANCELLATION_FILENAME,
            CARRIERS_FILENAME,
            AIRPORTS_FILENAME,
        ]
        list_dfs = read_files(all_files)

        # 4. Create dfs dictionary
        # The key is the name of the dataframe which is the same as the file name including its extension, but not including any abs. or rel. path.
        # i.e. 'ActiveWeather.csv' is the name of the dataframe and the key in the dictionary.
        df_dictionary = create_df_dictionary_using_name(*list_dfs)

    except Exception as e:
        print("ERROR READING CSV/JSON FILES")
        logging.error("ERROR READING CSV/JSON FILES: %s", e)
        return result

    # TRANSFORM

    # 5. Standard transformation for all dataframes.
    # stg_active_weather
    stg_active_weather = _standard_transform_in_df(
        df=df_dictionary[ACTIVE_WEATHER_FILENAME],
        df_name=ACTIVE_WEATHER_STG,
        df_types=df_active_weather_types,
        id_name="id_weather",
        pandera_schema=stg_active_weather_schema,  # Passing Pandera class, not instance object.
    )

    # stg_cancellation
    stg_cancellation = _standard_transform_in_df(
        df=df_dictionary[CANCELLATION_FILENAME],
        df_name=CANCELLATION_STG,
        df_types=df_cancellation_types,
        id_name="id_cancellation",
        pandera_schema=stg_cancellation_schema,  # Passing Pandera class, not instance object.
    )

    # stg_carriers
    stg_carriers = _standard_transform_in_df(
        df=df_dictionary[CARRIERS_FILENAME],
        df_name=CARRIERS_STG,
        df_types=df_carriers_types,
        id_name="id_carriers",
        pandera_schema=stg_carriers_schema,  # Passing Pandera class, not instance object.
    )

    # stg_airports
    stg_airports = _transform_airports(
        df=df_dictionary[AIRPORTS_FILENAME],
        df_name=AIRPORTS_STG,
        df_types=df_airports_types,
        pandera_schema=stg_airports_schema,  # Passing Pandera class, not instance object.
        new_df_column_names=df_airports_rename_columns,
    )

    # stg_aircraft
    stg_aircraft = _transform_aircrafts(
        df=df_departures,
        df_aircraft_columns=df_aircraft_columns,
        df_name=AIRCRAFT_STG,
        df_types=df_aircraft_types,
        id_name="id_aircraft",
        pandera_schema=stg_aircraft_schema,  # Passing Pandera class, not instance object.
    )

    # stg_departures
    stg_departures = _transform_departure_flights(
        df=df_departures,
        df_name=DEPARTURES_STG,
        df_types=df_departures_types,
        id_name="id_departure",
        pandera_schema=stg_departures_schema,  # Passing Pandera class, not instance object.
        new_df_column_names=df_departures_rename_columns,
    )

    # DEBUG
    logging.info(stg_active_weather.info())
    logging.info(f"stg_active_weather: {stg_active_weather.info()}")
    logging.info(f"stg_cancellation: {stg_cancellation.info()}")
    logging.debug(f"stg_carriers: {stg_carriers.info()}")
    logging.debug(f"stg_airports: {stg_airports.info()}")
    logging.debug(f"stg_aircraft: {stg_aircraft.info()}")
    logging.debug(f"stg_departures: {stg_departures.info()}")

    print("Generating from Pandas df to CSV: {}".format(stg_active_weather.name))
    # Generate CSV
    stg_active_weather.to_csv(
        "data/staging/{}.csv".format(stg_active_weather.name), index=False
    )
    stg_cancellation.to_csv(
        "data/staging/{}.csv".format(stg_cancellation.name), index=False
    )
    stg_carriers.to_csv("data/staging/{}.csv".format(stg_carriers.name), index=False)
    stg_airports.to_csv("data/staging/{}.csv".format(stg_airports.name), index=False)
    stg_aircraft.to_csv("data/staging/{}.csv".format(stg_aircraft.name), index=False)
    stg_departures.to_csv(
        "data/staging/{}.csv".format(stg_departures.name), index=False
    )

    result = True

    return result

def lookup_for_fk(main_df: pd.DataFrame, fk_df: pd.DataFrame):
    pass
    #for row in main_df.iterrows()

def transform_stg_to_fact_dim_tables(path_to_stg: str, types_of_columns: dict) -> bool:
    #pass
    # TODO: Implement this function.

    fact_table = pd.read_csv("{}/stg_departures.csv".format(path_to_stg))
    # dim_active_weather = pd.read_csv("{}/stg_active_weather.csv".format(path_to_stg))
    # dim_cancellation = pd.read_csv("{}/stg_cancellation.csv".format(path_to_stg))
    dim_carriers = pd.read_csv("{}/stg_carriers.csv".format(path_to_stg))
    dim_airports = pd.read_csv("{}/stg_airports.csv".format(path_to_stg))
    dim_aircraft = pd.read_csv("{}/stg_aircraft.csv".format(path_to_stg))
    
    
    #fact_table = fact_table.astype(df_fact_departures_types)
    #print(fact_table.info())
    
    # Aircraft FK processing
    aircraft_in_fact_table = fact_table[df_aircraft_columns]
    print(aircraft_in_fact_table.info())
    print(aircraft_in_fact_table.head())
    
    #dim_aircraft = dim_aircraft[df_aircraft_columns]
    print(dim_aircraft.info())
    print(dim_aircraft.head())
    
    for index, _ in aircraft_in_fact_table.iterrows():
        for index, _ in dim_aircraft[df_aircraft_columns].iterrows():
            row_aircraft = dim_aircraft.iloc[index]
            fact_row = aircraft_in_fact_table.iloc[index]
            
            if row_aircraft.equals(fact_row):
                print("FOUND MATCH")
                #print(row_aircraft)
                #print(fact_row)
                print('Index', index)
                print( dim_aircraft.iloc[index] )
                break
        break


def load_to_staging_in_s3(path_to_files: str) -> bool:
    """
    Load staging files to S3.

    Arguments:
        path_to_files -- Path to staging files.

    Returns:
        Boolean -- True if files were loaded to S3, False otherwise.
    """

    result = False

    client = boto3.client(
        "s3",
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
    )

    for csv_file_name in os.listdir(path_to_files):

        print("Uploading {} to S3".format(csv_file_name))
        # Upload to S3
        client.upload_file(
            Filename="data/staging/{}".format(csv_file_name),
            Bucket="departures-project-us-2022-juanse",
            Key="staging/{}".format(csv_file_name),
        )
    result = True

    return result


def load_to_S3_to_redshift(path_to_files: str) -> bool:
    """
    Load staging files to S3.

    Arguments:
        path_to_files -- Path to staging files.

    Returns:
        Boolean -- True if files were loaded to S3, False otherwise.
    """

    result = False

    client = boto3.client(
        "s3",
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
    )

    # Uploading all files except fact table
    for csv_file_name in os.listdir(path_to_files):
        if csv_file_name != "stg_departures.csv":
            # Dim table
            new_name = csv_file_name.replace("stg", "dim")

            print("Uploading {} to S3".format(new_name))
            # Upload to S3
            client.upload_file(
                Filename="data/staging/{}".format(csv_file_name),
                Bucket="departures-project-us-2022-juanse",
                Key="redshift-target/{}".format(new_name),
            )
    result = True

    return result


if __name__ == "__main__":
    # 1. Extract and Trnasform
    # if extract_and_transform_raw_files_and_convert_to_stg_tables():
    #     print("Extract and Transform: SUCCESS :)")

    # 2. If transform is successful, we can upload the staging tables to a S3 buckets called Staging.
    path_to_staging_files = "data/staging"
    # if load_to_staging_in_s3(path_to_staging_files):
    #     print("Load to S3: SUCCESS :)")


    transform_stg_to_fact_dim_tables(
        path_to_stg=path_to_staging_files, 
        types_of_columns=df_departures_types
    )

    # 3. Final
    # if load_to_S3_to_redshift(path_to_staging_files):
    #     print("Load to S3 Redshift target: SUCCESS :)")

