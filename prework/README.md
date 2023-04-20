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

Contain the following:
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

It all starts in the `prework_etl.ipynb` notebook where we take the CSV to read it with Pandas.
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