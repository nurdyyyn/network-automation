import json
import requests

ticket_url = "http://localhost:58000/api/v1/ticket"

print("Network Programibility: SMKN 13 Bandung")
username = input("Username: ")
password = input("Password: ")

headers = {
    "content-type": "application/json"
}

body_json = {
    "username": username,
    "password": password  
}

print(username, password)