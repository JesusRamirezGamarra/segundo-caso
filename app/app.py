import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # Muestra el ID del contenedor para verificar el balanceo de carga
    container_id = os.uname()[1]
    #return f"Hello, World! from container {container_id}"
    return f"Hello world: Ramirez Gamarra Lucio Jesus! from container {container_id}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080) 