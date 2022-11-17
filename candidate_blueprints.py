from flask import Blueprint, request
import requests
from utils import load_file_config, HEADERS

candidate_blueprint = Blueprint("candidate_blueprint", __name__)
data_config = load_file_config()
url_base = data_config.get("url-backend-result") + "/candidate"


@candidate_blueprint.route("/candidate", method=['GET'])
def get_all_candidate() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@candidate_blueprint.route("/candidate/<string:id_>", method=['GET'])
def get_candidate_by_id(id_: str) -> dict:
    url = url_base + f"/{id_}"
    response = requests.get(url, headers=HEADERS)
    return response.json()

@candidate_blueprint.route("/candidate/insert", method=['POST'])
def insert_candidate() -> dict:
    candidate = request.get_json()
    url = url_base + f"/insert"
    response = requests.post(url, headers=HEADERS, json=candidate)
    return response.json()

@candidate_blueprint.route("/candidate/update/<string:id_>", method=['PATCH'])
def update_candidate(id_: str) -> dict:
    candidate = request.get_json()
    url = url_base + f"/update/{id_}"
    response = requests.patch(url, headers=HEADERS, json=candidate)
    return response.json()

@candidate_blueprint.route("/candidate/delete/<string:id_>", method=['DELETE'])
def delete_candidate(id_: str) -> dict:
    url = url_base + f"/delete/{id_}"
    response = requests.delete(url, headers=HEADERS)
    return response.json()
