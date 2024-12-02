import subprocess

# Ejecutar el simulador de sensores
simulator_process = subprocess.Popen(["python", "simulator/sensor_simulator.py"])

# Ejecutar la aplicación web
app_process = subprocess.Popen(["python", "web_app/app.py"])

# Mantener ambos procesos activos
try:
    simulator_process.wait()
    app_process.wait()
except KeyboardInterrupt:
    simulator_process.terminate()
    app_process.terminate()
