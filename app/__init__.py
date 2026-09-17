from flask import Flask

def create_app():
    # 1. Crear la instancia de Flask
    app = Flask(__name__)

    # 2. Importar el blueprint main desde routes.py
    from .routes import main

    # 3. Registrar el blueprint en la aplicación
    app.register_blueprint(main)

    # 4. Retornar la instancia app
    return app

