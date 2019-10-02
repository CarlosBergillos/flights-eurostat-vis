import pandas as pd
import subprocess
import csv

airport = "LEMD"
year = "2018"

file_in = './avia_par_es/avia_par_es_fixed.csv'
file_airpts = './other_data/airports.csv'
file_out = f'./custom_data/{airport}_destinations_pax_'+year+'.csv'

df = pd.read_csv(file_in, sep=',')

pax_from_LEBL = df[(df['airpt_dep']==airport) & (df['tra_meas']=="PAS_CRD")]
LEBL_destinations_pax_2018 = pax_from_LEBL[['airpt_arr', year]]
LEBL_destinations_pax_2018 = LEBL_destinations_pax_2018.rename(columns={year: 'pax'+year})
LEBL_destinations_pax_2018 = LEBL_destinations_pax_2018.sort_values(by=['pax'+year], ascending=False)

# print(LEBL_destinations_pax_2018)
# LEBL_destinations_pax_2018.to_csv(file_out, index=None, header=False, sep=',')

dep_out = subprocess.check_output("q -H -d , \"SELECT latitude_deg, longitude_deg FROM ./other_data/airports.csv WHERE ident='"+airport+"' LIMIT 10\"", shell=True)
dep_out = dep_out.decode("utf-8")[:-1] #b string to normal string and remove last character '\n'
dep_out = dep_out.split(',')

dep_lat = dep_out[0]
dep_lon = dep_out[1]

airpts = pd.read_csv(file_airpts, sep=',', engine='python', skipinitialspace=True)

for i, row in LEBL_destinations_pax_2018.iterrows():
    airpt_arr = row['airpt_arr']
    rows_airpt = airpts[airpts['ident']==airpt_arr]
    if len(rows_airpt) < 1:
        LEBL_destinations_pax_2018.drop(i, inplace=True)
        continue
    row_airpt = rows_airpt.iloc[0]
    LEBL_destinations_pax_2018.at[i,'airpt_dep'] = airport
    LEBL_destinations_pax_2018.at[i,'airpt_dep_lat'] = dep_lat
    LEBL_destinations_pax_2018.at[i,'airpt_dep_lon'] = dep_lon
    LEBL_destinations_pax_2018.at[i,'airpt_arr_lat'] = row_airpt['latitude_deg']
    LEBL_destinations_pax_2018.at[i,'airpt_arr_lon'] = row_airpt['longitude_deg']

LEBL_destinations_pax_2018.to_csv(file_out, index=None, header=True, sep=',')
