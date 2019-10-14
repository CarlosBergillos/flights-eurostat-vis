import pandas as pd
import subprocess
import csv

units_map = {"PAS_CRD":"pax", "CAF_PAS":"flights"}

file_in = './avia_par_es/avia_par_es_fixed.csv' 

df = pd.read_csv(file_in, sep=',')
departure_airports = df['airpt_dep'].unique()

def parse_airport_data(airport, timeperiods, units):
    data_from_airport = df[df['airpt_dep']==airport]
    result = pd.DataFrame()
    file_out = f'./custom_data/{airport}.csv'
    for unit in units:
      unit2 = units_map[unit]
      data_from_airport_unit = data_from_airport[data_from_airport['tra_meas']==unit]
      sums_from_airport_unit = data_from_airport_unit[timeperiods].sum()
      sums_from_airport_unit = sums_from_airport_unit.to_frame(unit2)
      if result.empty:
        result = sums_from_airport_unit
      else:
        result = pd.concat([result, sums_from_airport_unit], axis=1)
    result.to_csv(file_out, index=True, index_label='timeperiod', sep=',')

if __name__ == '__main__':
    # years = [str(x) for x in range(2001, 2019)]
    timeperiods = []
    for year in range(2001, 2019):
        for month in range (1, 13):
            timeperiods.append(f'{year}M{month:02}')

    units = ["PAS_CRD", "CAF_PAS"]

    for airport in departure_airports:
    # for airport in ["LEBL"]:
        print(f"{airport}")
        parse_airport_data(airport, timeperiods, units)
