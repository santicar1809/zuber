import pandas as pd
import numpy as np
from scipy import stats as st

"""La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare cambia los sábados lluviosos.

H0: La duración promedio de los viajes entre Loop hasta el Aeropuerto Internacional O'hare los días lluviosos y los días soleados es igual.  
H1: La duración promedio de los viajes entre Loop hasta el Aeropuerto Internacional O'hare los días lluviosos y los días soleados **NO** es igual.  
Indice de significancia del 5%"""

def hypotesis_test(data):
    result_list=[]
    loop_trips=data[2]
    #Separamos los datos de días lluviosos y dias soleados
    good_trips=loop_trips[loop_trips['weather_conditions']=='Good']['duration_seconds']
    bad_trips=loop_trips[loop_trips['weather_conditions']=='Bad']['duration_seconds']
    var_good=np.var(good_trips)
    var_bad=np.var(bad_trips)
    print(f'Varianza de los días soleados: {var_good}\nVarianza de los días lluviosos: {var_bad}')
    #Hacemos la prueba de hipotesis
    alpha=0.05
    results=st.ttest_ind(good_trips,bad_trips)
    print(f'El promedio de los viajes soleados : {good_trips.mean()}\nEl promedio de los viajes lluviosos es : {bad_trips.mean()}\n\nt-statistic: {results[0]}\np-value: {results[1]}')
    if results.pvalue < alpha: # comparar el valor p con el umbral
        result="Rechazamos la hipótesis nula"
        print(result)
    else:
        result="No podemos rechazar la hipótesis nula"
        print(result)
    result_list.extend([var_good,var_bad,good_trips.mean(),bad_trips.mean(),results[0],results[1],result])
    results_df=pd.Series(result_list,index=['var_good','var_bad','good_trips_mean','bad_trips_mean','t-statistic','p-value','result'])
    results_df.to_csv('./files/modeling_output/reports/hypotesis_test.csv')
    
    return results_df