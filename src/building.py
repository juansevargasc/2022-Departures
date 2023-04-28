from main import create_df_dictionary_using_name, read_files, logging, pd
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

    # 6.
    print("\n", "--" * 20)
    read_schema_column_datatypes("columns.txt")
