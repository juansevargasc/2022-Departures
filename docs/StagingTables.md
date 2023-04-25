# Staging Tables

# Staging Tables  🥈

### ActiveWeather

- Name: `stg_active_weather`

**About this file**

Lookup information for active weather status encoding.

| Column | Data Type |
| --- | --- |
| id_weather | int64 |
| status | int64 |
| weather_description | object |

---

### Cancellation

- Name: `stg_cancellation`

**About this file**

Lookup information for the cancellation reason.

| Column | Data Type |
| --- | --- |
| id_cancellation | int64 |
| status | int64 |
| cancellation_reason | object |

---

### Carriers

- Name: `stg_carriers`

**About this file**

Lookup information for the marketing unique carrier and operating unique carrier.

| Column | Data Type |
| --- | --- |
| id_carriers | int64 |
| code | object |
| description | object |

---

## ****************Stations****************

- Name: `stg_airport`

**About this file**

Lookup information for the station/airport.

| Column | dtype |
| --- | --- |
| id_airport | int64 |
| airport_code | object |
| airport_name | object |
| airport_complete_name | object |
| us_state | object |
| us_state_abbr | object |
| latitude | float64 |
| longitude | float64 |
| elevation | int64 |
| icao_code | object |
| iata_code | object |
| faa_code | object |
| mesonet_code | object |

---

### ************************Departures************************

- Name: `stg_departures`

**About this file**

Compiled dataset of US domestic flight data with added airport, aircraft and present weather data.

**Aircraft Range Encoding** Short Range: Range < 2300 NM Medium Range: 2300 NM <= Range <= 4000 NM Long Range: Range > 4000 NM

**Cloud Level Encoding:**Low Level: Height < 6500 ft Mid Level: 6500 ft <= Height <= 20000 ft High Level: Height > 20000 ft

| Column Name | Data Type | Description |
| --- | --- | --- |
| id_departure | int64 | Unique id for departure |
| flight_date | datetime64[ns] |  |
| dep_hour | int64 |  |
| mkt_carrier_fl_num | int64 | Marketing Carrier Flight Number |
| op_carrier_fl_num | int64 | Op. Carrier Flight Number |
| dep_time | datetime64[ns] | Local time. |
| crs_dep_time | datetime64[ns] | Scheduled departure time, local time. |
| taxi_out | int64 | (in minutes) |
| dep_delay | int64 | (in minutes) |
| air_time | int64 | (in minutes) |
| distance | float64 | (in mi) |
| wind_dir | float64 | (°) angule  |
| wind_speed | float64 | (in kt) |
| wind_gust | float64 | (in kt) (In spanish: ráfaga) |
| visibility | float64 | (in mi) |
| temperature | float64 | (in C) |
| dew_point | float64 | The dew point is the temperature to which air must be cooled to become saturated with https://en.wikipedia.org/wiki/Water_vapor, assuming constant air pressure and water content. When cooled below the dew point, https://en.wikipedia.org/wiki/Moisture capacity is reduced and airborne water vapor will https://en.wikipedia.org/wiki/Condensation to form liquid water known as https://en.wikipedia.org/wiki/Dew https://en.wikipedia.org/wiki/Dew_point#cite_note-1 When this occurs via contact with a colder surface, dew will form on that surface.https://en.wikipedia.org/wiki/Dew_point#cite_note-2 (Dew in spanish: rocío) |
| rel_humidity | float64 | (%) |
| low_level_cloud | Boolean | Cloud Level Encoding:
Low Level: Height < 6500 ft  |
| mid_level_cloud | Boolean | Cloud Level Encoding:
Mid Level: 6500 ft <= Height <= 20000 f |
| high_level_cloud | Boolean | Cloud Level Encoding:
High Level: Height > 20000 ft |
| mkt_unique_carrier | int64 | Marketing Carrier Unique Code
fk |
| op_unique_carrier | int64 | Operating Carrier Unique Code. Sometimes a flight can be marketed by one carrier and operated by another. 
fk |
| origin | int64 | fk |
| dest | int64 | fk |
| cancelled | int64 | fk |
| mesonet_station | int64 | What is a mesonet? The term "mesonet" is derived from the words "mesoscale" and "network." In meteorology, a mesonet is typically a network of collectively owned and operated automated weather stations that are installed close enough to each other and report data frequently enough-. Source: https://www.campbellsci.com/mesonets fk (airport station code i.e. JFK) |
| active_weather | object | fk |

<aside>
💡 Fk Fields highlighted are already associated to an existing dim table.

</aside>

---

**New Tables coming from Departures**

- `stg_aircraft`
    - year_of_manufacture
    - manufacturer_name
    - icao_type
    - range
    - width

| Column Name | DType | Description |
| --- | --- | --- |
| year_of_manufacture | int64 |  |
| manufacturer | object |  |
| icao_type | object | An aircraft type designator is a two-, three- or four-character code designating every aircraft type (and some sub-types) that may appear in flight planning. 
These codes are defined by both the ICAO and the [IATA](https://en.wikipedia.org/wiki/International_Air_Transport_Association) - Source: https://en.wikipedia.org/wiki/List_of_aircraft_type_designators. Example: A321 |
| range | object | The maximal total range is the maximum distance an aircraft can fly between takeoff and landing. Powered aircraft range is limited by the aviation fuel energy storage capacity (chemical or electrical) considering both weight and volume limits. Aircraft Range Encoding Short Range: Range < 2300 NM Medium Range: 2300 NM <= Range <= 4000 NM Long Range: Range > 4000 NM |
| width | object | Aircraft Body Type  Example: Narrow-body. |