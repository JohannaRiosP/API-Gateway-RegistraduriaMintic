import requests

security_backend = "http://127.0.0.1:8080"
headers = {"Content-Type": "application/json; charset=utf-8"}

#Create roles

roles = [
    {"name": "Administrador", "description": "El que gestiona"},
    {"name": "Administrador-Jurado", "description": "El que gestiona los votos"},
]
