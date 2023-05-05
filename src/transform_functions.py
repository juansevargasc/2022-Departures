import pandas as pd
import logging
from pandera_schemas import *
from constants import *
from utils import *

# Trnasform Functions
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

    # Final Check. Does it comply with the schema?
    try:
        pandera_schema.validate(df_aircrafts, lazy=True)
    except Exception as e:
        print("\nERROR in schema validation. See app.logs for more details")
        logging.error("Validation error")
        logging.error("ERROR LINE 80: %s", e)

    return df_aircrafts


def _transform_departure_flights(
    df: pd.DataFrame,
    df_name: str,
    df_types: dict,
    id_name: str,
    pandera_schema: pa.DataFrameModel,
    new_df_column_names: dict,
) -> pd.DataFrame:
    """
    Cleaning departures flights.

    Arguments:
        df_departures -- pandas dataframe with departures flights.

    Returns:
        pd.DataFrame -- pandas dataframe with departures flights cleaned.
    """
    # 1. Rename
    df.rename(columns=new_df_column_names, inplace=True)

    # 2. Index
    df[id_name] = df.index

    # 3. Take Columns of interest
    #df = df[df_departures_columns]

    # 4. Duplicate values
    df.drop_duplicates(inplace=True)

    # Based on data exploration 'Active Weather' already a FK, is int and not float
    # Filling nan's
    df.loc[:, "active_weather"] = df["active_weather"].fillna(-1)
    df["active_weather"] = df["active_weather"].apply(lambda x: cast_to_int(x))

    # Filling nan's for booleans
    df["high_level_cloud"] = df["high_level_cloud"].fillna(0)
    df["mid_level_cloud"] = df["mid_level_cloud"].fillna(0)
    df["low_level_cloud"] = df["low_level_cloud"].fillna(0)

    # 5. Enforce data types.
    try:
        df = df.astype(df_types, copy=False)
    except Exception as e:
        print("Certain df type could not be converted. Continue...")
        logging.error("DF TYPE CANNOT BE CONVERTED: %s", e)

    # 6. Change name.
    df.name = df_name

    # Final Check. Does it comply with the schema?
    try:
        pandera_schema.validate(df, lazy=True)
    except Exception as e:
        print("\nERROR in schema validation. See app.logs for more details")
        logging.error("Validation error")
        logging.error("ERROR LINE 80: %s", e)

    return df
