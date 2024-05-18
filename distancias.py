from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from Def import obtener_coordenadas, calcular_distancia, calcular_tiempo_y_combustible

ciudad_origen = input("Ingrese la ciudad de origen: ")
ciudad_destino = input("Ingrese la ciudad de destino: ")

distancia = calcular_distancia(ciudad_origen, ciudad_destino)

if distancia:
    print(f"La distancia entre {ciudad_origen} y {ciudad_destino} es de {distancia:.2f} kilómetros.")
    
    velocidad_promedio = float(input("Ingrese la velocidad promedio esperada (en km/h): "))
    consumo_combustible = float(input("Ingrese el consumo de combustible por kilómetro (en litros/km): "))
    
    tiempo_horas, tiempo_minutos, tiempo_segundos, combustible = calcular_tiempo_y_combustible(distancia, velocidad_promedio, consumo_combustible)
    
    print(f"Tiempo estimado de viaje: {tiempo_horas} horas, {tiempo_minutos} minutos, {tiempo_segundos} segundos.")
    print(f"Combustible necesario: {combustible:.2f} litros.")
else:
    print("No se pudo obtener la información de una o ambas ciudades. Asegúrate de que los nombres estén escritos correctamente.")