from flask import Blueprint, request, jsonify
from application.services.proyecto_service import ProyectoService
from domain.entities.proyecto import Proyecto
from icecream import ic

proyecto_blueprint = Blueprint('proyecto', __name__)
proyecto_service = ProyectoService()

'''
Registrar proyecto
'''
@proyecto_blueprint.route('/', methods=['POST'])
def registrar_proyecto():
    data = request.json
    proyecto= Proyecto(**data)
    ic(proyecto.__str__())
    proyecto_service.registrar_proyecto(proyecto)
    return jsonify({"message": "Proyecto registrado exitosamente"}), 201

'''
Obtener proyecto por ID
'''
@proyecto_blueprint.route('/<int:proyecto_id>', methods=['GET'])
def obtener_proyecto(proyecto_id):
    proyecto = proyecto_service.obtener_proyecto(proyecto_id)
    if proyecto:
        return jsonify(proyecto.__dict__), 200
    return jsonify({"error": "Proyecto no encontrado"}), 404

'''
Listar todos los proyectos
'''
@proyecto_blueprint.route('/', methods=['GET'])
def listar_proyectos():
    proyectos = proyecto_service.listar_todos()
    for p in proyectos:
        ic(p.__dict__)
    return jsonify([p.__dict__ for p in proyectos]), 200

'''
Actualizar proyecto
'''
@proyecto_blueprint.route('/', methods=['PUT'])
def actualizar_proyecto():
    data = request.json
    proyecto = Proyecto(**data)
    proyecto_service.actualizar_proyecto(proyecto)
    return jsonify({"message": "Proyecto actualizado exitosamente"}), 200

'''
Eliminar proyecto
'''
@proyecto_blueprint.route('/<int:proyecto_id>', methods=['DELETE'])
def eliminar_proyecto(proyecto_id):
    proyecto = proyecto_service.obtener_proyecto(proyecto_id)
    ic(proyecto)
    if proyecto:
        proyecto_service.eliminar_proyecto(proyecto_id)
        return jsonify({"message": "Proyecto eliminado exitosamente"}), 200
    return jsonify({"error": "Proyecto no encontrado"}), 404

# patch para cambiar fecha de fin del proyecto
@proyecto_blueprint.route('/<int:proyecto_id>/fecha', methods=['PATCH'])
def cambiar_fecha_fin_proyecto(proyecto_id):
    data = request.json
    proyecto = proyecto_service.obtener_proyecto(proyecto_id)
    if proyecto:
        proyecto_service.cambiar_fecha_fin_proyecto(proyecto_id, data)
        return jsonify({"message": "Fecha de fin del proyecto actualizada exitosamente"}), 200
    return jsonify({"error": "Proyecto no encontrado"}), 404

# patch para cambiar presupuesto del proyecto
@proyecto_blueprint.route('/<int:proyecto_id>/presupuesto', methods=['PATCH'])
def cambiar_presupuesto(proyecto_id):
    data = request.json
    proyecto = proyecto_service.obtener_proyecto(proyecto_id)
    if proyecto:
        proyecto_service.cambiar_presupuesto(proyecto_id, data)
        return jsonify({"message": "Presupuesto del proyecto actualizado exitosamente"}), 200
    return jsonify({"error": "Proyecto no encontrado"}), 404

'''
Agregar materiales necesarios a un proyecto
'''
@proyecto_blueprint.route('/materiales', methods=['POST'])
def agregar_materiales():
    data = request.json
    print(data, 'data de agregar materiales')
    proyecto_service.agregar_materiales(data)
    return jsonify({"message": "Materiales agregados exitosamente"}), 201

'''
Verificar disponibilidad de materiales para avanzar proyecto
'''
@proyecto_blueprint.route('/<int:proyecto_id>/verificar_avance', methods=['GET'])
def verificar_avance_proyecto(proyecto_id):
    """Endpoint para verificar si un proyecto puede avanzar."""
    try:
        disponible, material_insuficiente = proyecto_service.verificar_disponibilidad_materiales(proyecto_id)
        if disponible:
            return jsonify({"message": "El proyecto puede avanzar a la siguiente fase"}), 200
        else:
            return jsonify({"error": f"No hay suficiente inventario para el material con ID {material_insuficiente}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


'''
Avanzar proyecto
'''
@proyecto_blueprint.route('/<int:proyecto_id>/avanzar', methods=['GET'])
def avanzar_proyecto(proyecto_id):
    """Endpoint para avanzar un proyecto a la siguiente fase."""
    try:
        proyecto_service.avanzar_proyecto(proyecto_id)
        return jsonify({"message": "El proyecto avanzó a la siguiente fase"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500