from flask import Blueprint, request
import requests
from utils import load_file_config, HEADERS

rol_blueprint = Blueprint("rol_blueprint", __name__)
data_config = load_file_config()
url_base = data_config.get("url-backend-result") + "/rol"


@rol_blueprint.route("/rols", method=['GET'])
def get_all_roles() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@rol_blueprint.route("/rol/<string:id_>", method=['GET'])
def get_rol_by_id(id_: int) -> dict:
    url = url_base + f"/{id_}"
    response = requests.get(url, headers=HEADERS)
    return response.json()

@rol_blueprint.route("/rol/insert", method=['POST'])
def insert_rol() -> dict:
    rol = request.get_json()
    url = url_base + f"/insert"
    response = requests.post(url, headers=HEADERS, json=rol)
    return response.json()

@rol_blueprint.route("/rol/update/<string:id_>", method=['PATCH'])
def update_rol(id_: int) -> dict:
    rol = request.get_json()
    url = url_base + f"/update/{id_}"
    response = requests.patch(url, headers=HEADERS, json=rol)
    return response.json()

@rol_blueprint.route("/rol/delete/<string:id_>", method=['DELETE'])
def delete_rol(id_: int) -> dict:
    url = url_base + f"/delete/{id_}"
    response = requests.delete(url, headers=HEADERS)
    return response.json()
