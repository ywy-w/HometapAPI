Hometap Septic API Microservice Readme

This microservice currently utilizes HouseCanary to find if a given address contains a septic system.

Instructions to run:
* retrieve the API key and API secret from an authorized HouseCanary account
* sign in to AWS under the relevant IAM user or use the following instructions: https://docs.aws.amazon.com/apprunner/latest/dg/setting-up.html
* create an apprunner service via the AWS console
* select 'Source code repository' for Repository type
* click 'Add new', provide Github oauth access
* create Connection name 'Hometap' and click 'Install another'
* give access only to the relevant Github repository 'HometapAPI'
* branch should be set to main
* choose 'Manual' under Deployment trigger and click 'Next'
* choose 'Python3' for Runtime
* 'pip install -r requirements.txt' for Build command
* 'python main.py' for Start command
* 'HometapAPI' for Service name
* enter Environment variables APIKEY : {the API key} & APISECRET : {the API secret} 
* leave all other options as they are and click 'Next'
* click 'Create & deploy'
* spinup takes up to 7 minutes
* copy Default domain link and integrate with Hometap Web app as necessary

Next Steps - Considerations for further development:
* API could be refactored to return multiple details from the details response object if they became relevant
* HouseCanary address supports unit, state, and city but is not implemented
* Address could be further validated/sanitized
* FastAPI supports typing via Pydantic but possibly not useful until complexity increases
* No authentication, with AWS url 3rd parties could make paid queries, could implement OAuth or simple header validation
* Selecting for automatic deployment enables a basic CI/CD pipeline on push to Github
* Scalability can be adjusted via apprunner
* If the same address might be queried alot, establish a database or cache to avoid paying for multiple API calls
* 