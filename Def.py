from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def obtener_coordenadas(ciudad):
    geolocalizador = Nominatim(user_agent="distancia_entre_ciudades")
    ubicacion = geolocalizador.geocode(ciudad)
    if ubicacion:
        return (ubicacion.latitude, ubicacion.longitude)
    else:
        return None

def calcular_distancia(ciudad_origen, ciudad_destino):
    coordenadas_origen = obtener_coordenadas(ciudad_origen)
    coordenadas_destino = obtener_coordenadas(ciudad_destino)

    if coordenadas_origen and coordenadas_destino:
        distancia = geodesic(coordenadas_origen, coordenadas_destino).kilometers
        return distancia
    else:
        return None

def calcular_tiempo_y_combustible(distancia, velocidad_promedio, consumo_combustible):
    # Calcular el tiempo estimado de viaje en horas
    tiempo_horas = distancia / velocidad_promedio
    
    # Convertir el tiempo estimado a horas, minutos y segundos
    horas = int(tiempo_horas)
    minutos = int((tiempo_horas - horas) * 60)
    segundos = int(((tiempo_horas - horas) * 60 - minutos) * 60)
    
    # Calcular el combustible necesario en litros
    combustible = distancia * consumo_combustible
    
    return horas, minutos, segundos, combustible
