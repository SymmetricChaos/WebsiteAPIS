#https://scryfall.com/docs/api

import requests
import json

def SFrequest(S):
    sfurl = "https://api.scryfall.com/"
    resp = requests.get(sfurl+S)
    J = json.loads(resp.content.decode('utf-8'))
    if "error" in J:
        raise Exception(f"Error {J['code']} {J['error']}\nRequest: {sfurl+S}")
    return J

#a = SFrequest("sets/aer")
#print(a)


a = SFrequest("cards?page=3")
for i in a['data'][0].items():
    print(i)
print()
print(a['data'][0]['layout'])
print(a['data'][0]['object'])
print(a['data'][0]['mana_cost'])
print(a['data'][0]['cmc'])
print(a['data'][0]['reprint'])
print(a['data'][0]['name'])
print(a['data'][0]['set'])