#https://api.scryfall.com

import requests
import json

def SFrequest(S):
    sfurl = "https://api.scryfall.com/"
    resp = requests.get(sfurl+S)
    J = json.loads(resp.content.decode('utf-8'))
    if "error" in J:
        raise Exception(f"Error {J['code']} {J['error']}\nRequest: {sfurl+S}")
    return J