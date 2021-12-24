
from flask_jwt_extended import JWTManager
from errors.ErrorHandler import BAD_REQUEST, INVALID_CREDENTIALS, NOT_FOUND,VALIDATION_ERROR
from flask import jsonify, Flask, Blueprint
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
from dotenv import load_dotenv
from modules.index import resources_dict
from swagger.swagger import generated_swagger
import os


# ================ Setup Application ================
api_name = 'user_api'
app = Flask(__name__)
api_user = Blueprint(api_name, __name__)
app.config.from_object('config')
# ======================= Jwt =======================
jwt = JWTManager(app)

load_dotenv('.env', verbose=True)
SERVER_URL = os.getenv('SERVER_URL')
SWAGGER_URL = '/api/docs'
API_URL = '/app/swagger.json'
# ======================== Initializing APP =======================

@api_user.route(API_URL, methods=['GET'])
def swagger_api_docs_yml():
    try:
        generated_swagger['servers'] = [{'url':f'http://{SERVER_URL}:5001/api'}]
        return generated_swagger
    except:
        pass

swaggerui_bluprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL
)

api = Api(app, prefix='/api/')

# ========================= Add Resources =========================
print(resources_dict.keys())
for routs in resources_dict.keys():
    for resource in resources_dict[routs]:
        api.add_resource(resource[0], routs + resource[1])

# ======================= Register Bluprint =======================
app.register_blueprint(api_user)
app.register_blueprint(swaggerui_bluprint)





# ======================= Error Handler =======================
@app.errorhandler(VALIDATION_ERROR)
@app.errorhandler(BAD_REQUEST)
@app.errorhandler(INVALID_CREDENTIALS)
@app.errorhandler(NOT_FOUND)
def handle_exception(err):
    """Return custom JSON when APIError or its children are raised"""
    description = 'Error'
    if hasattr(err,'description'):
       description = err.description
    
    code = 500
    if hasattr(err,'code'):
       code = err.code

    response = {"error": description}
    if len(err.args) > 0:
        response["message"] = err.args[0]
    # Add some logging so that we can monitor different types of errors
    app.logger.error(f'{description}: {response["message"]}')
    return jsonify(response), code


if __name__ == '__main__':
    
    app.run(port=5000, host='0.0.0.0')
