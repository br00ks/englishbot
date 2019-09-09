# EnglishBot 
<img src="/images/icon_1024x1024.png" width="75">
EnglishBot is a prototypical Android application to practice English with. Its main component is a conversational agent based on Rasa. The focus is on university specific vocabulary.

## Frontend (Android)
Frontend was developed in Android. To install on device, start Android Studio and edit the file `Constants.java`.
To make application work on your phone, the IP-address needs to be set to the IP address of the server (or laptop, if it runs locally). If application runs locally, it is important, that client and server are in the same network, otherwise it won't work. Alternative: use [ngrok](https://ngrok.com/), which exposes your local server. Note: ngrok should be used for testing purposes only!

## Backend (Rasa)
The backend is based on the open source machine learning framework [Rasa](https://rasa.com).

## Error Correction (LanguageTool)
A LanguageTool Server takes care of error correction. It's an open source proof reading tool for English and many other languages and comes with an own local java server. The server can be accessed via HTTP calls and gets back the results als JSON data.

Needs to be downloaded here:
- [LanguageTool Server](http://wiki.languagetool.org/http-server)
- and also n-gram data here: [ngram data](https://languagetool.org/download/ngram-data/)

## Not implemented yet
- MongoDB connection
