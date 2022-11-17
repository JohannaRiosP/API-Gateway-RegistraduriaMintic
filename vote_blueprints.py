from flask import Blueprint, request
import requests
from utils import load_file_config, HEADERS

vote_blueprint = Blueprint("vote_blueprint", __name__)
data_config = load_file_config()
url_base = data_config.get("url-backend-result") + "/vote"


@vote_blueprint.route("/vote", method=['GET'])
def get_all_vote() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@vote_blueprint.route("/vote/<string:id_>", method=['GET'])
def get_vote_by_id(id_: str) -> dict:
    url = url_base + f"/{id_}"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@vote_blueprint.route("/vote/insert", method=['POST'])
def insert_vote() -> dict:
    vote = request.get_json()
    url = url_base + f"/insert"
    response = requests.post(url, headers=HEADERS, json=vote)
    return response.json()


@vote_blueprint.route("/vote/update/<string:id_>", method=['PATCH'])
def update_vote(id_: str) -> dict:
    vote = request.get_json()
    url = url_base + f"/update/{id_}"
    response = requests.patch(url, headers=HEADERS, json=vote)
    return response.json()


@vote_blueprint.route("/vote/delete/<string:id_>", method=['DELETE'])
def delete_vote(id_: str) -> dict:
    url = url_base + f"/delete/{id_}"
    response = requests.delete(url, headers=HEADERS)
    return response.json()
