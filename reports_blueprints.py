from flask import Blueprint
import requests
from utils import load_file_config, HEADERS

reports_blueprints = Blueprint("reports_blueprints", __name__)
data_config = load_file_config()
url_base = data_config.get("url-backend-result") + "/reports"


@reports_blueprints.route("/reports/table_votes/all", methods=['GET'])
def report_tables_enrollments() -> dict:
    url = f'{url_base}/table_votes/all'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/table_votes/<string:id_>", methods=['GET'])
def report_tables_votes_by_id(id_: str) -> dict:
    url = f'{url_base}/table_votes/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/candidate_votes/all", methods=['GET'])
def report_candidate_votes() -> dict:
    url = f'{url_base}/candidate_votes/all'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/candidate_votes/<string:id_>", methods=['GET'])
def report_candidate_votes_by_id(id_: str) -> dict:
    url = f'{url_base}/candidate_votes/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/tables_top_votes", methods=['GET'])
def report_tables_top_votes() -> dict:
    url = f'{url_base}/tables_top_votes'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/politic_party_votes", methods=['GET'])
def report_politic_party_votes() -> dict:
    url = f'{url_base}/politic_party_votes'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/politic_party_distribution", methods=['GET'])
def report_politic_party_distribution() -> dict:
    url = f'{url_base}/politic_party_distribution'
    response = requests.get(url, headers=HEADERS)
    return {"message": "done"}, response.status_code
