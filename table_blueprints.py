from flask import Blueprint, request
import requests
from utils import load_file_config, HEADERS

table_blueprint = Blueprint("table_blueprint", __name__)
data_config = load_file_config()
url_base = data_config.get("url-backend-result") + "/table"

@table_blueprint.route("/table", method=['GET'])
def get_all_table() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@table_blueprint.route("/table/<string:id_>", method=['GET'])
def get_table_by_id(id_: str) -> dict:
    url = url_base + f"/{id_}"
    response = requests.get(url, headers=HEADERS)
    return response.json()

@table_blueprint.route("/table/insert", method=['POST'])
def insert_table() -> dict:
    table = request.get_json()
    url = url_base + f"/insert"
    response = requests.post(url, headers=HEADERS, json=table)
    return response.json()

@table_blueprint.route("/table/update/<string:id_>", method=['PATCH'])
def update_table(id_: str) -> dict:
    table = request.get_json()
    url = url_base + f"/update/{id_}"
    response = requests.patch(url, headers=HEADERS, json=table)
    return response.json()

@table_blueprint.route("/table/delete/<string:id_>", method=['DELETE'])
def delete_table(id_: str) -> dict:
    url = url_base + f"/delete/{id_}"
    response = requests.delete(url, headers=HEADERS)
    return response.json()
