from geopy.geocoders import Nominatim
from geopy.distance import geodesic

class Viaje:
    def __init__(self, ciudad_origen, ciudad_destino):
        self.ciudad_origen = ciudad_origen
        self.ciudad_destino = ciudad_destino

    def obtener_coordenadas(self, ciudad):
        geolocalizador = Nominatim(user_agent="distancia_entre_ciudades")
        ubicacion = geolocalizador.geocode(ciudad)
        if ubicacion:
            return (ubicacion.latitude, ubicacion.longitude)
        else:
            return None

    def calcular_distancia(self):
        coordenadas_origen = self.obtener_coordenadas(self.ciudad_origen)
        coordenadas_destino = self.obtener_coordenadas(self.ciudad_destino)

        if coordenadas_origen and coordenadas_destino:
            distancia = geodesic(coordenadas_origen, coordenadas_destino).kilometers
            return distancia
        else:
            return None

    def calcular_tiempo_y_combustible(self, velocidad_promedio, consumo_combustible):
        distancia = self.calcular_distancia()
        if distancia:
            tiempo_horas = distancia / velocidad_promedio
            horas = int(tiempo_horas)
            minutos = int((tiempo_horas - horas) * 60)
            segundos = int(((tiempo_horas - horas) * 60 - minutos) * 60)
            combustible = distancia * consumo_combustible
            return horas, minutos, segundos, combustible
        else:
            return None, None, None, None

ciudad_origen = input("Ingrese la ciudad de origen: ")
ciudad_destino = input("Ingrese la ciudad de destino: ")

viaje = Viaje(ciudad_origen, ciudad_destino)

distancia = viaje.calcular_distancia()

if distancia:
    print(f"La distancia entre {ciudad_origen} y {ciudad_destino} es de {distancia:.2f} kilómetros.")

    velocidad_promedio = float(input("Ingrese la velocidad promedio esperada (en km/h): "))
    consumo_combustible = float(input("Ingrese el consumo de combustible por kilómetro (en litros/km): "))

    tiempo_horas, tiempo_minutos, tiempo_segundos, combustible = viaje.calcular_tiempo_y_combustible(velocidad_promedio, consumo_combustible)

    if tiempo_horas is not None:
        print(f"Tiempo estimado de viaje: {tiempo_horas} horas, {tiempo_minutos} minutos, {tiempo_segundos} segundos.")
        print(f"Combustible necesario: {combustible:.2f} litros.")
    else:
        print("No se pudo calcular el tiempo estimado de viaje y el combustible necesario.")
else:
    print("No se pudo obtener la información de una o ambas ciudades. Asegúrate de que los nombres estén escritos correctamente.")
