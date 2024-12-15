import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from app.controllers.personal_controller import personal_blueprint
from app.controllers.subcontratista_controller import subcontratista_blueprint
from app.controllers.proyecto_controller import proyecto_blueprint

app = Flask(__name__)
app.register_blueprint(personal_blueprint, url_prefix="/api/personal")
app.register_blueprint(subcontratista_blueprint, url_prefix="/api/subcontratista")
app.register_blueprint(proyecto_blueprint, url_prefix="/api/proyecto")

if __name__ == "__main__":
    app.run(debug=True)
