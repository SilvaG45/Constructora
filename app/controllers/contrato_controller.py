from flask import Blueprint, request, jsonify
from application.services.contrato_service import ContratoService
from domain.entities.contrato import Contrato
from icecream import ic

contrato_blueprint = Blueprint('contrato', __name__)
contrato_service = ContratoService()

@contrato_blueprint.route('/', methods=['POST'])
def registrar_contrato():
    data = request.json
    # buscar el cliente por el id y crear el contrato
    cliente_id = data.get("cliente_id")
    if not cliente_id:
        return jsonify({"error": "El campo 'cliente_id' es requerido"}), 400
    cliente= contrato_service.obtener_cliente(cliente_id)
    # buscar el proyecto por el id y crear el contrato
    proyecto_id = data.get("proyecto_id")
    if not proyecto_id:
        return jsonify({"error": "El campo 'proyecto_id' es requerido"}), 400
    proyecto= contrato_service.obtener_proyecto(proyecto_id)
    # creamos el contrato con los datos recibidos pero no con proyecto_id sino con el objeto proyecto
    contrato = Contrato(
        monto=data.get("monto"),
        condiciones=data.get("condiciones"),
        estado=data.get("estado"),
        cliente=cliente,
        proyecto=proyecto
    )
    print(contrato)
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

@contrato_blueprint.route('/registrar_contrato_info', methods=['POST'])
def registrar_contrato_info():
    data = request.json
    info_contrato = data.get("info_contrato")
    cliente_id = data.get("cliente_id")

    if not info_contrato or not cliente_id:
        return jsonify({"error": "Datos incompletos: se requieren info_contrato y cliente_id"}), 400

    contrato_service.registrar_contrato_info(info_contrato, cliente_id)
    return jsonify({"message": "Contrato registrado con cliente asociado exitosamente"}), 201

@contrato_blueprint.route('/<int:contrato_id>/actualizar_estado', methods=['PATCH'])
def actualizar_estado_contrato(contrato_id):
    data = request.json
    nuevo_estado = data.get("estado")

    if not nuevo_estado:
        return jsonify({"error": "El campo 'estado' es requerido"}), 400

    contrato_service.actualizar_estado_contrato(contrato_id, nuevo_estado)
    return jsonify({"message": f"Estado del contrato {contrato_id} actualizado a '{nuevo_estado}'"}), 200