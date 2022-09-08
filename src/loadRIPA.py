"""
load RIPA data directly from SD website

example:
from loadRIPA import loadRIPA
result_df=loadRIPA()

optional argument loadRIPA(base='https://whereever.the.base/of/the/data/location/is/')
but that base is set for the current website right now
"""

import pandas as pd
import numpy as np


# utility functions to convert data to type and handle missing values properly
def convert_dtype_float(x):
    if not x:
        return np.NaN
    try:
        return float(x)
    except:
        return np.NaN

def convert_dtype_stopcode(x):
    if not x:
        return -1
    try:
        return int(x)
    except:
        return -1

def convert_dtype_string(x):
    if not x:
        return ''
    try:
        return str(x)
    except:
        return ''

def loadRIPA(base='https://seshat.datasd.org/pd/'):
    # Descriptions of the people stopped as perceived by the officer: disability/gender/race/ethnicity
    disability_df = pd.read_csv(base+"ripa_disability_datasd.csv")
    gender_df = pd.read_csv(base+"ripa_gender_datasd.csv",
                            converters = {"gender": convert_dtype_string})
    race_df = pd.read_csv(base+"ripa_race_datasd.csv")

    # Result of stop: warning, citation, arrest, search, etc
    stop_result_df = pd.read_csv(base+"ripa_stop_result_datasd.csv")

    # Reason for stop: codes and text description [optional/dirty]
    stop_reason_df = pd.read_csv(base+"ripa_stop_reason_datasd.csv",
                             converters = {"reason_for_stopcode": convert_dtype_stopcode})

    # Details: where the stop was made, who the officer was, etc.
    stop_details_df = pd.read_csv(base+"ripa_stops_datasd.csv",
                              converters = {"land_mark": convert_dtype_string,
                                            'date_stop': convert_dtype_string})

    # Search: basis for searches conducted and whether/how/why/what was found
    search_basis_df = pd.read_csv(base+"ripa_search_basis_datasd.csv")
    contraband_df = pd.read_csv(base+"ripa_contraband_evid_datasd.csv")

    # Seizures: basis for seizure and what what was taken
    prop_seize_basis_df = pd.read_csv(base+"ripa_prop_seize_basis_datasd.csv",
                                  converters = {"basisforpropertyseizure": convert_dtype_string})
    prop_seize_type_df = pd.read_csv(base+"ripa_prop_seize_type_datasd.csv",
                                 converters = {"type_of_property_seized": convert_dtype_string})

    
    # put it all together
    result_df = pd.merge(disability_df, gender_df, how="outer", on=["stop_id","pid"])
    result_df = pd.merge(result_df, race_df, how="outer", on=["stop_id","pid"])
    result_df = pd.merge(result_df, stop_result_df, how="outer", on=["stop_id","pid"])
    result_df = pd.merge(result_df, stop_reason_df, how="outer", on=["stop_id","pid"])
    result_df = pd.merge(result_df, stop_details_df, how="outer", on=["stop_id","pid"])
    result_df = pd.merge(result_df, search_basis_df, how="outer", on=["stop_id","pid"])
    result_df = pd.merge(result_df, contradband_df, how="outer", on=["stop_id","pid"])
    result_df = pd.merge(result_df, prop_seize_basis_df, how="outer", on=["stop_id","pid"])
    result_df = pd.merge(result_df, prop_seize_type_df, how="outer", on=["stop_id","pid"])

    # make a consolidated datetime column
    result_df['datetime_stop'] = pd.to_datetime(result_df['date_stop'] + ' ' + result_df['time_stop'], errors='coerce')

    return result_df
