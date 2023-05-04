from main import (
    read_postgres_database,
    create_df_dictionary_using_name,
    read_files,
    logging,
    pd,
)
from pandera_schemas import *
from exceptions import SchemaError
from constants import *
from utils import read_schema_column_datatypes


def _standard_transform_in_df(
    df: pd.DataFrame,
    df_name: str,
    df_types: dict,
    id_name: str,
    pandera_schema: pa.DataFrameModel,
) -> pd.DataFrame:
    """
    Standard transformation for all dataframes.

    Arguments:
        df -- Pandas dataframe.
        df_name -- Dataframe name.
        df_types -- Dictionary with column names and data types.
        id_name -- Primary key column name.
        pandera_schema -- Pandera schema.

    Returns:
        Transformed dataframe.
    """

    # 1. Add id_weather PK column
    df[id_name] = df.index

    # 2. Change column naming to lowercase.
    new_columns = {column: column.lower() for column in df.columns}
    df.rename(columns=new_columns, inplace=True)

    # 4. Enforce data types.
    df = df.astype(df_types, copy=False)

    # 3. Change name.
    df.name = df_name

    # DEBUG
    # print("TITLE", df.name)
    # print(df.head(10))
    # print(df.info())

    # Final Check. Does it comply with the schema?
    try:
        pandera_schema.validate(df, lazy=True)
    except Exception as e:
        print("\nERROR in schema validation. See app.logs for more details")
        logging.error("Validation error")
        logging.error("ERROR LINE 80: %s", e)

    return df


def _transform_airports(
    df: pd.DataFrame,
    df_name: str,
    df_types: dict,
    pandera_schema: pa.DataFrameModel,
    new_df_column_names,
) -> pd.DataFrame:

    # 1. Columns to drop.
    df = df.drop("FAA", axis=1)

    # 2. Change column naming to lowercase.
    df.rename(columns=new_df_column_names, inplace=True)

    # 4. Enforce data types.
    df = df.astype(df_types, copy=False)

    # 3. Change name.
    df.name = df_name

    # DEBUG
    # print("TITLE", df.name)
    # print(df.head(10))
    # print(df.info())

    # Final Check. Does it comply with the schema?
    try:
        pandera_schema.validate(df, lazy=True)
    except Exception as e:
        print("\nERROR in schema validation. See app.logs for more details")
        logging.error("Validation error")
        logging.error("ERROR LINE 80: %s", e)

    return df


def _separate_aircraft_table_from_main_table(
    df: pd.DataFrame, desired_columns: list
) -> pd.DataFrame:
    """
    Separate aircraft table from main table.
    """
    df_aircrafts = df[desired_columns].drop_duplicates()

    return df_aircrafts


def _transform_aircrafts(
    df: pd.DataFrame,
    df_aircraft_columns: list,
    df_name: str,
    df_types: dict,
    id_name: str,
    pandera_schema: pa.DataFrameModel,
) -> pd.DataFrame:
    """
    Transform aircrafts dataframe.

    Arguments:
        df -- df_departures dataframe, where we will get the aircrafts.
        df_columns -- Columns to keep.
        df_name -- df Name.
        df_types -- df Types-
        pandera_schema -- Pandera schema.
    Returns:
        Transoformed df_aircrafts -- df with aircrafts.
    """
    # 1. Get df_aircrafts from df_departures. Duplicates are already taken care of.
    df_aircrafts = _separate_aircraft_table_from_main_table(df, df_aircraft_columns)

    # 2. id_aircraft PK column
    df_aircrafts.reset_index(inplace=True, drop=True)
    df_aircrafts[id_name] = df_aircrafts.index

    # 4. Enforce data types.
    df_aircrafts = df_aircrafts.astype(df_types, copy=False)

    # 3. Change name.
    df_aircrafts.name = df_name

    # DEBUG
    print("TITLE", df_aircrafts.name)
    print(df_aircrafts.head(10))
    print(df_aircrafts.info())

    # Final Check. Does it comply with the schema?
    try:
        pandera_schema.validate(df_aircrafts, lazy=True)
    except Exception as e:
        print("\nERROR in schema validation. See app.logs for more details")
        logging.error("Validation error")
        logging.error("ERROR LINE 80: %s", e)

    return df_aircrafts

def cast_to_int(number) -> int:
    try:
        result = float(number)
        result = int(result)
        #print(result)
    except Exception:
        print(f'This value {number} cannot be casted to int. Continue...')
        logging.debug('Value cannot be casted')
        return number
    return result

def _transform_departure_flights(
    df: pd.DataFrame,
    df_name: str,
    df_types: dict,
    id_name: str,
    pandera_schema: pa.DataFrameModel,
    new_df_column_names: dict
) -> pd.DataFrame:
    """
    Cleaning departures flights.

    Arguments:
        df_departures -- pandas dataframe with departures flights.

    Returns:
        pd.DataFrame -- pandas dataframe with departures flights cleaned.
    """
    # DEBUG
    print("BEFORE", df_departures.head(10))
    print(df_departures.info())

    # 1. Rename
    df.rename(columns=new_df_column_names, inplace=True)
    
    # 2. Index
    df[id_name] = df.index
    
    # 3. Take Columns of interest
    df = df[df_departures_columns]
    print("AFTER", df.info())

    # 4. Duplicate values
    df.drop_duplicates(inplace=True)
    
    # Based on data exploration 'Active Weather' already a FK, is int and not float
    # Filling nan's
    df['active_weather'] = df['active_weather'].fillna(-1)
    df['active_weather'] = df['active_weather'].apply(lambda x: cast_to_int(x))

    # 
    df['high_level_cloud'] = df['high_level_cloud'].fillna(0)

    # 5. Enforce data types.
    try:
        df = df.astype(df_types, copy=False)
    except Exception as e:
        print('Certain df type could not be converted. Continue...')
        logging.error("DF TYPE CANNOT BE CONVERTED: %s", e)

    # 6. Change name.
    df.name = df_name

    # DEBUG
    print("TITLE", df.name)
    print(df.head(10))
    print(df.info())

    # Final Check. Does it comply with the schema?
    try:
        pandera_schema.validate(df, lazy=True)
    except Exception as e:
        print("\nERROR in schema validation. See app.logs for more details")
        logging.error("Validation error")
        logging.error("ERROR LINE 80: %s", e)

    return df


if __name__ == "__main__":
    # EXTRACT
    # 1. Starting to read the DB containing the main table data.
    df_departures = read_postgres_database(
        username=USERNAME,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        database=DATABASE,
        sql_script=SQL_SCRIPT_GET_ALL_DEPARTURES,
    )

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
    df_names = list(df_dictionary.keys())

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
    cols = df_departures.columns.to_list()

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
        new_df_column_names=df_departures_rename_columns
    )

    # df_aircraft_columns

    # 6.
    print("\n", "--" * 20)
    read_schema_column_datatypes("columns.txt")
