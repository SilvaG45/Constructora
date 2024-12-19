from flask import Blueprint, request, jsonify
from application.services.proveedor_service import ProveedorService
from domain.entities.proveedor import Proveedor

proveedor_blueprint = Blueprint('proveedor', __name__)
proveedor_service = ProveedorService()

@proveedor_blueprint.route('/', methods=['POST'])
def registrar_proveedor():
    data = request.json
    proveedor = Proveedor(**data)
    print(proveedor, 'proveedor')
    proveedor_service.registrar_proveedor(proveedor)
    return jsonify({"message": "Proveedor registrado exitosamente"}), 201

@proveedor_blueprint.route('/<int:proveedor_id>', methods=['GET'])
def obtener_proveedor(proveedor_id):
    proveedor = proveedor_service.obtener_proveedor(proveedor_id)
    if proveedor:
        return jsonify(proveedor.__dict__), 200
    return jsonify({"error": "Proveedor no encontrado"}), 404

@proveedor_blueprint.route('/', methods=['GET'])
def listar_proveedores():
    proveedores = proveedor_service.listar_todos()
    return jsonify([p.__dict__ for p in proveedores]), 200

@proveedor_blueprint.route('/<int:proveedor_id>/pedidos', methods=['GET'])
def obtener_historial_pedidos(proveedor_id):
    pedidos = proveedor_service.obtener_historial_pedidos(proveedor_id)
    if pedidos is not None:
        return jsonify({"pedidos": [p.__dict__ for p in pedidos]}), 200
    return jsonify({"error": "Proveedor no encontrado"}), 404