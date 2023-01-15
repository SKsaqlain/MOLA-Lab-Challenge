# MOLA-Lab-Challenge
 Chrome Extension for Twitter Sentiment Analysis


### Python-Flask Apis
The apis are located in `MOLA-Lab-Challenge/com/mola/lab/src/main` directory
The flask app contains two endpoints 
1) /api/language-detection [POST api which takes list of texts as request body and returns a list with text and language]
2) /api/sentiment-score

### Python Flask-App setup and run
```
$ cd MOLA-Lab-Challenge/com/mola/lab
$ pipenv shell
$ pipenv install
$ sh bootstrap.sh
```

### Chrome-extension
The chrome extension to extract timeline tweets and annotate with emojis is present `MOLA-Lab-Challenge/com/mola/lab/gextension`.
To setup the project please follow the below link
```
https://developer.chrome.com/docs/extensions/mv3/getstarted/development-basics/#load-unpacked
```
After loading the extension open twitter page and click on the extension few times for it to start up and fetch the results.
