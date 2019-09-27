# EnglishBot 
<img src="/images/icon_1024x1024.png" width="75">
EnglishBot is a Android application prototype to practice English with. Its main component is a conversational agent based on Rasa. The focus is on university specific vocabulary.

## How to use
To try the application, download this repository. The following picture shows the architecture of the application.

<p align="center">
  <img src="/images/architecture_en.png" width="425">
</p>
The android client communicates with the backend via websockets. The backend is based on the open source machine learning framework [Rasa](https://rasa.com).

The next steps are to install the android application and start the Rasa NLU, Rasa Core, Action and LanguageTool Server.

## Requirements
- pip3 (tested with 9.0)
- Python3 (tested with 3.6.8)

## Install requirements
Install the required packages:

`pip install -r requirements.txt`

## Install Android application
Frontend was developed in Android. To install on device, start Android Studio and edit the file `Constants.java`.
To make application work on your phone, the IP-address needs to be set to the IP address of the server (or laptop, if it runs locally). If application runs locally, it is important, that client and server are in the same network, otherwise it won't work. Alternative: use [ngrok](https://ngrok.com/), which exposes your local server. Note: ngrok should be used for testing purposes only!

## Download LanguageTool Server
A LanguageTool Server takes care of error correction. It's an open source proof reading tool for English and many other languages and comes with an own local java server. The server can be accessed via HTTP calls and gets back the results als JSON data.

The size of LanguageTool server is too big to upload on Github. To use the application, the server needs to be downloaded aswell as the n-gram data set, which makes it possible to detect errors with words that are often confused.
- [LanguageTool Server](http://wiki.languagetool.org/http-server)
- N-Gram data set: [ngram data](https://languagetool.org/download/ngram-data/) (about 8 gb)

## Start the services
The EnglishBot app needs four services that need to be started:
1. Webserver (will run on on port 5005) - in folder backend
`make webserver`

2. Backend: Action Server (will run on on port 5055) - in folder backend
`make action-server`

3. NLU Server (will run on on port 5045) - in folder backend
`make nlu-server`

4. LanguageTool Server - in folder languagetool
`make java-server`

## Not implemented yet
- MongoDB connection
