from flask import Blueprint, request, jsonify
from application.services.subcontratista_service import SubcontratistaService
from domain.entities.subcontratista import Subcontratista
from icecream import ic

subcontratista_blueprint = Blueprint('subcontratista', __name__)
subcontratista_service = SubcontratistaService()

@subcontratista_blueprint.route('/', methods=['POST'])
def registrar_subcontratista():
    data = request.json
    subcontratista = Subcontratista(**data)
    ic(subcontratista)
    subcontratista_service.registrar_subcontratista(subcontratista)
    return jsonify({"message": "Subcontratista registrado exitosamente"}), 201

@subcontratista_blueprint.route('/<int:subcontratista_id>', methods=['GET'])
def obtener_subcontratista(subcontratista_id):
    subcontratista = subcontratista_service.obtener_subcontratista(subcontratista_id)
    if subcontratista:
        return jsonify(subcontratista.__dict__), 200
    return jsonify({"error": "Subcontratista no encontrado"}), 404

@subcontratista_blueprint.route('/', methods=['GET'])
def listar_subcontratistas():
    subcontratistas = subcontratista_service.listar_todos()
    return jsonify([s.__dict__ for s in subcontratistas]), 200

# Endpoint para liberar un subcontratista de un proyecto
@subcontratista_blueprint.route('/<int:subcontratista_id>/proyectos', methods=['DELETE'])
def liberar_proyecto(subcontratista_id):
    data = request.json
    proyecto_id = data.get("proyecto_id")
    if not proyecto_id:
        return jsonify({"error": "El campo 'proyecto_id' es obligatorio"}), 400

    subcontratista = subcontratista_service.liberar_de_proyecto(subcontratista_id, proyecto_id)
    if subcontratista:
        return jsonify({"message": f"Proyecto {proyecto_id} eliminado de subcontratista {subcontratista_id} exitosamente"}), 200
    return jsonify({"error": "Subcontratista no encontrado o no asignado a este proyecto"}), 404

# Endpoint para obtener proyectos asignados a un subcontratista
@subcontratista_blueprint.route('/<int:subcontratista_id>/proyectos', methods=['GET'])
def obtener_proyectos_asignados(subcontratista_id):
    proyectos = subcontratista_service.obtener_proyectos_asignados(subcontratista_id)
    if proyectos is not None:
        return jsonify({"proyectos": proyectos}), 200
    return jsonify({"error": "Subcontratista no encontrado"}), 404

@subcontratista_blueprint.route('/proyectos', methods=['POST'])
def asignar_proyecto():
    data = request.json
    subcontratista_service.asignar_a_proyecto(data)
    return jsonify({"message": "Proyecto asignado exitosamente"}), 201