import pandas
import matplotlib.pyplot as plt

filename = './avia_par_es/avia_par_es_fixed.csv'
df = pandas.read_csv(filename, sep=',')

#print("ES_LEBL_ES_LEMD" in df['airpts'].unique())
#print("ES_LEMD_ES_LEBL" in df['airpts'].unique())

#cols = ['2000M01', '2000M02', '2000M03', '2000M04','2000M05','2000M06', '2000M07', '2000M08', '2000M09', '2000M10','2000M11','2000M12',
cols_2018 = ['2018M01', '2018M02', '2018M03', '2018M04','2018M05','2018M06', '2018M07', '2018M08', '2018M09', '2018M10','2018M11','2018M12']

cols_months = [ '2001M01', '2001M02', '2001M03', '2001M04','2001M05','2001M06', '2001M07', '2001M08', '2001M09', '2001M10','2001M11','2001M12',
                '2002M01', '2002M02', '2002M03', '2002M04','2002M05','2002M06', '2002M07', '2002M08', '2002M09', '2002M10','2002M11','2002M12',
                '2003M01', '2003M02', '2003M03', '2003M04','2003M05','2003M06', '2003M07', '2003M08', '2003M09', '2003M10','2003M11','2003M12',
                '2004M01', '2004M02', '2004M03', '2004M04','2004M05','2004M06', '2004M07', '2004M08', '2004M09', '2004M10','2004M11','2004M12',
                '2005M01', '2005M02', '2005M03', '2005M04','2005M05','2005M06', '2005M07', '2005M08', '2005M09', '2005M10','2005M11','2005M12',
                '2006M01', '2006M02', '2006M03', '2006M04','2006M05','2006M06', '2006M07', '2006M08', '2006M09', '2006M10','2006M11','2006M12',
                '2007M01', '2007M02', '2007M03', '2007M04','2007M05','2007M06', '2007M07', '2007M08', '2007M09', '2007M10','2007M11','2007M12',
                '2008M01', '2008M02', '2008M03', '2008M04','2008M05','2008M06', '2008M07', '2008M08', '2008M09', '2008M10','2008M11','2008M12',
                '2009M01', '2009M02', '2009M03', '2009M04','2009M05','2009M06', '2009M07', '2009M08', '2009M09', '2009M10','2009M11','2009M12',
                '2010M01', '2010M02', '2010M03', '2010M04','2010M05','2010M06', '2010M07', '2010M08', '2010M09', '2010M10','2010M11','2010M12',
                '2011M01', '2011M02', '2011M03', '2011M04','2011M05','2011M06', '2011M07', '2011M08', '2011M09', '2011M10','2011M11','2011M12',
                '2012M01', '2012M02', '2012M03', '2012M04','2012M05','2012M06', '2012M07', '2012M08', '2012M09', '2012M10','2012M11','2012M12',
                '2013M01', '2013M02', '2013M03', '2013M04','2013M05','2013M06', '2013M07', '2013M08', '2013M09', '2013M10','2013M11','2013M12',
                '2014M01', '2014M02', '2014M03', '2014M04','2014M05','2014M06', '2014M07', '2014M08', '2014M09', '2014M10','2014M11','2014M12',
                '2015M01', '2015M02', '2015M03', '2015M04','2015M05','2015M06', '2015M07', '2015M08', '2015M09', '2015M10','2015M11','2015M12',
                '2016M01', '2016M02', '2016M03', '2016M04','2016M05','2016M06', '2016M07', '2016M08', '2016M09', '2016M10','2016M11','2016M12',
                '2017M01', '2017M02', '2017M03', '2017M04','2017M05','2017M06', '2017M07', '2017M08', '2017M09', '2017M10','2017M11','2017M12',
                '2018M01', '2018M02', '2018M03', '2018M04','2018M05','2018M06', '2018M07', '2018M08', '2018M09', '2018M10','2018M11','2018M12']

cols_years = [  '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
        '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']

flights_from_LEBL = df[(df['airpt_dep']=="LEBL") & (df['tra_meas']=="CAF_PAS")]
flights_from_LEBL_to_US = df[(df['airpt_dep']=="LEBL") & (df['country_arr']=="US") & (df['tra_meas']=="CAF_PAS")]

# sum_flights_from_LEBL = flights_from_LEBL[cols_years].sum()
# plot1 = sum_flights_from_LEBL.plot(x ='t', y='flights', kind = 'bar')
# plot1.get_figure().savefig('flights_from_LEBL.pdf', format='pdf')
# plt.clf()

pax_from_LEBL = df[(df['airpt_dep']=="LEBL") & (df['tra_meas']=="PAS_CRD")]
pax_from_LEBL_to_US = df[(df['airpt_dep']=="LEBL") & (df['country_arr']=="US") & (df['tra_meas']=="PAS_CRD")]

sum_pax_from_LEBL = pax_from_LEBL[cols_years].sum()
# print(sum_pax_from_LEBL)
plot2 = sum_pax_from_LEBL.plot(kind = 'bar')
plot2.get_figure().savefig('pax_from_LEBL.pdf', format='pdf')

plt.clf()

sum_pax_from_LEBL_2018 = pax_from_LEBL[cols_2018].sum()
# print(sum_pax_from_LEBL_2018)
plot3 = sum_pax_from_LEBL_2018.plot(kind = 'bar')
plot3.get_figure().savefig('pax_from_LEBL_2018.pdf', format='pdf')

plt.clf()

sum_pax_from_LEBL_all = pax_from_LEBL[cols_months].sum()
# print(sum_pax_from_LEBL_2018)
plot4 = sum_pax_from_LEBL_all.plot(kind = 'area')
plot4.get_figure().savefig('sum_pax_from_LEBL_all.pdf', format='pdf')


LEBL_destinations_pax_2018 = pax_from_LEBL[['airpt_arr', '2018']]
LEBL_destinations_pax_2018 = LEBL_destinations_pax_2018.sort_values(by=['2018'], ascending=False)
# print(LEBL_destinations_pax_2018.head(10))

LEBL_destinations_flights_2018 = flights_from_LEBL[['airpt_arr', '2018']]
LEBL_destinations_flights_2018 = LEBL_destinations_flights_2018.sort_values(by=['2018'], ascending=False)
# print(LEBL_destinations_flights_2018.head(10))


#print(len(df['airpts'].unique()))
#print(df['unit'].unique())
#print(df['tra_meas'].unique())
