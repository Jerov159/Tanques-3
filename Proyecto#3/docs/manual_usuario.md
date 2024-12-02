# Manual de Usuario

Este manual proporciona las instrucciones necesarias para instalar, configurar y utilizar el sistema de monitoreo de niveles en tanques.

## Contenido
1. [Requisitos Previos](#requisitos-previos)
2. [Instalación](#instalación)
3. [Uso del Sistema](#uso-del-sistema)
4. [Funciones Principales](#funciones-principales)
5. [Solución de Problemas Comunes](#solución-de-problemas-comunes)

---

## Requisitos Previos

Antes de comenzar, asegúrate de tener lo siguiente:

- Python 3.8 o superior instalado.
- Acceso a un proyecto de Firebase con una base de datos en tiempo real configurada.
- Archivo JSON de credenciales de Firebase descargado.
- Conexión a Internet para interactuar con Firebase y cargar recursos externos.

---

## Instalación

### Paso 1: Clonar el Repositorio
Descarga el código fuente.

### Paso 2: Instalar dependencias 

Ejecuta el siguiente comando para instalar las bibliotecas necesarias:

pip install -r requeriments.txt

### Paso 3: Configurar Firebase

1.Ve a la consola de Firebase y descarga el archivo JSON de credenciales.
2.Coloca el archivo en la carpeta raíz del proyecto.
3.Abre main.py y verifica que la URL de la base de datos sea correcta.

### Paso 4: Ejecutar el proyecto

1.Inicia el servidor con el siguiente comando:
python main.py
2.Accede al sistema visitando http://127.0.0.1:5000 en tu navegador.

---

## Uso del Sistema
### 1. Interfaz Principal
La página principal ofrece:

Un gráfico de barras con los niveles de agua actualizados en tiempo real.
Botones para:
Actualizar datos manualmente.
Exportar datos a CSV.
Campos para filtrar registros por fecha.
Tabla de Historial
La parte inferior de la página web muestra una tabla con:

### 2. IDs de los sensores.
Niveles de agua registrados.
Opciones para ordenar datos por columnas.
Gráficos en Python
Los datos generados por los sensores simulados también se visualizan en tiempo real con gráficos creados mediante matplotlib.

## Funciones Principales
### Simulación de Sensores:
Generación de datos automáticos cada 2 segundos.
Envío de datos al servidor en tiempo real.

### Visualización de Datos:
Gráfico de Barras: Muestra los niveles actuales de los sensores.
Tabla de Historial: Permite revisar registros anteriores.

### Exportación de Datos:

Los datos pueden descargarse como un archivo CSV.
### Filtrado por Fecha:
Consulta datos específicos según un rango de fechas.

---

## Solución de Problemas Comunes

### Error al Conectar con Firebase
Verifica que el archivo JSON de credenciales esté en la ubicación correcta.
Asegúrate de que la URL de la base de datos en main.py sea válida.

### Gráficos o Tabla No Se Actualizan
Confirma que el servidor Flask esté en ejecución.
Actualiza el navegador para recargar la página web.

### Exportación a CSV No Funciona
Asegúrate de que el navegador permita descargas de archivos.
Verifica que existan datos disponibles antes de intentar exportar.
