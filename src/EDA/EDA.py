import plotly.express as px
import sys
import os

def eda_report(data):
    '''Te EDA report will create some files to analyze the in deep the variables of the table.
    The elements will be divided by categoric and numeric and some extra info will printed'''

    cabs=data[0]
    trips=data[1]
    
    names=['cabs','trips','loop_trips']
    for df,name in zip(data,names):
        
        describe_result=df.describe()

        eda_path = './files/modeling_output/figures/'

        if not os.path.exists(eda_path):
            os.makedirs(eda_path)

        # Exporting the file
        with open(f'./files/modeling_output/reports/describe_{name}.txt', 'w') as f:
            f.write(describe_result.to_string())

        # Exporting general info
        with open(f'./files/modeling_output/reports/info_{name}.txt','w') as f:
            sys.stdout = f
            df.info()
            sys.stdout = sys.__stdout__
    
    
    
    #Ordenamos los valores de mayor a menor promedio de viajes y redondeamos
    
    hood=trips.sort_values(by='average_trips',ascending=False)
    hood_top_10=hood.head(10)
    hood_top_10['average_trips']=hood_top_10['average_trips'].round(2)
    
    #Creamos un diagrama de barras para visualiazar mejor
    
    fig=px.bar(hood_top_10,x='dropoff_location_name',y='average_trips',title='Top 10 barrios principales', color='dropoff_location_name')
    fig.update_traces(showlegend=False)
    fig.write_image(eda_path+'fig.png', format='png', scale=2)
    fig.write_html(eda_path+'fig.html')
    
    #Ordenamos de mayor a menor las empresas con más viajes
    
    taxi_company=cabs.sort_values(by='trips_amount',ascending=False)
    top10_taxi_company=taxi_company.head(10)
    
    #Creamos diagrama de barras para visualizar mejor
    
    fig1=px.bar(top10_taxi_company,x='company_name',y='trips_amount',title='Top 10 empresas de taxi principales', color='company_name')
    fig1.update_traces(showlegend=False)
    fig1.write_image(eda_path+'fig1.png', format='png', scale=2)
    fig1.write_html(eda_path+'fig1.html')
