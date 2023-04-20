
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

