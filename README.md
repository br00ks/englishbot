# EnglishBot 
<img src="/images/icon_1024x1024.png" width="75">
EnglishBot is a Android application prototype to practice English with. Its main component is a conversational agent based on Rasa. The focus is on university specific vocabulary.

## How to use
To try the application, download this repository. The following picture shows the architecture of the application.

<p align="center">
  <img src="/images/architecture_en.png" width="425">
</p>

The next steps are to install the android application and start the Rasa NLU, Rasa Core, Action and LanguageTool Server.

## Frontend - Android
Frontend was developed in Android. To install on device, start Android Studio and edit the file `Constants.java`.
To make application work on your phone, the IP-address needs to be set to the IP address of the server (or laptop, if it runs locally). If application runs locally, it is important, that client and server are in the same network, otherwise it won't work. Alternative: use [ngrok](https://ngrok.com/), which exposes your local server. Note: ngrok should be used for testing purposes only!

## Backend - Rasa Stack
The backend is based on the open source machine learning framework [Rasa](https://rasa.com).
More information to start backend [here](https://github.com/br00ks/englishbot/tree/master/backend)

## Error Correction - LanguageTool
A LanguageTool Server takes care of error correction. It's an open source proof reading tool for English and many other languages and comes with an own local java server. The server can be accessed via HTTP calls and gets back the results als JSON data.

The size of LanguageTool server is too big to upload on Github. To use the application, the server needs to be downloaded aswell as the n-gram data set, which makes it possible to detect errors with words that are often confused.
- [LanguageTool Server](http://wiki.languagetool.org/http-server)
- optional download n-gram data set: [ngram data](https://languagetool.org/download/ngram-data/) (about 8 gb)

The server should run on port 8082 and can be started like this:
`java -cp languagetool-server.jar org.languagetool.server.HTTPServer --port 8082 --public --languageModel [/path/to/ngrams-dataset]`

## Not implemented yet
- MongoDB connection
