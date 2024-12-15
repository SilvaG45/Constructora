from flask import Blueprint, request, jsonify
from application.services.cliente_service import ClienteService
from domain.entities.cliente import Cliente

cliente_blueprint = Blueprint('cliente', __name__)
cliente_service = ClienteService()

@cliente_blueprint.route('/', methods=['POST'])
def registrar_cliente():
    data = request.json
    cliente = Cliente(**data)
    cliente_service.registrar_cliente(cliente)
    return jsonify({"message": "Cliente registrado exitosamente"}), 201

@cliente_blueprint.route('/<int:cliente_id>', methods=['GET'])
def obtener_cliente(cliente_id):
    cliente = cliente_service.obtener_cliente(cliente_id)
    if cliente:
        return jsonify(cliente.__dict__), 200
    return jsonify({"error": "Cliente no encontrado"}), 404

@cliente_blueprint.route('/', methods=['GET'])
def listar_clientes():
    clientes = cliente_service.listar_todos()
    return jsonify([c.__dict__ for c in clientes]), 200