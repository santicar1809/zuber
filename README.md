# Descripción del proyecto

Estás trabajando como analista para Zuber, una nueva empresa de viajes compartidos que se está lanzando en Chicago. Tu tarea es encontrar patrones en la información disponible. Quieres comprender las preferencias de los pasajeros y el impacto de los factores externos en los viajes.
Al trabajar con una base de datos, analizarás los datos de los competidores y probarás una hipótesis sobre el impacto del clima en la frecuencia de los viajes.

## Descripción de los datos

### Una base de datos con información sobre viajes en taxi en Chicago:

1. tabla neighborhoods: datos sobre los barrios de la ciudad

- name: nombre del barrio
- neighborhood_id: código del barrio  

2. tabla cabs: datos sobre los taxis  

- cab_id: código del vehículo
- vehicle_id: ID técnico del vehículo
- company_name: la empresa propietaria del vehículo  

3. tabla trips: datos sobre los viajes

- trip_id: código del viaje
- cab_id: código del vehículo que opera el viaje
- start_ts: fecha y hora del inicio del viaje (tiempo redondeado a la hora)
- end_ts: fecha y hora de finalización del viaje (tiempo redondeado a la hora)
- duration_seconds: duración del viaje en segundos
- distance_miles: distancia del viaje en millas
- pickup_location_id: código del barrio de recogida
- dropoff_location_id: código del barrio de finalización  

4. tabla weather_records: datos sobre el clima

- record_id: código del registro meteorológico
- ts: fecha y hora del registro (tiempo redondeado a la hora)
- temperature: temperatura cuando se tomó el registro
- description: breve descripción de las condiciones meteorológicas, por ejemplo, "lluvia ligera" o "nubes dispersas"

## Diagrama ER

![Alt text](https://github.com/santicar1809/zuber/blob/master/datasets/238116676-2edba3f3-131c-40eb-b0d0-273d6213d7db.png)

## Preguntas SQL  

 1. Encuentra la cantidad de viajes en taxi para cada compañía de taxis para el 15 y 16 de noviembre de 2017, asigna al campo resultante el nombre trips_amount e imprímelo también. Ordena los resultados por el campo trips_amount en orden descendente.

 2. Encuentra la cantidad de viajes para cada empresa de taxis cuyo nombre contenga las palabras "Yellow" o "Blue" del 1 al 7 de noviembre de 2017. Nombra la variable resultante trips_amount. Agrupa los resultados por el campo company_name.

 3. Del 1 al 7 de noviembre de 2017, las empresas de taxis más populares fueron Flash Cab y Taxi Affiliation Services. Encuentra el número de viajes de estas dos empresas y asigna a la variable resultante el nombre trips_amount. Junta los viajes de todas las demás empresas en el grupo "Other". Agrupa los datos por nombres de empresas de taxis. Asigna el nombre company al campo con nombres de empresas de taxis. Ordena el resultado en orden descendente por trips_amount.

 4. Recupera los identificadores de los barrios de O'Hare y Loop de la tabla neighborhoods.

 5. Para cada hora recupera los registros de condiciones meteorológicas de la tabla weather_records. Usando el operador CASE, divide todas las horas en dos grupos: Bad si el campo description contiene las palabras rain o storm, y Good para los demás. Nombra el campo resultante weather_conditions. La tabla final debe incluir dos campos: fecha y hora (ts) y weather_conditions.

 6. Recupera de la tabla de trips todos los viajes que comenzaron en el Loop (pickup_location_id: 50) el sábado y terminaron en O'Hare (dropoff_location_id: 63). Obtén las condiciones climáticas para cada viaje. Utiliza el método que aplicaste en la tarea anterior. Recupera también la duración de cada viaje. Ignora los viajes para los que no hay datos disponibles sobre las condiciones climáticas.
    Las columnas de la tabla deben estar en el siguiente orden:
    - start_ts
    - weather_conditions
    - duration_seconds
    - Ordena por trip_id.

## Análisis en python

Una vez se extrae la infomación de las tablas de ProtgresSQL, se queda corto para hacer un análisis más gráfico y estadistico, por lo cual pasamos las consultas de SQL a archivos csv que analizaremos con más detalle en python.

### Ahora tenemos estos tres CSV:

1. /datasets/project_sql_result_01.csv. contiene los siguientes datos:

- company_name: nombre de la empresa de taxis
- trips_amount: el número de viajes de cada compañía de taxis el 15 y 16 de noviembre de 2017. 

2. /datasets/project_sql_result_04.csv. contiene los siguientes datos:

- dropoff_location_name: barrios de Chicago donde finalizaron los viajes
- average_trips: el promedio de viajes que terminaron en cada barrio en noviembre de 2017.

3. /datasets/project_sql_result_07.csv — el resultado de la última consulta. Contiene datos sobre viajes desde el Loop hasta el Aeropuerto Internacional O'Hare. 
Estos son los valores de campo de la tabla:

- start_ts: fecha y hora de la recogida
- weather_conditions: condiciones climáticas en el momento en el que comenzó el viaje
- duration_seconds: duración del viaje en segundos.

## Instrucciones:

- importar los archivos
- estudiar los datos que contienen
- asegurarte de que los tipos de datos sean correctos
- identificar los 10 principales barrios en términos de finalización del recorrido
- hacer gráficos: empresas de taxis y número de viajes, los 10 barrios principales por número de finalizaciones
- sacar conclusiones basadas en cada gráfico y explicar los resultados

## Conclusiones:

1. En conclusión los 3 barrios más populares en cuanto a finalización de viajes son Loop, River North y Streeterville debido a que su promedio de viajes es más alto, esto se debe a que la mayoría de estos barrios y el resto de barrios de la lista quedan en el Downtown y cerga al lago michigan los cuales son las zonas turisticas más representativas de Chicago. El unico barrio que no queda cerca a la zona es O'Hare, el cual es el barrio donde está el aeropuerto, por esta razón se encuentra en la lista, al Chicago ser una de las ciudades más turisticas de Estados Unidos, recibe más viajes en sus destinos turisticos.

2. Las 3 empresas más conocidas de Chicago son Flash Cab, Taxi Afiliation Services y Medallion Leasing, los cuales son buenas opciones para invertir debido a su alta cantidad de viajes, sin embargo, sería importante hacer un análisis más detallado de estas empresas.

## Gráficos

![Alt text](https://github.com/santicar1809/zuber/blob/master/datasets/barplot_hoods)

![Alt text](https://github.com/santicar1809/zuber/blob/master/datasets/barplot_company)
