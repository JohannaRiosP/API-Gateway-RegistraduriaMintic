from flask import Blueprint, request
import requests
from utils import load_file_config, HEADERS

political_party_blueprints = Blueprint("political_party_blueprints", __name__)
data_config = load_file_config()
url_base = data_config.get("url-backend-result") + "/political_party"

@political_party_blueprints.route("/political_partys", methods=['GET'])
def get_all_political_party() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@political_party_blueprints.route("/political_party/<string:id_>", methods=['GET'])
def get_political_party_by_id(id_: str) -> dict:
    url = url_base + f"/{id_}"
    response = requests.get(url, headers=HEADERS)
    return response.json()

@political_party_blueprints.route("/political_party/insert", methods=['POST'])
def insert_political_party() -> dict:
    political_party = request.get_json()
    url = url_base + f"/insert"
    response = requests.post(url, headers=HEADERS, json=political_party)
    return response.json()

@political_party_blueprints.route("/political_party/update/<string:id_>", methods=['PATCH'])
def update_political_party(id_: str) -> dict:
    political_party = request.get_json()
    url = url_base + f"/update/{id_}"
    response = requests.patch(url, headers=HEADERS, json=political_party)
    return response.json()

@political_party_blueprints.route("/political_party/delete/<string:id_>", methods=['DELETE'])
def delete_political_party(id_: str) -> dict:
    url = url_base + f"/delete/{id_}"
    response = requests.delete(url, headers=HEADERS)
    return response.json()
