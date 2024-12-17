from flask import Blueprint, request, jsonify
from application.services.material_service import MaterialService
from domain.entities.material import Material

material_blueprint = Blueprint('material', __name__)
material_service = MaterialService()

@material_blueprint.route('/', methods=['POST'])
def registrar_material():
    data = request.json
    material = Material(**data)
    material_service.registrar_material(material)
    return jsonify({"message": "Material registrado exitosamente"}), 201

@material_blueprint.route('/<int:material_id>', methods=['GET'])
def obtener_material(material_id):
    material = material_service.obtener_material(material_id)
    if material:
        return jsonify(material.__dict__), 200
    return jsonify({"error": "Material no encontrado"}), 404

@material_blueprint.route('/', methods=['GET'])
def listar_materiales():
    materiales = material_service.listar_todos()
    return jsonify([m.__dict__ for m in materiales]), 200

@material_blueprint.route('/<int:material_id>/precio', methods=['PUT'])
def actualizar_precio(material_id):
    data = request.json
    nuevo_precio = data.get("precio")
    if nuevo_precio is None:
        return jsonify({"error": "El campo 'precio' es obligatorio"}), 400

    material = material_service.actualizar_precio(material_id, nuevo_precio)
    if material:
        return jsonify({"message": f"Precio actualizado a {nuevo_precio}"}), 200
    return jsonify({"error": "Material no encontrado"}), 404