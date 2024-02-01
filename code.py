 ## Análisis exploratorio de datos:
#%% 1. Importar librerías
import pandas as pd
import numpy as np
from scipy import stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
#%% Importar archivos
cabs=pd.read_csv('datasets/moved_project_sql_result_01.csv')
trips=pd.read_csv('datasets/moved_project_sql_result_04.csv')
loop_trips=pd.read_csv('datasets/moved_project_sql_result_07.csv')
#%% Imprimimos los dataframes 
print(cabs.head(5))
print()
print(trips.head(5))
print()
print(loop_trips.head(5))
#%% Revisamos los tipos de datos de los dataframes
print(cabs.info())
print()
print(trips.info())
print()
print(loop_trips.info())
# %%
