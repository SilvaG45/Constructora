import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from app.controllers.personal_controller import personal_blueprint
from app.controllers.subcontratista_controller import subcontratista_blueprint
from app.controllers.proyecto_controller import proyecto_blueprint
from app.controllers.cliente_controller import cliente_blueprint
from app.controllers.proveedor_controller import proveedor_blueprint
from app.controllers.pedido_controller import pedido_blueprint
from app.controllers.material_controller import material_blueprint
from app.controllers.contrato_controller import contrato_blueprint

app = Flask(__name__)
app.register_blueprint(personal_blueprint, url_prefix="/api/personal")
app.register_blueprint(subcontratista_blueprint, url_prefix="/api/subcontratista")
app.register_blueprint(proyecto_blueprint, url_prefix="/api/proyecto")
app.register_blueprint(cliente_blueprint, url_prefix="/api/cliente")
app.register_blueprint(proveedor_blueprint, url_prefix="/api/proveedor")
app.register_blueprint(pedido_blueprint, url_prefix="/api/pedido")
app.register_blueprint(material_blueprint, url_prefix="/api/material")
app.register_blueprint(contrato_blueprint, url_prefix="/api/contrato")



if __name__ == "__main__":
    app.run(debug=True)
