##fix header, convert ':' to 0, and remove whitespaces
sed 's/,/\t/g' avia_par_es.tsv > avia_par_es_fixed.tsv
sed -i 's;airp_pr\\time;airpts;g' avia_par_es_fixed.tsv
sed -i 's/:/0/g' avia_par_es_fixed.tsv
sed -i "s/ //g" avia_par_es_fixed.tsv
##

tra_meas: Traffic and transport measurement
CAF_PAS: Commercial passenger air flights
CAF_PAS_ARR: Commercial passenger air flights (arrivals)
PAS_BRD: Passengers on board
PAS_BRD_ARR: Passengers on board (arrivals)
PAS_CRD: Passengers carried
ST_PAS: Passengers seats available

