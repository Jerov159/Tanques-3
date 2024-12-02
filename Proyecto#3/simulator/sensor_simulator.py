import random
import time
import requests
import threading
import matplotlib.pyplot as plt
from collections import deque

# Configuración de la API y sensores
API_URL = "http://127.0.0.1:5000/recibir"
ALTURA_TANQUE = 1.5  # Altura del tanque en metros
RADIO_TANQUE = 0.25  # Radio del tanque en metros
VOLUMEN_MAXIMO = 300  # Volumen máximo del tanque en litros
INTERVALO_DATOS = 2  # Intervalo de envío en segundos

# Generar ID de los sensores basados en el nombre y número de identificación
ESTUDIANTE = "Jeronimo"
IDENTIFICACION = "1979"
SENSORES = [f"{ESTUDIANTE[:4].upper()}{IDENTIFICACION}{i+1}" for i in range(7)]  # 7 tanques

# Datos en tiempo real para graficar
datos_nivel = {sensor: deque(maxlen=20) for sensor in SENSORES}
tiempos = deque(maxlen=20)

# Función para convertir nivel medido a volumen
def convertir_a_volumen(distancia):
    # Distancia medida por el sensor (desde el sensor al nivel de agua)
    nivel_agua = max(0, ALTURA_TANQUE - distancia)  # Altura de agua
    volumen = (3.1416 * (RADIO_TANQUE**2) * nivel_agua) * 1000  # En litros
    return min(volumen, VOLUMEN_MAXIMO)

# Función para simular datos de un sensor
def simulate_sensor_data(sensor_id):
    while True:
        distancia = round(random.uniform(0, ALTURA_TANQUE), 2)  # Simular distancia en metros
        volumen = convertir_a_volumen(distancia)
        
        # Construir el payload en el formato esperado por la API
        payload = {
            'idsensor': str(sensor_id),       # Asegurar que el ID sea una cadena
            'nivel': round(volumen, 2)
        }
        try:
            # Enviar datos a la API
            response = requests.post(API_URL, json=payload)
            if response.status_code == 201:
                print(f"{sensor_id} -> Dato enviado: {payload}")
                # Actualizar datos locales para graficar
                if len(tiempos) == 0 or (time.time() - tiempos[-1] > INTERVALO_DATOS):
                    tiempos.append(time.time())
                datos_nivel[sensor_id].append(volumen)
            else:
                print(f"{sensor_id} -> Error al enviar: {response.text}")
        except Exception as e:
            print(f"{sensor_id} -> Error al conectar con la API: {e}")

        time.sleep(INTERVALO_DATOS)

# Función para graficar en tiempo real
def graficar_niveles():
    plt.ion()  # Modo interactivo de matplotlib
    fig, ax = plt.subplots()
    while True:
        ax.clear()
        for sensor_id, valores in datos_nivel.items():
            ax.plot(range(len(valores)), valores, label=f"Tanque {sensor_id}")
        ax.set_title("Nivel de agua en tiempo real")
        ax.set_xlabel("Tiempo")
        ax.set_ylabel("Nivel de agua (litros)")
        ax.set_ylim(0, VOLUMEN_MAXIMO + 10)
        ax.legend()
        plt.pause(0.1)

# Ejecutar simulación de varios sensores y graficar
if __name__ == "__main__":
    # Crear un hilo para cada sensor
    for sensor_id in SENSORES:
        threading.Thread(target=simulate_sensor_data, args=(sensor_id,), daemon=True).start()
    
    # Iniciar la gráfica en tiempo real
    graficar_niveles()