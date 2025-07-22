import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from datetime import datetime

ubicacion = ['Lima Centro', 'Lima Norte', 'Lima Este', 'Lima Sur', 'Lima Oeste']

# Datos generados aleatoriamente para simular niveles de contaminación en diferentes sectores de Lima
data = {
    'Zona': ubicacion,
    'PM2.5': np.random.uniform(30, 120, len(ubicacion)),  # Material particulado
    'CO2': np.random.uniform(350, 500, len(ubicacion)),  # Dióxido de carbono
    'NO2': np.random.uniform(20, 50, len(ubicacion)),  # Dióxido de nitrógeno
    'O3': np.random.uniform(50, 150, len(ubicacion)),  # Ozono
    'SO2': np.random.uniform(5, 15, len(ubicacion)),  # Dióxido de azufre
}

df = pd.DataFrame(data)

# Valores simulados de los umbrales de contaminación para cada parámetro según las recomendaciones de la OMS
th = {
    'PM2.5': 35,
    'CO2': 400,
    'NO2': 40,
    'O3': 100,
    'SO2': 10,
}

# Función para verificar si los niveles de contaminación exceden los umbrales
def verificar_calidad_aire(row, th): #th = thresholds
    alert = []
    for column in ['PM2.5', 'CO2', 'NO2', 'O3', 'SO2']:
        if row[column] > th[column]:
            alert.append(f"Alerta: {column} excede el umbral recomendado.")
    return alert if alert else ["Calidad del aire dentro de los límites"]


# Aplicar la función para verificar la calidad del aire
df['Calidad del aire'] = df.apply(lambda row: verificar_calidad_aire(row, th), axis=1)


# Generador de reporte gráfico
plt.figure(figsize=(10, 6))
sb.barplot(x='Zona', y='CO2', data=df, color='lightgreen', label='CO2')
sb.barplot(x='Zona', y='O3', data=df, color='orange', label='O3')
sb.barplot(x='Zona', y='NO2', data=df, color='purple', label='NO2')
sb.barplot(x='Zona', y='PM2.5', data=df, color='skyblue', label='PM2.5')
sb.barplot(x='Zona', y='SO2', data=df, color='lightcoral', label='SO2')


plt.title("Simulación de Niveles de Contaminación en Diferentes Sectores de Lima")
plt.ylabel("Concentración (µg/m³, ppm, ppb)")
plt.xlabel("Ubicación en Lima")
plt.legend(title="Contaminantes")
plt.show()


#Ruta para guardar el archivo en un directorio específico, el cual será creado si no existe
folder_path = './src'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

#Fecha y hora actual para nombrar el archivo
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Nombre formateado del archivo
file_name = f'calidad_aire_lima_{current_time}.csv'

# Ruta del archivo
file_path = os.path.join(folder_path, file_name)

df.to_csv(file_path, index=False)
print(f"Reporte guardado en: {file_path}")

# Mostrar la tabla con alertas
df[['Zona', 'PM2.5', 'CO2', 'NO2', 'O3', 'SO2', 'Calidad del aire']]