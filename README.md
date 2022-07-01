Hometap Septic API Microservice Readme

This microservice currently utilizes HouseCanary to find if a given address contains a septic system.

Instructions to run:
* Retrieve the API key and API secret from an authorized HouseCanary account
* Sign in to AWS under the relevant IAM user or use the following instructions: https://docs.aws.amazon.com/apprunner/latest/dg/setting-up.html
* Create an apprunner service via the AWS console
* Select 'Source code repository' for Repository type
* Click 'Add new', provide Github OAuth access
* Create Connection name 'Hometap' and click 'Install another'
* Give access only to the relevant Github repository 'HometapAPI'
* Branch should be set to main
* Choose 'Manual' under Deployment trigger and click 'Next'
* Choose 'Python3' for Runtime
* 'pip install -r requirements.txt' for Build command
* 'python main.py' for Start command then click 'Next'
* 'HometapAPI' for Service name
* Enter Environment variables APIKEY : {the API key} & APISECRET : {the API secret} 
* Leave all other options as they are and click 'Next'
* Click 'Create & deploy'
* Spinup takes up to 7 minutes
* Copy Default domain link and integrate with Hometap Web app as necessary

Next Steps - Considerations for further development:
* API could be refactored to return multiple details from the details response object if they became relevant
* HouseCanary address supports unit, state, and city but is not implemented
* Address could be further validated/sanitized
* FastAPI supports typing via Pydantic but possibly not useful until complexity increases
* No authentication, with AWS url 3rd parties could make paid queries, could implement OAuth, header validation, or domain restriction
* Selecting for automatic deployment enables a basic CI/CD pipeline on push to Github
* Scalability can be adjusted via apprunner
* If the same address might be queried alot, establish a database or cache to avoid paying for multiple API calls 
* Current error handling fails quietly to log only. Could include error resp in return body to handle in Web App