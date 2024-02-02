/*Herramienta usada -ProtsgreSQL
Como los datos del proyecto se encuentran en la plataforma de TripleTen, todos los ejercicios de SQL serán ejecutados en la web de TripleTen.
Febrero - 2024 */
----------------------------------------------------------------------------
-- Analisis de pregundas--
/*1.  
Encuentra la cantidad de viajes en taxi para cada compañía de taxis para el 15 y 16 de noviembre de 2017, asigna al campo resultante el nombre trips_amount e imprímelo también. 
Ordena los resultados por el campo trips_amount en orden descendente.*/
/*--------------Solucion-------------*/
SELECT 
    cabs.company_name,
    COUNT(cabs.company_name) AS trips_amount
FROM
    cabs INNER JOIN 
    trips ON trips.cab_id=cabs.cab_id
WHERE 
    trips.start_ts::date BETWEEN '2017-11-15' AND '2017-11-16'
GROUP BY 
    cabs.company_name
ORDER BY 
    COUNT(cabs.company_name) DESC;
/*Explicacion*/
/*Con esta tabla obtenemos la cantidad de viajes que hace cada compañia en Chicago contando el número de veces 
que aparece cada nombre de cada compañia, entre el 15 de noviembre y el 16 de noviembre*/

/*2. 
Encuentra la cantidad de viajes para cada empresa de taxis cuyo nombre contenga las palabras "Yellow" o "Blue" 
del 1 al 7 de noviembre de 2017. Nombra la variable resultante trips_amount. Agrupa los resultados por el campo company_name.*/
/*--------------Solucion-------------*/
SELECT 
    cabs.company_name, 
    COUNT(cabs.company_name) AS trips_amount
FROM
    cabs INNER JOIN
    trips ON trips.cab_id = cabs.cab_id
WHERE
    (cabs.company_name LIKE '%Yellow%' OR 
    cabs.company_name LIKE '%Blue%')
    AND trips.start_ts::date BETWEEN '2017-11-1' AND '2017-11-7'
GROUP BY 
    cabs.company_name;
/*Expliacion*/
/*Contamos el número de veces que se repetía cada nombre de la compañia para agrupar las empresas y 
se filtra únicamente las empresas con 'blue' o 'yellow' en su nombre y que fuera del 1 al 7 de noviembre, 
despues ordenamos los datos por el campo del nombre de la empresa.*/

/*3. 
Del 1 al 7 de noviembre de 2017, las empresas de taxis más populares fueron Flash Cab y Taxi Affiliation Services. 
Encuentra el número de viajes de estas dos empresas y asigna a la variable resultante el nombre trips_amount. 
Junta los viajes de todas las demás empresas en el grupo "Other". Agrupa los datos por nombres de empresas de taxis. 
Asigna el nombre company al campo con nombres de empresas de taxis. Ordena el resultado en orden descendente por trips_amount.*/
/*--------------Solucion-------------*/
SELECT 
    CASE WHEN cabs.company_name ='Flash Cab' THEN 'Flash Cab'
    WHEN cabs.company_name = 'Taxi Affiliation Services' THEN 'Taxi Affiliation Services'
    ELSE 'Other' END AS company,
    COUNT(trips.trip_id) AS trips_amount
FROM
    cabs INNER JOIN
    trips ON trips.cab_id=cabs.cab_id
WHERE
    trips.start_ts::date BETWEEN '2017-11-01' AND '2017-11-07'
GROUP BY
    company
ORDER BY
    trips_amount DESC;
/*Expliacion*/
/*Creamos un caso para sumar los datos de la empresa 'Flash Cab' y 'Taxi Affiliation Services', 
y clasificar las demás como 'Otros', luego filtramos los valores desde el primero de noviembre hasta el siete de noviembre,
agrupando todo por el nuevo caso que hicimos y ordenandolo de mayor número de viajes a menor.*/
/*4.
Recupera los identificadores de los barrios de O'Hare y Loop de la tabla neighborhoods.*/ 
/*--------------Solucion-------------*/
SELECT 
    neighborhood_id,name
FROM
    neighborhoods
WHERE
    name LIKE '%Hare' OR name LIKE 'Loop';  
/*Expliacion*/
/*En esta query seleccionamos el id del barrio y su nombre, posteriormente filtramos por los barrios Loop y O'Hare.*/
/*5.
Para cada hora recupera los registros de condiciones meteorológicas de la tabla weather_records. 
Usando el operador CASE, divide todas las horas en dos grupos: 
Bad si el campo description contiene las palabras rain o storm, y Good para los demás. 
Nombra el campo resultante weather_conditions. 
La tabla final debe incluir dos campos: fecha y hora (ts) y weather_conditions.*/
/*--------------Solucion-------------*/
SELECT
    ts,
    CASE WHEN description LIKE '%rain%' THEN 'Bad'
    WHEN description LIKE '%storm%' THEN 'Bad'
    ELSE 'Good' END AS weather_conditions
FROM
    weather_records
GROUP BY
    ts,
    weather_conditions;
/*Expliacion*/
/*Creamos un caso en el que los valores donde las condiciones tengan palablas como 'storm' o 'rain' sea clasificado como malo
y el resto como bueno, de esa manera podemos clasificar el clima en 2, buen clima o mal clima.*/
/*6.
Recupera de la tabla de trips todos los viajes que comenzaron en el Loop (pickup_location_id: 50) 
el sábado y terminaron en O'Hare (dropoff_location_id: 63). 
Obtén las condiciones climáticas para cada viaje. 
Utiliza el método que aplicaste en la tarea anterior. 
Recupera también la duración de cada viaje. 
Ignora los viajes para los que no hay datos disponibles sobre las condiciones climáticas.
Las columnas de la tabla deben estar en el siguiente orden:
 - start_ts
 - weather_conditions
 - duration_seconds
 - Ordena por trip_id.*/
/*--------------Solucion-------------*/
SELECT
    trips.start_ts,
    T.weather_conditions,
    trips.duration_seconds
FROM
    trips INNER JOIN 
    (SELECT
        ts,
        CASE WHEN weather_records.description LIKE '%rain%' THEN 'Bad'
        WHEN weather_records.description LIKE '%storm%' THEN 'Bad'
        ELSE 'Good' END AS weather_conditions
    FROM
        weather_records) T
    ON T.ts= trips.start_ts
WHERE
    trips.pickup_location_id = 50 AND  trips.dropoff_location_id=63 AND EXTRACT (DOW from trips.start_ts) = 6
ORDER BY
    trips.trip_id;
/*Expliacion*/
/*Para este caso debemos crear un caso en una consulta interna donde tengamos los datos del clima unidos 
con los datos de los viajes. Posteriormente filtramos los datos por la locación Loop y O'Hare, 
teniendo en cuenta solo los sábados, y ordenando los datos por el id del viaje.

