import pandas as pd
import subprocess

file_in = './avia_par_es/avia_par_es.tsv'
file_out = './avia_par_es/avia_par_es_fixed.csv'

cwd1 = f"sed 's/\t/,/g' {file_in} > {file_out}"
cwd2 = fr"sed -i 's;airp_pr\\time;airpts;g' {file_out}"
cwd3 = f"sed -i 's/:/0/g' {file_out}"
cwd4 = f"sed -i 's/ //g' {file_out}"
cwd5 = f"sed -i 's/LSZM/LFSB/g' {file_out}"

subprocess.run(cwd1, shell=True)    #change the '\t' present to make everything consistently comma separated
subprocess.run(cwd2, shell=True)    #change weird header name
subprocess.run(cwd3, shell=True)    #change ':' to '0'
subprocess.run(cwd4, shell=True)    #remove white spaces
subprocess.run(cwd5, shell=True)

df = pd.read_csv(file_out, sep=',')
for i, row in df.iterrows():
    txt_airpts = row['airpts']
    splits_airpts = txt_airpts.split('_')
    df.at[i, 'country_dep'] = splits_airpts[0]
    df.at[i, 'country_arr'] = splits_airpts[2]
    df.at[i, 'airpt_dep'] = splits_airpts[1]
    df.at[i, 'airpt_arr'] = splits_airpts[3]

#delete old col
df = df.drop('airpts',axis=1)

#reorder cols
cols = list(df.columns.values)
cols.insert(2, cols.pop(-1))
cols.insert(2, cols.pop(-1))
cols.insert(2, cols.pop(-1))
cols.insert(2, cols.pop(-1))

df = df[cols]

df = df.to_csv(file_out, index=None, header=True, sep=',')
