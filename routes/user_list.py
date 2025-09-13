import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from mock import usuarios
from flask import Blueprint, jsonify


user_list = Blueprint('user_list', __name__)

@user_list.route('/list', methods=["GET"])
def fn_users_list():
    return jsonify({
        "data":usuarios
    })