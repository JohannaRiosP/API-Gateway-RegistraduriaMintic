from datetime import timedelta
import requests
from flask import Flask, request
from flask_cors import CORS
from flask_jwt_extended import (verify_jwt_in_request, get_jwt_identity, JWTManager, create_access_token)
from waitress import serve
import utils
import requests
from table_blueprints import table_blueprint
from candidate_blueprints import candidate_blueprint
from political_party_blueprints import political_party_blueprint
from vote_blueprints import vote_blueprint
from user_blueprints import user_blueprint
from rol_blueprints import rol_blueprint


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "misiontic"
cors = CORS(app)
jwt = JWTManager(app)

app.register_blueprint(table_blueprint)
app.register_blueprint(vote_blueprint)
app.register_blueprint(political_party_blueprint)
app.register_blueprint(candidate_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(rol_blueprint)


@app.before_request
def before_request_callback():
    endpoint = utils.clean_url(request.path)
    exclude_routes = ['/login', '/']
    if endpoint in exclude_routes:
        pass
    elif verify_jwt_in_request():
        user = get_jwt_identity()
        if user.get('rol'):
            has_grant = utils.validate_grant(endpoint, request.method, user['rol'].get('idRol'))
            if not has_grant:
                return{"message": "Permission denied by grant"}, 401
        else:
            return{"message": "Permission denied by rol"}, 401
    else:
        return{"message": "Permission denied"}, 401


@app.route("/", methods=['GET'])
def home():
    response = {"message": "Welcome to the academic API Gateway..."}
    return response


@app.route("/login", methods=['POST'])
def login() -> tuple:
    user = request.get_json()
    url = data_config.get("url-backend-security") + "/user/login"
    response = requests.post(url, headers=utils.HEADERS, json=user)
    if response.status_code == 200:
        user_logged = response.json()
        del user_logged['rol']['permission']
        expires = timedelta(days=1)
        access_token = create_access_token(identity=user_logged, expires_delta=expires)
        return {"token": access_token, "user_id": user_logged.get('id')}, 200
    else:
        return {"message": "Access denied"}, 401


#Config and execute app
if __name__ == "__main__":
    data_config = utils.load_file_config()
    print("API Gateway Server Running: http://" + data_config.get("url-api-gateway") + ":" + str(data_config.get("port")))
    serve(app, host=data_config.get("url-api-gateway"), port=data_config.get("port"))
