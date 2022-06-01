

### This is a script to access NOAA tide and current data

import pandas as pd
import numpy as np
import requests as re

## a bunch of observations for a single station

sample_request = re.get('https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?begin_date=20211030 15:00&end_date=20220523 15:00&station=8454000&product=hourly_height&units=english&time_zone=gmt&application=ports_screen&format=json&datum=STND')

sample_json = sample_request.json()
data_df = pd.DataFrame(sample_json["data"])
data_df.head()

##This is a version that runs through a shorter timeframe (I ended up going with a couple days, but this is arbitrary) but for more stations (I used five sample ones from SoCal, but again this is arbitrary.

## get the last week of data (May 17 7:00 p.m. to May 24 7:00 p.m.) for 5 stations
## i pulled 5 southern california stations out of a hat
## stations: (1) oil platform harvest (9411406), Santa Barbara (9411340), Santa Monica (9410840), "Los Angeles" (9410660), La Jolla (9410230)

list_of_stations = [
    9411406,
    9411340,
    9410840,
    9410660,
    9410230
    ]

master_df_list = []
for station in list_of_stations:
    station_input = station
    url = 'https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?begin_date=20150823 15:00&end_date=20150825 15:00&station=' + \
        str(station_input) + \
            '&product=hourly_height&units=english&time_zone=gmt&application=ports_screen&format=json&datum=STND'
    sample_request = re.get(url)
    print(sample_request)
    sample_json = sample_request.json()
    ## this gives you station ID, station name, station latitude, and station longitude.
    # data_df = pd.DataFrame(sample_json["metadata"], index = [0])
    ## this gives you the actual data (note: this is somewhat specific to the "product" you're looking for)
    data_df = pd.DataFrame(sample_json["data"])
    master_df_list.append(data_df)

master_df_out = pd.concat(master_df_list)
master_df_out.head()


