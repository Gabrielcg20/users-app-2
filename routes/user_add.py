import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import Blueprint, jsonify, request
from mock import usuarios


user_add = Blueprint('user_add', __name__)

@user_add.route('/add', methods=['POST'])
def fn_add_new_user():
    if request.method == 'POST':
        req = request.json

        new_user = _model_user_swap(req) 
  
        usuarios.append(new_user)
    
        return jsonify({
            "data":new_user
        })   
    



def _model_user_swap(req):
    return  {
        "nombre": req['nombre'],
        "edad": req['edad'],
        "email": req['email']
    }
