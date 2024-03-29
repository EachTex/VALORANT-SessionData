import requests
import base64
import os

lockfile = f"{os.environ.get('LOCALAPPDATA')}\\Riot Games\\Riot Client\\Config\\lockfile"
with open(lockfile, "r") as f:
    data = f.read()

d = {}
d['name'], d['pid'], d['port'], d['password'], d['protocol'] = data.split(":")

print(d['port'])

password = d['password']
print(base64.b64encode(f'riot:{password}'.encode()).decode())

def getSession(port, password):
    lnk = f'https://127.0.0.1:{port}/chat/v1/session'
    header = {
        "Authorization": f"Basic {base64.b64encode(f'riot:{password}'.encode()).decode()}"
    }
    req = requests.get(lnk, headers = header, verify = False)
    print(req.json())

def getHelp(port, password):
    lnk = f'https://127.0.0.1:{port}/help'
    header = {
        "Authorization": f"Basic {base64.b64encode(f'riot:{password}'.encode()).decode()}"
    }
    req = requests.get(lnk, headers = header, verify = False)
    print(req.json())

getSession(port = d['port'], password = d['password'])
getHelp(port = d['port'], password = d['password'])
