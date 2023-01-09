from com.mola.lab.src.main.model.English import EnglishSchema
from flask import Flask, jsonify ,request, Blueprint
import json
from com.mola.lab.src.main.model.Tweet import Tweet, TweetSchema
from com.mola.lab.src.main.model.Sentiment import SentimentSchema

app=Flask(__name__)

sentiment_api = Blueprint('sentiment_api', __name__)


response=[
 {
   "tweet_text": "Stats on Twitter World Cup",
   "sentiment_score": {
     "positive": 0.07268287241458893,
     "neutral": 0.863078773021698,
     "negative": 0.0642382949590683
   },
   "detected_mood": "NEUTRAL"
 }
]

@sentiment_api.route("/api/sentiment-score", methods=['POST'])
def sentiment_score():
    content=request.json
    print(content)
    requestSchema=TweetSchema(many=True)
    responseSchema=SentimentSchema(many=True)
    print(request)
    tweets=requestSchema.dump(content)
    # print(request.get_json())
    return responseSchema.dump(response)

