COPY departures (fl_date,dep_hour,mkt_unique_carrier,mkt_carrier_fl_num,op_unique_carrier,op_carrier_fl_num,tail_num,
    origin,dest,dep_time,crs_dep_time,taxi_out,dep_delay,air_time,distance,cancelled,latitude,longitude,
    elevation,mesonet_station,year_of_manufacture,manufacturer,icao_type,range,width,wind_dir,wind_spd,
    wind_gust,visibility,temperature,dew_point,rel_humidity,altimeter,lowest_cloud_layer,n_cloud_layer,
    low_level_cloud,mid_level_cloud,high_level_cloud,cloud_cover,active_weather
    )
--FROM 'stage_departures.csv'
    FROM '/var/lib/postgresql/data/stage_departures.csv'
    DELIMITER ','
    CSV HEADER;