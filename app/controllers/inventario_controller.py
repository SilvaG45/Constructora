from flask import Blueprint, request, jsonify
from application.services.inventario_service import InventarioService
from domain.entities.material import Material

# Configuración del blueprint
inventario_blueprint = Blueprint('inventario', __name__)
inventario_service = InventarioService()

# Endpoint para registrar un material
@inventario_blueprint.route('/materiales', methods=['POST'])
def registrar_material():
   pass

# Endpoint para verificar el inventario de un material
@inventario_blueprint.route('/materiales/<string:nombre>/verificar', methods=['POST'])
def verificar_inventario(nombre):
    data = request.json
    cantidad = data.get("cantidad")
    if cantidad is None:
        return jsonify({"error": "El campo 'cantidad' es obligatorio"}), 400

    try:
        suficiente = inventario_service.verificar_inventario(nombre, cantidad)
        if suficiente:
            return jsonify({"message": f"Hay suficiente inventario de '{nombre}'"}), 200
        return jsonify({"message": f"No hay suficiente inventario de '{nombre}'"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

# Endpoint para actualizar la cantidad de un material
@inventario_blueprint.route('/materiales/<string:nombre>', methods=['PATCH'])
def actualizar_inventario(nombre):
    data = request.json
    cantidad = data.get("cantidad")
    if cantidad is None:
        return jsonify({"error": "El campo 'cantidad' es obligatorio"}), 400

    try:
        inventario_service.actualizar_inventario(nombre, cantidad)
        return jsonify({"message": f"Inventario de '{nombre}' actualizado exitosamente"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

# Endpoint para listar todos los materiales
@inventario_blueprint.route('/materiales', methods=['GET'])
def listar_materiales():
    materiales = inventario_service.listar_materiales()
    return jsonify([material.__dict__ for material in materiales]), 200