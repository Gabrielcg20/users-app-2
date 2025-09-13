from flask import Blueprint, request, jsonify
from mock import usuarios

user_modify_bp = Blueprint('user_modify_bp', __name__)

def fn_get_user_data(email):
    for usuario in usuarios:
        if usuario['email'] == email:
            return usuario
    return None

def fn_modify_user_data(res, req):
    res['nombre'] = req['nombre']
    res['edad'] = req['edad']
    return True

@user_modify_bp.route('/modify/<string:email>', methods=['PUT'])
def fn_user_modify(email):
    req = request.json
    res = fn_get_user_data(email)
    validate = fn_modify_user_data(res, req)
    
    if validate:
        return jsonify({
            'data': 'success modify user'
        })
    return jsonify({
        'data': 'modify not success'
    })