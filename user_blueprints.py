from flask import Blueprint, request
import requests
from utils import load_file_config, HEADERS

user_blueprint = Blueprint("user_blueprint", __name__)
data_config = load_file_config()
url_base = data_config.get("url-backend-security") + "/user"


@user_blueprint.route("/user", method=['GET'])
def get_all_user() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@user_blueprint.route("/user/<string:id_>", method=['GET'])
def get_user_by_id(id_: int) -> dict:
    url = url_base + f"/{id_}"
    response = requests.get(url, headers=HEADERS)
    return response.json()

@user_blueprint.route("/user/insert", method=['POST'])
def insert_user() -> dict:
    user = request.get_json()
    url = url_base + f"/insert"
    response = requests.post(url, headers=HEADERS, json=user)
    return response.json()


@user_blueprint.route("/user/update/<string:id_>", method=['PATCH'])
def update_user(id_: int) -> dict:
    user = request.get_json()
    url = url_base + f"/update/{id_}"
    response = requests.patch(url, headers=HEADERS, json=user)
    return response.json()

@user_blueprint.route("/user/delete/<string:id_>", method=['DELETE'])
def delete_user(id_: int) -> dict:
    url = url_base + f"/delete/{id_}"
    response = requests.delete(url, headers=HEADERS)
    return response.json()
