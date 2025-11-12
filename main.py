# Proyecto: Simulación de Telemetría IoT
# Autor: Fátima Graciela Chiñas Martínez
# Descripción:
# Este programa simula la lectura de datos de sensores (temperatura y humedad)
# y su transmisión a la nube en formato JSON, representando un ejemplo sencillo
# de un sistema IoT o de telemetría.

import random
import time
import json

def leer_sensores():
    temperatura = round(random.uniform(20, 35), 2)
    humedad = round(random.uniform(40, 80), 2)
    return {"temperatura": temperatura, "humedad": humedad}

def enviar_datos(datos):
    print("Enviando datos a la nube:", json.dumps(datos))
    print("-" * 40)

print("🌐 Iniciando simulación de telemetría IoT...\n")

for i in range(5):
    lectura = leer_sensores()
    enviar_datos(lectura)
    time.sleep(2)

print("✅ Simulación finalizada.")
