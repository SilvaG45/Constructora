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

@pedido_blueprint.route('/<int:pedido_id>/materiales', methods=['POST'])
def agregar_material_a_pedido(pedido_id):
    data = request.json
    material_id = data.get("material_id")
    cantidad = data.get("cantidad")
    if not material_id or not cantidad:
        return jsonify({"error": "Los campos 'material_id' y 'cantidad' son obligatorios"}), 400

    pedido = pedido_service.agregar_material_a_pedido(pedido_id, material_id, cantidad)
    if pedido:
        return jsonify({"message": f"Material {material_id} agregado al pedido {pedido_id} exitosamente"}), 200
    return jsonify({"error": "Pedido no encontrado"}), 404

@pedido_blueprint.route('/<int:pedido_id>/materiales', methods=['GET'])
def consultar_materiales(pedido_id):
    materiales = pedido_service.consultar_materiales(pedido_id)
    if materiales is not None:
        return jsonify({"materiales": materiales}), 200
    return jsonify({"error": "Pedido no encontrado"}), 404