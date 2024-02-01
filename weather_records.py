##Código para obtener la tabla de weather_records de la web
import requests
from bs4 import BeautifulSoup
import pandas as pd
URL='https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html'
req=requests.get(URL)
attr={"id": "weather_records"}
soup=BeautifulSoup(req.text,'lxml')
weather=soup.find('table',attr)
#print(weather_records)
header_table=[]
content=[]
for row in weather.find_all('th'):
    header_table.append(row.text)
for row in weather.find_all('tr'):
    if not row.find_all('th'):
        content.append([element.text for element in row.find_all('td')])
weather_records=pd.DataFrame(content,columns=header_table)
print(weather_records)