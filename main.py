import json
import requests
import os
import time

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

while action != 0:
    os.system('clear')
    print("Pilih Menu:")
    print("1. Network Devices List")
    print("2. Host List")
    print("3. Network Issue")
    print("4. Network Health")
    print("0. Quit")
    action = int(input("Masukan Nomor Menu: "))
    if action == 0:
        break
    elif action == 1:
        os.system('clear')
        url = "http://localhost:58000/api/v1/network-device"

        respon = requests.get(url, headers=headers, verify=False)

        print("Network Devices List ")

        respon_json = respon.json()
        networkDevices = respon_json["response"]

        print("Hostname\tType\tIP")
        for networkDevice in networkDevices:
            print(networkDevice["hostname"], "\t", networkDevice["platformId"], "\t", networkDevice["managementIpAddress"])
        d = input("\npress Enter to Back")
        continue
    elif action == 2:
        os.system('clear')
        url = "http://localhost:58000/api/v1/host"

        respon = requests.get(url, headers=headers, verify=False)

        print("Host List ")

        respon_json = respon.json()
        hosts = respon_json["response"]

        print("Hostname\tIP\tMac Address\tConnected Interface")
        for host in hosts:
            print(host["hostName"], "\t", host["hostIp"], "\t", host["hostMac"], "\t", host["connectedInterfaceName"])
        d = input("\npress Enter to Back")
        continue
    elif action == 3:
        os.system('clear')
        url = "http://localhost:58000/api/v1/assurance/health-issues"

        respon = requests.get(url, headers=headers, verify=False)

        print("Health Issues")

        respon_json = respon.json()
        issues = respon_json["response"]

        print("Source\tIssue\tDescription\tTime")
        for issue in issues:
            print(issue["issueSource"], "\t", issue["issueName"], "\t", issue["issueDescription"], "\t", issue["issueTimestamp"])
        d = input("\npress Enter to Back")
        continue
    elif action == 4:
        os.system('clear')
        url = "http://localhost:58000/api/v1/network-health"

        respon = requests.get(url, headers=headers, verify=False)

        print("Network Health")

        health = respon.json()

        print(health)
        print("Clients Health: ",health["healthyClient"],"%")
        print("Network Devices Health: ",health["healthyNetworkDevice"],"%")
        print("Num Routers: ",health["numLicensedRouters"])
        print("Num Switches: ",health["numLicensedSwitches"])
        print("Num Unreachable: ",health["numUnreachable"])

        d = input("\npress Enter to Back")
        continue

headers = {
    "X-Auth-Token": serviceTicket
}

logout_url = "http://localhost:58000/api/v1/ticket/"+serviceTicket
req = requests.delete(logout_url, headers=headers, verify=False)
print(req.status_code)
print("Program Dihentikan")