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

# Endpoint para asignar un proyecto a un personal
@personal_blueprint.route('/proyectos', methods=['POST'])
def asignar_proyecto():
    data = request.json
    personal_service.asignar_a_proyecto(data)
    return jsonify({"message": "Proyecto asignado exitosamente"}), 201

# Endpoint para obtener proyectos asignados a un personal
@personal_blueprint.route('/<int:personal_id>/proyectos', methods=['GET'])
def obtener_proyectos_asignados(personal_id):
    proyectos = personal_service.obtener_proyectos_asignados(personal_id)
    if proyectos is not None:
        return jsonify({"proyectos": proyectos}), 200
    return jsonify({"error": "Personal no encontrado"}), 404

@personal_blueprint.route('/<int:personal_id>/horas', methods=['GET'])
def obtener_horas_trabajadas(personal_id):
    horas = personal_service.obtener_horas_trabajadas(personal_id)
    # cambiar en el atributo de la entidad personal
    personal= personal_service.obtener_personal(personal_id)
    personal.setHorasTrabajadas(horas)
    return jsonify({"horas_trabajadas": horas}), 200


