from flask import Flask

app = Flask(__name__)

# Esta ruta solo se registrará una vez por ejecución
@app.route('/api/hello')
def hello():
    return "Hola mundo desde Flask 2.2.5"

if __name__ == '__main__':
    # Usar el puerto 5000 que Codespaces mapea automáticamente
    app.run(host='0.0.0.0', port=5000)