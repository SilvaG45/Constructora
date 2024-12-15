from flask import Blueprint, request, jsonify
from application.services.personal_service import PersonalService
from domain.entities.personal import Personal

personal_blueprint = Blueprint('personal', __name__)
personal_service = PersonalService()

@personal_blueprint.route('/', methods=['POST'])
def registrar_personal():
    data = request.json
    personal = Personal(**data)
    personal_service.registrar_personal(personal)
    return jsonify({"message": "Personal registrado exitosamente"}), 201

@personal_blueprint.route('/<int:personal_id>', methods=['GET'])
def obtener_personal(personal_id):
    personal = personal_service.obtener_personal(personal_id)
    if personal:
        return jsonify(personal.__dict__), 200
    return jsonify({"error": "Personal no encontrado"}), 404

@personal_blueprint.route('/', methods=['GET'])
def listar_personal():
    personal = personal_service.listar_todos()
    return jsonify([p.__dict__ for p in personal]), 200
