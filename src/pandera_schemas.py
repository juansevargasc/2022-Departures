import pandera as pa
from pandera.typing import Series

class stg_active_weather_schema(pa.DataFrameModel):
    id_weather: Series[int] = pa.Field(ge=0, nullable=False)
    status: Series[int] = pa.Field(ge=0)
    weather_description: Series[str] = pa.Field()

