import os
import requests
import uvicorn
from fastapi import FastAPI, HTTPException

api_key = os.getenv('APIKEY')
api_secret = os.getenv('APISECRET')
app = FastAPI()

# TODO finish error handling and logging and testing
@app.get("/septic-check")
async def has_septic(address: str = '', zipcode: str = ''):
    base = 'https://api.housecanary.com/v2'
    # base = 'https://0b0d0ef1-409e-4164-aeda-70556b4f33f8.mock.pstmn.io'
    # base = 'https://doesntexistoijolkj.net'
    url = base + f'/property/details?address={address}&zipcode={zipcode}'
    try:
        resp = requests.get(url, auth=(api_key, api_secret), timeout=5)
        resp.raise_for_status()
        sewer_type = resp.json()['property/details']['result']['property']['sewer']
        return {'septic': True if sewer_type == 'Septic' else False}
    # failing quietly monitor logs for problems, could add error responses to return
    except requests.Timeout as e:
        raise HTTPException(status_code=504, detail=e)
    except Exception as e:
        print(resp, e) if 'resp' in locals() else print(e)
    return {'septic': False}


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
