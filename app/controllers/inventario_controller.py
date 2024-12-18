from flask import Blueprint, request, jsonify
from application.services.inventario_service import InventarioService
from domain.entities.material import Material
from infrastructure.repositories.sqlite_inventario_repository import SQLiteInventarioRepository

# Configuración del blueprint
inventario_blueprint = Blueprint('inventario', __name__)
inventario_service = InventarioService(SQLiteInventarioRepository("inventario.db"))

# Endpoint para registrar un material
@inventario_blueprint.route('/materiales', methods=['POST'])
def registrar_material():
    data = request.json
    if not all(key in data for key in ("nombre", "cantidad_disponible", "precio")):
        return jsonify({"error": "Los campos 'nombre', 'cantidad_disponible' y 'precio' son obligatorios"}), 400

    material = Material(
        nombre=data['nombre'],
        cantidad_disponible=data['cantidad_disponible'],
        precio=data['precio']
    )
    try:
        inventario_service.registrar_material(material.nombre, material.cantidad_disponible, material.precio)
        return jsonify({"message": f"Material '{material.nombre}' registrado exitosamente"}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# Endpoint para consultar un material
@inventario_blueprint.route('/materiales/<string:nombre>', methods=['GET'])
def consultar_material(nombre):
    try:
        material = inventario_service.consultar_material(nombre)
        return jsonify(material.__dict__), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

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
    materiales = inventario_service.listar_todos()
    return jsonify([material.__dict__ for material in materiales]), 200