import pandera as pa
from pandera.typing import Series


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
    # airport_name
