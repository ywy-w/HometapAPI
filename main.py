import os

import requests
import uvicorn
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
    # resp = requests.get(url, auth=(api_key, api_secret)).json()
    # print(resp)
    # sewer_type = resp['property/details']['result']['property']['sewer']
    sewer_type = 'Septic'
    return {'septic': True if sewer_type == 'Septic' else False, api_key: api_secret}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
