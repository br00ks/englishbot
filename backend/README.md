# EnglishBot Backend
This is the backend for the EnglishBot application.

## Requirements
- pip3 (tested with 9.0)
- Python3 (tested with 3.6.8)

## Install
Install the required packages:

`pip install -r requirements.txt`

## Start the services
The EnglishBot app needs four services that need to be started:
1. Webserver (will run on on port 5005)
`make webserver`

2. Action Server (will run on on port 5055)
`make action-server`

3. NLU Server (will run on on port 5045)
`make nlu-server`

4. LanguageTool Server (see repository ..., will run on on port 8082)
`make java-server`

## Retrain models
You can retrain the models as follows:

`rasa train`

You can also use the flag `--debug` to see the output.
