import pandas as pd
from src.preprocessing.weather_records import weather_conditions
def load_datasets():
    '''This function will upload the necessary datasets
    to perform the project.'''
    cabs=pd.read_csv('./files/datasets/input/moved_project_sql_result_01.csv')
    trips=pd.read_csv('./files/datasets/input/moved_project_sql_result_04.csv')
    loop_trips=pd.read_csv('./files/datasets/input/moved_project_sql_result_07.csv')
    weather_conditions()
    return cabs,trips,loop_trips