import pandas as pd
import subprocess
import csv


unit = "PAS_CRD"

units_map = {"PAS_CRD":"pax"}

file_in = './avia_par_es/avia_par_es_fixed.csv'
file_airports = './other_data/airports.csv'

df = pd.read_csv(file_in, sep=',')
airports_data = pd.read_csv(file_airports, sep=',', engine='python', skipinitialspace=True)

def parse_airport_data(airport, year, unit):
    unit_s = units_map[unit]
    file_out = f'./custom_data/{year}_{unit_s}_{airport}.csv'

    data_from_airport = df[(df['airpt_dep']==airport) & (df['tra_meas']==unit)]
    destinations_data = data_from_airport[['airpt_arr', year]]
    destinations_data = destinations_data.rename(columns={year: 'value'})
    destinations_data = destinations_data.sort_values(by=['value'], ascending=False)

    # print(LEBL_destinations_pax_2018)
    # LEBL_destinations_pax_2018.to_csv(file_out, index=None, header=False, sep=',')

    dep_airport = airports_data[airports_data['ident']==airport].iloc[0]
    dep_lat = dep_airport['latitude_deg']
    dep_lon = dep_airport['longitude_deg']

    for i, row in destinations_data.iterrows():
        if row['value'] == 0:
            destinations_data.drop(i, inplace=True)
            continue

        airpt_arr = row['airpt_arr']
        rows_airpt = airports_data[airports_data['ident']==airpt_arr]
        if len(rows_airpt) < 1:
            destinations_data.drop(i, inplace=True)
            continue

        row_airpt = rows_airpt.iloc[0]
        destinations_data.at[i,'airpt_dep'] = airport
        destinations_data.at[i,'airpt_dep_lat'] = dep_lat
        destinations_data.at[i,'airpt_dep_lon'] = dep_lon
        destinations_data.at[i,'airpt_arr_lat'] = row_airpt['latitude_deg']
        destinations_data.at[i,'airpt_arr_lon'] = row_airpt['longitude_deg']

    destinations_data.to_csv(file_out, index=None, header=True, sep=',')

if __name__ == '__main__':
    departure_airports = df['airpt_dep'].unique()
    arrival_airports = df['airpt_arr'].unique()

    #prune to a subset of only the airports we need for faster queries later
    airports_data = airports_data[(airports_data['ident'].isin(departure_airports)) | (airports_data['ident'].isin(arrival_airports))]

    for year in range(2001, 2019):
        for airport in departure_airports:
            print(f"{year} - {airport}")
            parse_airport_data(airport, str(year), unit)
