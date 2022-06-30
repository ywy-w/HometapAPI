import os

import requests
from fastapi import FastAPI
from pprint import pprint
from mock_response import prop_details

api_key = os.getenv('APIKEY')
api_secret = os.getenv('APISECRET')
app = FastAPI()


@app.get("/septic-check")
async def has_septic(address: str = '', zipcode: str = ''):
    base = 'https://api.housecanary.com/v2'
    url = base + f'/property/details?address={address}&zipcode={zipcode}'
    resp = requests.get(url, auth=(api_key, api_secret)).json()
    sewer_type = resp['property/details']['result']['property']['sewer']
    return {'septic': True if sewer_type == 'Septic' else False}
