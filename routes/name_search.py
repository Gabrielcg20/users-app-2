import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from mock import usuarios
from flask import Blueprint, jsonify, request


name_search = Blueprint('name_search', __name__)

def _search_name(nombre):
    for usuario in usuarios:
        if usuario['nombre'] == nombre:
            return usuario

        

@name_search.route('/user', methods=['GET'])
def fn_search_name():
    req = request.args.get('usuario', type=str)
    res = _search_name(req)
    return jsonify(res)
        
