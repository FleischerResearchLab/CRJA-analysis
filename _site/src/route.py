# pip install openrouteservice
import config
import openrouteservice
from openrouteservice.distance_matrix import distance_matrix
import pandas as pd

def ors(client, loc, profile):
    return distance_matrix(client, locations = loc, profile = profile, 
                        destinations = [1], metrics = ['distance', 'duration'], units = "km")

# dest = [longitude, latitude]
# geisel = [-117.2376,32.8811]
# profiles = [“driving-car”, “foot-walking”, “cycling-regular”]
# 500 request per 40 min
def commute_time(df, dest_name, dest, profile):
    # import API
    client = openrouteservice.Client(key = config.api_key)
    result = df
    
    dist = []
    time = []
    for i, row in df.iterrows():
        loc = [[row['lon'], row['lat']], dest]
        res = ors(client, loc, profile)
        dist.append(res['distances'][0][0])
        time.append(res['durations'][0][0])

    result["To_{}_dist(km)".format(dest_name)] = dist
    result["To_{}_time(min)".format(dest_name)] = [x / 60 for x in time]
    
    return result

