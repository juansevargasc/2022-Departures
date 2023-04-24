# Staging Tables

# Staging Tables  🥈

### Active Weather

- Name: `dim_active_weather`

**About this file**

Lookup information for active weather status encoding.

| Column | Data Type |
| --- | --- |
| id_weather | int64 |
| status | int64 |
| weather_description | object |

---

### Cancellation

- Name: `dim_cancellation`

**About this file**

Lookup information for the cancellation reason.

| Column | Data Type |
| --- | --- |
| id_cancellation | int64 |
| status | int64 |
| cancellation_reason | object |

---

### Carriers

- Name: `dim_carriers`

**About this file**

Lookup information for the marketing unique carrier and operating unique carrier.

| Column | Data Type |
| --- | --- |
| id_carriers | int64 |
| code | object |
| description | object |

---

## ****************Stations****************

- Name: `dim_stations`

**About this file**

Lookup information for the station/airport.

| Column | dtype |
| --- | --- |
| id_airport | int64 |
| airport | object |
| display_airport_name | object |
| display_airport_city_name_full | object |
| airport_state_name | object |
| airport_state_code | object |
| latitude | float64 |
| longitude | float64 |
| elevation | int64 |
| icao | object |
| iata | object |
| faa | object |
| mesonet_station | object |

---

### ************************Departures************************

********************FACT TABLE********************

- Name: `fact_departures`

**About this file**

Compiled dataset of US domestic flight data with added airport, aircraft and present weather data.

**Aircraft Range Encoding**Short Range: Range < 2300 NM Medium Range: 2300 NM <= Range <= 4000 NM Long Range: Range > 4000 NM

**Cloud Level Encoding:**Low Level: Height < 6500 ft Mid Level: 6500 ft <= Height <= 20000 ft High Level: Height > 20000 ft

| Column Name | Data Type | Description |
| --- | --- | --- |
| id_departure | int64 | Unique id for departure |
| fl_date | object |  |
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
| mesonet_station | object | fk |
| year_of_manufacture | int64 |  |
| manufacturer | object |  |
| icao_type | object |  |
| range | object |  |
| width | object |  |
| wind_dir | float64 |  |
| wind_spd | float64 | (in kt) |
| wind_gust | float64 | (in kt) |
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

<aside>
💡 Fields highlighted are already associated to an existing dim table.

</aside>