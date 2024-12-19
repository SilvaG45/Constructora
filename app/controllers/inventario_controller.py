from flask import Blueprint, request, jsonify
from application.services.inventario_service import InventarioService
from domain.entities.material import Material

# Configuración del blueprint
inventario_blueprint = Blueprint('inventario', __name__)
inventario_service = InventarioService()

@inventario_blueprint.route('/', methods=['POST'])
def registrar_inventario():
    inventario_service.agregar_inventario()
    return jsonify({"message": "Inventario registrado exitosamente"}), 201

@inventario_blueprint.route('/<int:inventario_id>', methods=['GET'])
def obtener_inventario(inventario_id):
    inventario = inventario_service.obtener_inventario(inventario_id)
    if inventario:
        return jsonify(inventario.__dict__), 200
    return jsonify({"error": "Inventario no encontrado"}), 404

@inventario_blueprint.route('/', methods=['GET'])
def obtener_inventarios():
    inventarios = inventario_service.listar_inventarios()
    return jsonify([i.__dict__ for i in inventarios
    ]), 200

# Endpoint para registrar un material
@inventario_blueprint.route('/materiales', methods=['POST'])
def registrar_material():
    data= request.json
    print(data, 'data de registrar material')
    inventario_service.registrar_material(data)
    return jsonify({"message": "Material registrado exitosamente"}), 201
    
@inventario_blueprint.route('/materiales/<string:nombre>/cantidad', methods=['GET'])
def consultar_cantidad(nombre):
    try:
        material = inventario_service.consultar_cantidad(nombre)
        cantidad= material['cantidad']
        return jsonify({"message": f"La cantidad de {nombre} en inventario es {cantidad}"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    
# Endpoint para actualizar la cantidad de un material
@inventario_blueprint.route('/materiales/<string:nombre>/cantidad', methods=['PATCH'])
def actualizar_inventario(nombre):
    data = request.json
    cantidad = data.get("cantidad")
    if cantidad is None:
        return jsonify({"error": "El campo 'cantidad' es obligatorio"}), 400
    try:
        inventario_service.actualizar_inventario(nombre, cantidad)
        return jsonify({"message": f"Inventario de {nombre} actualizado exitosamente"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@inventario_blueprint.route('/materiales/<string:nombre>/precio', methods=['PATCH'])
def actualizar_precio(nombre):
    data = request.json
    precio = data.get("precio")
    if precio is None:
        return jsonify({"error": "El campo 'precio' es obligatorio"}), 400
    try:
        inventario_service.actualizar_precio(nombre, precio)
        return jsonify({"message": f"Precio de {nombre} actualizado exitosamente"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

# Endpoint para listar todos los materiales
@inventario_blueprint.route('/materiales', methods=['GET'])
def listar_materiales():
    materiales = inventario_service.listar_materiales()
    print(materiales, 'materiales')
   # retornar los materiales que es un diccionario
    return jsonify([m for m in materiales]), 200