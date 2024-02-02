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
    ![image]