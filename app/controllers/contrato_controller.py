from flask import Blueprint, request, jsonify
from application.services.contrato_service import ContratoService
from domain.entities.contrato import Contrato

contrato_blueprint = Blueprint('contrato', __name__)
contrato_service = ContratoService()

@contrato_blueprint.route('/', methods=['POST'])
def registrar_contrato():
    data = request.json
    contrato = Contrato(**data)
    contrato_service.registrar_contrato(contrato)
    return jsonify({"message": "Contrato registrado exitosamente"}), 201

@contrato_blueprint.route('/<int:contrato_id>', methods=['GET'])
def obtener_contrato(contrato_id):
    contrato = contrato_service.obtener_contrato(contrato_id)
    if contrato:
        return jsonify(contrato.__dict__), 200
    return jsonify({"error": "Contrato no encontrado"}), 404

@contrato_blueprint.route('/', methods=['GET'])
def listar_contratos():
    contratos = contrato_service.listar_todos()
    return jsonify([c.__dict__ for c in contratos]), 200