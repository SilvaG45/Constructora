from flask import Blueprint, request, jsonify
from application.services.subcontratista_service import SubcontratistaService
from domain.entities.subcontratista import Subcontratista

subcontratista_blueprint = Blueprint('subcontratista', __name__)
subcontratista_service = SubcontratistaService()

@subcontratista_blueprint.route('/', methods=['POST'])
def registrar_subcontratista():
    data = request.json
    subcontratista = Subcontratista(**data)
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