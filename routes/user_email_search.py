import sys
import os
from flask import request
from flask import Blueprint, jsonify
from mock import usuarios

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

user_email_search = Blueprint("user_email_search", __name__)


def _search_product_by_email(email):
    for product in usuarios:
        if product['email'] == str(email):
           return product
    return None    


@user_email_search.route("/", methods = ["GET"])
def search_by_email():
    if request.method == "GET":

        req_email = request.args.get("email", type=str)
        email = _search_product_by_email(req_email)

        return jsonify({
            "data: ": email
        })
