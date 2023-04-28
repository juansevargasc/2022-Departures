# Raw Tables  🥉
- Original column and table names.
- Original schema and data types. 
___

## ActiveWeather

**About this file**

Lookup information for active weather status encoding.

| Column | Data Type |
| --- | --- |
| STATUS | int64 |
| WEATHER_DESCRIPTION | object |

---

## Cancellation

**About this file**

Lookup information for the cancellation reason.

| Column | Data Type |
| --- | --- |
| STATUS | int64 |
| CANCELLATION_REASON | object |

---

## Carriers

**About this file**

Lookup information for the marketing unique carrier and operating unique carrier.

| Column | Data Type |
| --- | --- |
| CODE | object |
| DESCRIPTION | object |

---

## ****************Stations****************

**About this file**

Lookup information for the station/airport.

| Column | Dtype |
| --- | --- |
| AIRPORT_ID | int64 |
| AIRPORT | object |
| DISPLAY_AIRPORT_NAME | object |
| DISPLAY_AIRPORT_CITY_NAME_FULL | object |
| AIRPORT_STATE_NAME | object |
| AIRPORT_STATE_CODE | object |
| LATITUDE | float64 |
| LONGITUDE | float64 |
| ELEVATION | int64 |
| ICAO | object |
| IATA | object |
| FAA | object |
| MESONET_STATION | object |

---

## ************************CompleteData************************

**About this file**

Compiled dataset of US domestic flight data with added airport, aircraft and present weather data.

**Aircraft Range Encoding** Short Range: Range < 2300 NM Medium Range: 2300 NM <= Range <= 4000 NM Long Range: Range > 4000 NM

**Cloud Level Encoding:** Low Level: Height < 6500 ft Mid Level: 6500 ft <= Height <= 20000 ft High Level: Height > 20000 ft

| Column Name | Data Type | Description |
| --- | --- | --- |
| id_departure | int64 | Unique id for departure |
| flight_date | datetime64[ns] |  |
| dep_hour | int64 |  |
| mkt_unique_carrier | object | Marketing Carrier Unique Code
fk |
| mkt_carrier_fl_num | int64 | Marketing Carrier Flight Number |
| op_unique_carrier | object | Operating Carrier Unique Code. Sometimes a flight can be marketed by one carrier and operated by another. 
fk |
| op_carrier_fl_num | int64 | Op. Carrier Flight Number |
| tail_num | object | FAA N-Number/Registration |
| origin | object | fk |
| dest | object | fk |
| dep_time | datetime64[ns] |  |
| crs_dep_time | datetime64[ns] |  |
| taxi_out | int64 | (in minutes) |
| dep_delay | int64 | (in minutes) |
| air_time | int64 | (in minutes) |
| distance | float64 | (in mi) |
| cancelled | int64 | fk |
| latitude | float64 |  |
| longitude | float64 |  |
| elevation | float64 | (in ft) |
| mesonet_station | object | What is a mesonet? The term "mesonet" is derived from the words "mesoscale" and "network." In meteorology, a mesonet is typically a network of collectively owned and operated automated weather stations that are installed close enough to each other and report data frequently enough-. Source: https://www.campbellsci.com/mesonets - fk (airport station code i.e. JFK) |
| year_of_manufacture | int64 |  |
| manufacturer | object |  |
| icao_type | object | An aircraft type designator is a two-, three- or four-character https://en.wikipedia.org/wiki/Alphanumeric https://en.wikipedia.org/wiki/Code designating every aircraft type (and some sub-types) that may appear in flight planning. These codes are defined by both the https://en.wikipedia.org/wiki/International_Civil_Aviation_Organization (ICAO) and the https://en.wikipedia.org/wiki/International_Air_Transport_Association (IATA). Source: https://en.wikipedia.org/wiki/List_of_aircraft_type_designators |
| range | object | The maximal total range is the maximum distance an aircraft can fly between takeoff and landing. Powered aircraft range is limited by the aviation fuel energy storage capacity (chemical or electrical) considering both weight and volume limits. Aircraft Range Encoding Short Range: Range < 2300 NM Medium Range: 2300 NM <= Range <= 4000 NM Long Range: Range > 4000 NM |
| width | object | Aircraft Body Type |
| wind_dir | float64 | (°) angule  |
| wind_speed | float64 | (in kt) |
| wind_gust | float64 | (in kt) (In spanish: ráfaga) |
| visibility | float64 | (in mi) |
| temperature | float64 | (in C) |
| dew_point | float64 | (in C) |
| rel_humidity | float64 | (%) |
| altimeter | float64 | (in Hg) |
| lowest_cloud_layer | float64 | (in ft) |
| n_cloud_layer | float64 | Number of cloud layers |
| low_level_cloud | Boolean | Low level cloud? |
| mid_level_cloud | Boolean | Mid-level cloud? |
| high_level_cloud | Boolean | High level cloud? |
| cloud_cover | float64 | Low Level: Height < 6500 ft Mid Level: 6500 ft <= Height <= 20000 ft High Level: Height > 20000 ft |
| active_weather | object | fk |

---