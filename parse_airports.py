import pandas as pd
import subprocess
import csv

file_in = './avia_par_es/avia_par_es_fixed.csv'
file_airports = './other_data/airports.csv'

file_local_airports_out = './custom_data/local_airports.json'
file_all_airports_out = './custom_data/all_airports.json' 

df = pd.read_csv(file_in, sep=',')
airports_data = pd.read_csv(file_airports, sep=',', engine='python', skipinitialspace=True)
departure_airports = df['airpt_dep'].unique()
arrival_airports = df['airpt_arr'].unique()

def generate_local_airports():
    # local_airports = pd.DataFrame(columns=['airpt', 'name', 'airpt_lat', 'airpt_lon'])
    local_airports = []
    for airpt in departure_airports:
        airpt_data = airports_data[airports_data['ident']==airpt].iloc[0]
        airpt_lat = airpt_data['latitude_deg']
        airpt_lon = airpt_data['longitude_deg']
        airpt_name = airpt_data['name']
        airpt_iata = airpt_data['iata_code']
        pax_sum_2018 =  df[(df['airpt_dep']==airpt)&(df['tra_meas']=="PAS_CRD")]['2018'].sum()
        row = {'airpt':airpt, 'name':airpt_name, 'iata':airpt_iata, 'lat': airpt_lat, 'lon': airpt_lon, 'rank': pax_sum_2018}
        local_airports.append(row)

    local_airports = pd.DataFrame(local_airports)
    local_airports = local_airports.sort_values(by=['rank'], ascending=False)
    local_airports = local_airports.drop(columns=['rank'])
    with open(file_local_airports_out, 'w', encoding='utf-8') as file:
        local_airports.to_json(file, orient='records', force_ascii=False)

def generate_all_airports():
    all_airports = []
    for airpt in arrival_airports:
        airpt_data = airports_data[airports_data['ident']==airpt]
        if len(airpt_data) < 1:
          print(f"Error with {airpt}")
          continue
        airpt_data = airpt_data.iloc[0]
        airpt_name = airpt_data['name']
        airpt_iata = airpt_data['iata_code']
        row = {'icao':airpt, 'iata':airpt_iata, 'name':airpt_name}
        all_airports.append(row)

    all_airports = pd.DataFrame(all_airports)
    with open(file_all_airports_out, 'w', encoding='utf-8') as file:
        all_airports.to_json(file, orient='records', force_ascii=False)

def parse_airport_data(airport, year):
    file_out = f'./custom_data/{year}_{airport}.csv'

    ap_data = df[df['airpt_dep']==airport]

    ap_data_pax = ap_data[ap_data['tra_meas']=="PAS_CRD"]
    ap_data_pax = ap_data_pax[['airpt_arr', year]]
    ap_data_pax = ap_data_pax.rename(columns={'airpt_arr': 'airpt', year: 'pax'})

    ap_data_flights = ap_data[ap_data['tra_meas']=="CAF_PAS"]
    ap_data_flights = ap_data_flights[['airpt_arr', year]]
    ap_data_flights = ap_data_flights.rename(columns={'airpt_arr': 'airpt', year: 'flights'})

    destinations_data = pd.merge(ap_data_pax, ap_data_flights, how='inner', on='airpt')
    destinations_data = destinations_data.sort_values(by=['pax'], ascending=False)

    for i, row in destinations_data.iterrows():
        if (row['pax'] == 0) | (row['flights'] == 0):
            destinations_data.drop(i, inplace=True)
            continue

        airpt = row['airpt']
        rows_airpt = airports_data[airports_data['ident']==airpt]
        if len(rows_airpt) < 1:
            destinations_data.drop(i, inplace=True)
            continue

        row_airpt = rows_airpt.iloc[0]
        destinations_data.at[i,'airpt_iata'] = row_airpt['iata_code']
        destinations_data.at[i,'airpt_lat'] = row_airpt['latitude_deg']
        destinations_data.at[i,'airpt_lon'] = row_airpt['longitude_deg']
        destinations_data.at[i,'airpt_name'] = row_airpt['name']

    destinations_data.to_csv(file_out, index=False, header=True, sep=',')

if __name__ == '__main__':
    generate_local_airports()
    # generate_all_airports()
    #prune to a subset of only the airports we need for faster queries later
    # airports_data = airports_data[(airports_data['ident'].isin(departure_airports)) | (airports_data['ident'].isin(arrival_airports))]

    for year in range(2001, 2019):
        for airport in departure_airports:
        # for airport in ["LEBL"]:
            print(f"{year} - {airport}")
            parse_airport_data(airport, str(year))
