from flask import Flask, jsonify
from flask_cors import CORS
from routes.user_list import user_list
from routes.user_email_search import user_email_search
from routes.user_name_and_email_search import user_bp
from routes.user_delete import user_delete
from routes.user_add import user_add
from routes.name_search import name_search
import sentry_sdk
sentry_sdk.init(
    dsn="https://7a8bbeae55317898c6380efa13aa114b@o4510009648545792.ingest.us.sentry.io/4510009693437952",
    # Add data like request headers and IP for users, if applicable;
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)

app = Flask(__name__)
CORS(app)

app.register_blueprint(user_email_search, url_prefix ='/user')
app.register_blueprint(user_list, url_prefix='/users')
app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(user_delete, url_prefix='/delete')
app.register_blueprint(user_add, url_prefix='/user') 
app.register_blueprint(name_search, url_prefix='/search')


@app.route('/')
def index():
    return jsonify ({"data":"user-app"})


@app.errorhandler(404)
def handle_404(e):
    response = {
    "error": "Not Found",
    "message": "La ruta solicitada no existe",
    "status": 404
    }
    sentry_sdk.capture_message('La ruta solicitada no existe - 404 Error')
    return jsonify(response), 404


def handle_500(e):
    response = {
    "error": "Internal Server Error",
    }

    sentry_sdk.capture_message('Internal Server Error 500')
    return jsonify(response), 500

 

app.register_error_handler(500, handle_500)

if __name__ == "__main__":
    app.run(debug=True)
