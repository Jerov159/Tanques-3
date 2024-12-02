# Sistema de Monitoreo de Niveles en Tanques

Este proyecto implementa un sistema para monitorear y visualizar en tiempo real los niveles de agua en tanques mediante simulación de sensores, almacenamiento en Firebase y una interfaz web interactiva.

## Características

- **Simulación de Sensores**: Siete sensores virtuales que generan datos de niveles de agua y los envían al servidor.
- **Base de Datos en Tiempo Real**: Almacenamiento de los datos en Firebase para acceso en tiempo real.
- **Visualización Interactiva**: Gráficos de barras dinámicos y tablas con opciones de filtrado y exportación.
- **Gráficos en Python**: Uso de `matplotlib` para graficar los datos simulados.
- **Exportación de Datos**: Descarga de registros en formato CSV.

## Tecnologías Utilizadas

- **Backend**: Python, Flask, Firebase Admin SDK.
- **Frontend**: HTML, Bootstrap, Chart.js.
- **Simulación y Gráficos**: Python (`matplotlib`, `requests`).
- **Base de Datos**: Firebase Real-Time Database.

## Requisitos

Asegúrate de tener instalado:

- Python 3.8 o superior.
- Firebase configurado con credenciales administrativas.
- Las dependencias especificadas en `requirements.txt`.

## Instalación

1. Instala los requisitos mencionados en el "requeriments.txt".
2. Ejecuta run_all.py.
3. Abre el dominio "http://127.0.0.1:5000".