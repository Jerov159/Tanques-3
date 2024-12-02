from flask import Flask, request, jsonify, render_template
from firebase_admin import credentials, initialize_app, db
import re

# Inicialización de Flask
app = Flask(__name__)

# Inicialización de Firebase
cred = credentials.Certificate("web_app/sensor-nivel-agua-firebase-adminsdk-pilli-e47e18e343.json")
initialize_app(cred, {'databaseURL': 'https://sensor-nivel-agua-default-rtdb.firebaseio.com'})

# Referencia a la base de datos (Nodo)
firebase_ref = db.reference('sensor-nivel-agua')

# Validación del formato del idsensor
sensor_pattern = re.compile(r'^JERO1979[1-7]$')  # Valida idsensor para los sensores del 1 al 7

@app.route('/recibir', methods=['POST'])
def recibir_datos():
    try:
        # Log para confirmar la entrada a la función
        print("Solicitud POST recibida en /recibir")

        # Obtener datos del cuerpo de la solicitud
        data = request.json
        print(f"Datos recibidos: {data}")

        # Validación de datos
        if 'idsensor' not in data or 'nivel' not in data:
            print("Error: Faltan campos obligatorios (idsensor, nivel)")
            return jsonify({'error': 'Faltan campos obligatorios (idsensor, nivel)'}), 400

        # Validar formato de idsensor
        if not sensor_pattern.match(data['idsensor']):
            print(f"Error: Formato inválido para idsensor: {data['idsensor']}")
            return jsonify({'error': 'Formato de idsensor inválido (debe ser JERO19791 a JERO19797)'}), 400

        # Obtener fecha y hora actuales
        from datetime import datetime
        now = datetime.now()
        fecha = now.strftime('%Y-%m-%d')
        hora = now.strftime('%H:%M:%S')
        print(f"Fecha: {fecha}, Hora: {hora}")

        # Construir registro
        registro = {
            'fecha': fecha,
            'hora': hora,
            'idsensor': data['idsensor'],
            'nivel': data['nivel']
        }
        print(f"Registro construido: {registro}")

        # Guardar datos en Firebase
        nuevo_registro = firebase_ref.push(registro)

        # Confirmación de éxito
        print("Datos guardados exitosamente en Firebase")
        return jsonify({'message': 'Datos guardados exitosamente', 'id': nuevo_registro.key}), 201

    except Exception as e:
        # Log de error para identificar problemas
        print(f"Error interno: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/ver_datos', methods=['GET'])
def ver_datos():
    try:
        # Recuperar todos los datos de Firebase
        datos = firebase_ref.get()

        if not datos:
            return jsonify({'message': 'No hay datos disponibles'}), 200

        # Convertir los datos a una lista para enviarlos al navegador
        datos_list = [{'id': key, **value} for key, value in datos.items()]

        return jsonify(datos_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Ruta para la página web principal
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)