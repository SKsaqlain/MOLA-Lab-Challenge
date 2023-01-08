from flask import Flask
from com.mola.lab.src.main.controller.Language import langiage_api
from com.mola.lab.src.main.controller.Sentiment import sentiment_api

app=Flask(__name__)
app.register_blueprint(langiage_api)
app.register_blueprint(sentiment_api)


@app.route("/")
def hello_work():
    return "hellow,world"

app.run()
