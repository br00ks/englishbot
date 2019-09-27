# EnglishBot Backend
This is the backend for the EnglishBot application.

## Requirements
- pip 9.0
- Python 3.6.8

## Install
First you need to clone this repository and install the required packages:

`pip install -r requirements.txt`

After installing the requirements, you need to train the models as follows:

`rasa train`

You can also use the flag `--debug` to see the output.

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
