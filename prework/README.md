# Prework
The prework here is the process of translating two CSV files, 
one to a PostgreSQL database and the other into a JSON file that contains the columns as 
Python dictionary would.

The idea is to provide two different sources other than CSV files to the main project and 
simulate an ETL pipeline use case.

the files that are given in this dataset:
[2022 U.S. Domestic Flights Departures](https://www.kaggle.com/datasets/jl8771/2022-us-airlines-domestic-departure-data)

<figure>
    <img src="../img/Screenshot 2023-04-20 at 12.39.04 PM.png"
         alt="Kaggle Dataset Flight Dep.">
    <figcaption>Author: Jacky Luo</figcaption>
</figure>

And the dataset contains the following:

```shell
 > tree data/csvFiles/
data/csvFiles/
├── ActiveWeather.csv
├── Cancellation.csv
├── Carriers.csv
├── CompleteData.csv
└── Stations.csv
```
---

## 1. Building a Relational DB in Postgres
The file that will be chosen for this is the **main file** which contains all the flight departures:
`CompleteData.csv`. It is even convenient if you want to explore the data set and make some
SQL queries.

- It all starts in the `prework_etl.ipynb` notebook where we take the CSV to read it with Pandas.
The column list is the following:
```python
[
    FL_DATE
    DEP_HOUR
    MKT_UNIQUE_CARRIER
    MKT_CARRIER_FL_NUM
    OP_UNIQUE_CARRIER
    OP_CARRIER_FL_NUM
    TAIL_NUM
    ORIGIN
    DEST
    DEP_TIME
    CRS_DEP_TIME
    TAXI_OUT
    DEP_DELAY
    AIR_TIME
    DISTANCE
    CANCELLED
    LATITUDE
    LONGITUDE
    ELEVATION
    MESONET_STATION
    YEAR OF MANUFACTURE
    MANUFACTURER
    ICAO TYPE
    RANGE
    WIDTH
    WIND_DIR
    WIND_SPD
    WIND_GUST
    VISIBILITY
    TEMPERATURE
    DEW_POINT
    REL_HUMIDITY
    ALTIMETER
    LOWEST_CLOUD_LAYER
    N_CLOUD_LAYER
    LOW_LEVEL_CLOUD
    MID_LEVEL_CLOUD
    HIGH_LEVEL_CLOUD
    CLOUD_COVER
    ACTIVE_WEATHER
]
```

40 columns

From here int he notebook I standardize names to be lower case, and rename the dataframe coluns with the update.

- Then the table creation script (the sql comments are further information about the specific column and the dataset but you can ignore them):

```SQL
CREATE TABLE IF NOT EXISTS departures (
    fl_date DATE,
    dep_hour INTEGER,  -- INTEGER IS 4 byte integer
    mkt_unique_carrier VARCHAR(15), -- Marketing Unique Carrier Code
    mkt_carrier_fl_num INTEGER, -- Marketing carrier flight number
    op_unique_carrier VARCHAR(15),
    op_carrier_fl_num INTEGER,
    tail_num VARCHAR(15),-- FAA Number Registration
    origin  VARCHAR(15),
    dest VARCHAR(15),
    dep_time TIMESTAMP,
    crs_dep_time TIMESTAMP,
    taxi_out INTEGER, -- Taxi Out Time (Minutes)
    dep_delay INTEGER,-- Departure Delay (Minutes)
    air_time INTEGER, -- (Minutes)
    distance FLOAT, -- Distance Between Airports (Miles)
    cancelled INTEGER, -- FK to cancelled table
    latitude FLOAT,
    longitude FLOAT,
    elevation FLOAT, -- (Feet)
    mesonet_station VARCHAR(15), -- FK to Stations
    year_of_manufacture INTEGER, -- Only Year
    manufacturer VARCHAR(15), -- Manufacturer Aircraft
    icao_type VARCHAR(5), -- Aircraft ICAO Type Designator
    range VARCHAR(15), -- Range of Aircraft
    width VARCHAR(15), -- Aircraft Body Type
    wind_dir FLOAT, -- Wind direction
    wind_spd FLOAT, -- Wind Speed
    wind_gust FLOAT, -- Wind Gust (kt) -> knots
    visibility FLOAT, -- (mi) -> miles
    temperature FLOAT, -- (C°)
    dew_point FLOAT, -- (C°) The dew point is the temperature to which air must be cooled to become saturated with water vapor, assuming constant air pressure and water content.
    rel_humidity FLOAT, -- (%) Relative Humidity
    altimeter FLOAT, -- Altimeter Setting/Pressure (in Hg)
    lowest_cloud_layer FLOAT, -- (ft)
    n_cloud_layer FLOAT, --
    low_level_cloud FLOAT, -- Low Cloud Layer Present?
    mid_level_cloud FLOAT, -- Mid Cloud Layer Present?
    high_level_cloud FLOAT, --  High Cloud Layer Present?
    cloud_cover FLOAT, -- Cloud Cover
    active_weather INTEGER -- FK Active Weather Table
);
```

- [Optional] If you want to use Docker for your Postgres Database, you can use:

```shell
docker run -d --rm --name=postgres  -p 5439:5439 -v /Your-User/your-path-for-postgres-data:/var/lib/postgresql/data -e POSTGRES_PASSWORD=mysecretpass postgres
```

- To load the CSV file you want into the database, you can use:

```SQL
COPY departures (fl_date,dep_hour,mkt_unique_carrier,mkt_carrier_fl_num,op_unique_carrier,op_carrier_fl_num,tail_num,
    origin,dest,dep_time,crs_dep_time,taxi_out,dep_delay,air_time,distance,cancelled,latitude,longitude,
    elevation,mesonet_station,year_of_manufacture,manufacturer,icao_type,range,width,wind_dir,wind_spd,
    wind_gust,visibility,temperature,dew_point,rel_humidity,altimeter,lowest_cloud_layer,n_cloud_layer,
    low_level_cloud,mid_level_cloud,high_level_cloud,cloud_cover,active_weather
    )
    FROM '/var/lib/postgresql/data/stage_departures.csv' -- This is the case for my csv called stage_departures.csv that is within the docker volume for the container.
    DELIMITER ','
    CSV HEADER;
```