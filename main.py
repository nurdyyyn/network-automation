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

respon = requests.post(ticket_url, json.dumps(body_json), headers=headers, verify=False)
respon_json = respon.json()
if respon.status_code > 201 :
    print("Login Fail/Error,",respon_json["response"]["message"])
    exit()

print("Login Success")
serviceTicket = respon_json["response"]["serviceTicket"]
action = 99

headers={"X-Auth-Token": serviceTicket}