import pandas as pd
from sqlalchemy import create_engine
import logging
import os


# VARIABLES
# Database in Postgres.
SQL_SCRIPT_GET_ALL_DEPARTURES = "SELECT * FROM departures LIMIT 20"
USERNAME = 'postgres'
PASSWORD = 'mysecretpass'
HOST = 'localhost'
PORT = '5439'
DATABASE = 'departures_db'

# PATHS to files
# CSV files
weather_csv_file = '../data/weather.csv'


# ------------------------------------------------
# LOGGING
# Configuration
logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s')

# ------------------------------------------------



def run_example():
    a = 'Run this example'
    b = os.path.abspath('../')
    print('This is only for DEBUG')
    print('{} - This is the path: {}'.format(a, b))
    print('--'*40)

def read_postgres_database(username: str, password: str, host: str, port: str, database: str, sql_script: str) -> pd.DataFrame:
    '''
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
    '''
    # Definning variables
    
    try:
        engine = create_engine(
            'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
                username,
                password,
                host,
                port,
                database   
            )
        )
    except Exception as e:
        logging.debug('-- DB CONNECTION Line 55 --')
        logging.error('DB CONNECTION - Error connecting to the database: %s', e)
        return pd.DataFrame()
    
    
    try:
        df_departures = pd.read_sql(sql_script, engine)
    except Exception as e:
        logging.debug('-- DB CONNECTION Line 63 --')
        logging.error('PANDAS READ SQL - Error reading the database: %s', e)
        return pd.DataFrame()
        #raise e
    
    return df_departures

def read_csv_files(csv_files_list: list()) -> list():
    '''
    This function is used to read a csv file and return a pandas dataframe.

    Arguments:
        csv_files_list -- list of csv files you want to read

    Returns:
        list(pd.DataFrame) -- list of pandas dataframes
    '''
    df_list = []
    for csv_file in csv_files_list:
        try:
            df = pd.read_csv(csv_file)
            df_list.append(df)
        except Exception as e:
            logging.debug('-- CSV READ Line 91 --')
            logging.error('CSV READ - Error reading the csv file: %s', e)
            raise e
    return df_list

def read_json_files(json_files_list: list()) -> list():
    '''
    This function is used to read a json file and return a pandas dataframe.

    Arguments:
        json_files_list -- list of json files you want to read

    Returns:
        list(pd.DataFrame) -- list of pandas dataframes
    '''
    df_list = []
    for json_file in json_files_list:
        try:
            df = pd.read_json(json_file)
            df_list.append(df)
        except Exception as e:
            logging.debug('-- JSON READ Line 113 --')
            logging.error('JSON READ - Error reading the json file: %s', e)
            raise e
    return df_list

if __name__ == '__main__':
    run_example()
    
    # 1. Starting to read the DB containing the main table data.
    df_departures = read_postgres_database(
        username=USERNAME,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        database=DATABASE,
        sql_script=SQL_SCRIPT_GET_ALL_DEPARTURES
    )
    
    if len(df_departures) != 0:
        print(df_departures.head(10))
        print('SUCCESS')
    else:
        print( ':( Something went wrong' )
