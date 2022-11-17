from flask import Blueprint, request
import requests
from utils import load_file_config, HEADERS

table_blueprint = Blueprint("table_blueprint", __name__)
data_config = load_file_config()
url_base = data_config.get("url-backend-results") + "/table"


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