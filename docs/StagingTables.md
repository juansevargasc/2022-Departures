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
| weather_description | string |

---

### Cancellation

- Name: `stg_cancellation`

**About this file**

Lookup information for the cancellation reason.

| Column | Data Type |
| --- | --- |
| id_cancellation | int64 |
| status | int64 |
| cancellation_reason | string |

---

### Carriers

- Name: `stg_carriers`

**About this file**

Lookup information for the marketing unique carrier and operating unique carrier.

| Column | Data Type |
| --- | --- |
| id_carriers | int64 |
| code | string |
| description | string |

---

## ****************Stations****************

- Name: `stg_airport`

**About this file**

Lookup information for the station/airport.

| Column | dtype |
| --- | --- |
| id_airport | int64 |
| airport_code | string |
| airport_name | string |
| airport_complete_name | string |
| us_state | category |
| us_state_abbr | category |
| latitude | float64 |
| longitude | float64 |
| elevation | int64 |
| icao_code | string |
| iata_code | string |
| mesonet_code | string |

---

### ************************Departures************************

- Name: `stg_departures`

**About this file**

Compiled dataset of US domestic flight data with added airport, and present weather data.

**Cloud Level Encoding:** Low Level: Height < 6500 ft Mid Level: 6500 ft <= Height <= 20000 ft High Level: Height > 20000 ft

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
| dew_point | float64 | The dew point is the temperature to which air must be cooled to become saturated with https://en.wikipedia.org/wiki/Water_vapor, assuming constant air pressure and water content. When cooled below the dew point, https://en.wikipedia.org/wiki/Moisture capacity is reduced and airborne water vapor will https://en.wikipedia.org/wiki/Condensation to form liquid water known as https://en.wikipedia.org/wiki/Dew.https://en.wikipedia.org/wiki/Dew_point#cite_note-1 When this occurs via contact with a colder surface, dew will form on that surface.https://en.wikipedia.org/wiki/Dew_point#cite_note-2 (Dew in spanish: rocío) |
| rel_humidity | float64 | (%) |
| low_level_cloud | Boolean | Cloud Level Encoding:Low Level: Height < 6500 ft  |
| mid_level_cloud | Boolean | Cloud Level Encoding: Mid Level: 6500 ft <= Height <= 20000 f |
| high_level_cloud | Boolean | Cloud Level Encoding: High Level: Height > 20000 ft |
| mkt_unique_carrier | string | Marketing Carrier Unique Code - fk |
| op_unique_carrier | string | Operating Carrier Unique Code. Sometimes a flight can be marketed by one carrier and operated by another - fk |
| origin | string | fk |
| dest | string | fk |
| cancelled | int64 | fk - Already linked as FK |
| mesonet_station | string | What is a mesonet? The term "mesonet" is derived from the words "mesoscale" and "network." In meteorology, a mesonet is typically a network of collectively owned and operated automated weather stations that are installed close enough to each other and report data frequently enough-. Source: https://www.campbellsci.com/mesonets fk (airport station code i.e. JFK) |
| active_weather | int64 | fk - Already linked as FK |


<aside>
💡 Some fileds come with the FK from the external table others with the value itself. They all will become linked with FK's in the following stage.

</aside>

---

**New Tables coming from Departures**

- `stg_aircraft`

**Aircraft Range Encoding** Short Range: Range < 2300 NM Medium Range: 2300 NM <= Range <= 4000 NM Long Range: Range > 4000 NM

| Column Name | DType | Description |
| --- | --- | --- |
| id_aircraft | int64 |  |
| year_of_manufacture | int64 |  |
| manufacturer | category |  |
| icao_type | string | An aircraft type designator is a two-, three- or four-character https://en.wikipedia.org/wiki/Alphanumeric https://en.wikipedia.org/wiki/Code designating every aircraft type (and some sub-types) that may appear in flight planning. These codes are defined by both the https://en.wikipedia.org/wiki/International_Civil_Aviation_Organization (ICAO) and the https://en.wikipedia.org/wiki/International_Air_Transport_Association (IATA). Source: https://en.wikipedia.org/wiki/List_of_aircraft_type_designators - Example: A321 |
| range | category | The maximal total range is the maximum distance an aircraft can fly between takeoff and landing. Powered aircraft range is limited by the aviation fuel energy storage capacity (chemical or electrical) considering both weight and volume limits. **Aircraft Range Encoding Short Range: Range < 2300 NM Medium Range: 2300 NM <= Range <= 4000 NM Long Range: Range > 4000 NM** |
| width | category | Aircraft Body Type Example: Narrow-body.  |