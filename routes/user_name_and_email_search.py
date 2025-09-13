from flask import Blueprint, request, jsonify
from mock import usuarios

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/user/', methods=['GET'])
def search_users():
    name_param = request.args.get('name')
    email_param = request.args.get('email')
    
    if name_param is None and email_param is None:
        return jsonify({"error": "Se requiere 'name' o 'email'"}), 400
    
    results = []
    
    for user in usuarios:
        nombre_match = True
        email_match = True
        
        if name_param is not None:
            nombre_match = name_param.lower() in user["nombre"].lower()
        
        if email_param is not None:
            email_match = email_param.lower() in user["email"].lower()
        
        if nombre_match and email_match:
            results.append({
                "nombre": user["nombre"],
                "email": user["email"]
            })
    
    return jsonify({"data": results})