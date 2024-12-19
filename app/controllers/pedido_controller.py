from flask import Blueprint, request, jsonify
from application.services.pedido_service import PedidoService
from domain.entities.pedido import Pedido

pedido_blueprint = Blueprint('pedido', __name__)
pedido_service = PedidoService()

@pedido_blueprint.route('/', methods=['POST'])
def registrar_pedido():
    data = request.json
    pedido = Pedido(**data)
    pedido_service.registrar_pedido(pedido)
    return jsonify({"message": "Pedido registrado exitosamente"}), 201

@pedido_blueprint.route('/<int:pedido_id>', methods=['GET'])
def obtener_pedido(pedido_id):
    pedido = pedido_service.obtener_pedido(pedido_id)
    if pedido:
        return jsonify(pedido.__dict__), 200
    return jsonify({"error": "Pedido no encontrado"}), 404

@pedido_blueprint.route('/', methods=['GET'])
def listar_pedidos():
    pedidos = pedido_service.listar_todos()
    return jsonify([p.__dict__ for p in pedidos]), 200

@pedido_blueprint.route('/materiales', methods=['POST'])
def agregar_material_a_pedido():
    data = request.json
    pedido_service.agregar_material_a_pedido(data)
    return jsonify({"message": "Material agregado exitosamente"}), 201
   

@pedido_blueprint.route('/<int:pedido_id>/materiales', methods=['GET'])
def consultar_materiales(pedido_id):
    materiales = pedido_service.consultar_materiales(pedido_id)
    if materiales is not None:
        return jsonify({"materiales": materiales}), 200
    return jsonify({"error": "Pedido no encontrado"}), 404