import requests
from decimal import Decimal

global nowver
nowver = 0.1

def getLV():
    global defver, iniverorigin
    iniverorigin = latest_version[1:]
    iniver = float(latest_version[1:])
    print(iniver)
    if iniver > nowver:
        defver = 1
        return
    elif iniver == nowver:
        defver = 2
        return
    else:
        defver = 3
        return

owner = 'FuariLai'
repo = 'Serenity'
url = f'https://api.github.com/repos/{owner}/{repo}/releases/latest'

response = requests.get(url)
data = response.json()
latest_version = data['tag_name']

print(f'최신 버전: {latest_version}')