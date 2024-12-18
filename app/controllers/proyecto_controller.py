from flask import Blueprint, request, jsonify
from application.services.proyecto_service import ProyectoService
from domain.entities.proyecto import Proyecto
from icecream import ic

proyecto_blueprint = Blueprint('proyecto', __name__)
proyecto_service = ProyectoService()

@proyecto_blueprint.route('/', methods=['POST'])
def registrar_proyecto():
    data = request.json
    proyecto= Proyecto(**data)
    ic(proyecto.__str__())
    proyecto_service.registrar_proyecto(proyecto)
    return jsonify({"message": "Proyecto registrado exitosamente"}), 201

@proyecto_blueprint.route('/<int:proyecto_id>', methods=['GET'])
def obtener_proyecto(proyecto_id):
    proyecto = proyecto_service.obtener_proyecto(proyecto_id)
    if proyecto:
        return jsonify(proyecto.__dict__), 200
    return jsonify({"error": "Proyecto no encontrado"}), 404

@proyecto_blueprint.route('/', methods=['GET'])
def listar_proyectos():
    proyectos = proyecto_service.listar_todos()
    return jsonify([p.__dict__ for p in proyectos]), 200

@proyecto_blueprint.route('/', methods=['PUT'])
def actualizar_proyecto():
    data = request.json
    proyecto = Proyecto(**data)
    proyecto_service.actualizar_proyecto(proyecto)
    return jsonify({"message": "Proyecto actualizado exitosamente"}), 200

@proyecto_blueprint.route('/<int:proyecto_id>', methods=['DELETE'])
def eliminar_proyecto(proyecto_id):
    proyecto = proyecto_service.obtener_proyecto(proyecto_id)
    ic(proyecto)
    if proyecto:
        proyecto_service.eliminar_proyecto(proyecto_id)
        return jsonify({"message": "Proyecto eliminado exitosamente"}), 200
    return jsonify({"error": "Proyecto no encontrado"}), 404