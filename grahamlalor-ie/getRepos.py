import requests, json, urllib, random
import getpass
from urllib.parse import urljoin
import sys
from pathlib import Path
from ast import literal_eval
GITHUB_API = 'https://api.github.com'

# User Input
#
username = "websiteProject@yopmail.com" #input('Github username: ')
password = "Fluffycheese2\"" #getpass.getpass('Github password: ')
note = "admin script"+ str(random.randint(1,101)) #input('Note (optional): ')
#
# Compose Request
#
tokenFile = Path("response.json")
if tokenFile.is_file() is False:
    url = urljoin(GITHUB_API, 'authorizations')
    payload = {}
    if note:
        payload['note'] = note
    res = requests.post(
        url,
        auth = (username, password),
        data = json.dumps(payload),
        )
    #
    # Parse Response
    #
    j = json.loads(res.text)
    with open('response.json','w') as i:
        json.dump(j, i)
    token = j['token']
    #print('New token: %s' % token)

with open('response.json','r') as auth:
    data = json.load(auth)
    token = data["token"]
#print(token)

headerData = {
        'Authorization': 'token %s' % token
        }
# check diff in repos and save if changed
try:
    with open('repos.json','r') as i:
        r = requests.get(url="Https://api.github.com/users/GLalor/repos", headers= headerData)
        if json.loads(i.read()) == r.json():
            print("No difference in the files")
        else:
            print("There is a difference in the files")
            data = r.json()
            with open('repos.json','w') as i:
                json.dump(r.json(), i)
except FileNotFoundError:
    r = requests.get(url="Https://api.github.com/users/GLalor/repos", headers= headerData)
    data = r.json()
    with open('repos.json','w') as i:
        json.dump(r.json(), i)