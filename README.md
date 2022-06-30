Hometap Septic API Microservice Readme

This microservice currently utilizes HouseCanary to find if a given address contains a septic system.

Instructions to run:
* retrieve the API key and API secret from an authorized HouseCanary account
* sign in to AWS under the relevant IAM user or use the following instructions: https://docs.aws.amazon.com/apprunner/latest/dg/setting-up.html
* create an apprunner service via the AWS console
* select Source code repository for Repository type
* click Add new, provide oauth access
* create Connection name 'HometapAPI' and click 'Install another'
* give access only to the relevant Github repository 'HometapAPI'
* branch should be set to main
* choose Manual under Deployment trigger and click Next
* choose Python3 for Runtime
* 'pip install -r requirements.txt' for Build command
* 'uvicorn main:app' for Start command
* HometapAPI for Service name
* 1vCPU & 2GB RAM
* enter Environment variables APIKEY : {the API key} & APISECRET : {the API secret} 
* 

NEXT STEPS - Considerations for further development
* HouseCanary address supports unit, state, and city but is not implemented
* FastAPI supports typing via Pydantic but is not implemented
* 