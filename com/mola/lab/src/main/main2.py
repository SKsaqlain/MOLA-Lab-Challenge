from flask import Flask, jsonify ,request, Blueprint
from flask_cors import CORS, cross_origin
from faulthandler import is_enabled
from marshmallow import Schema, fields
import os

class English(object):
    def __init__(self,tweet_text,is_english):
        self.tweet_text=tweet_text
        self.is_english=is_english

class EnglishSchema(Schema):
    tweet_text=fields.Str()
    is_english=fields.Bool()


class Sentiment(object):
    def __init__(self,tweet_text,sentiment_score,detected_mood):
        self.tweet_text=tweet_text
        self.sentiment_score=sentiment_score
        self.detected_mood=detected_mood

class Tweet(object):
    def __init__(self,tweet_text):
        self.tweet_text=tweet_text

class TweetSchema(Schema):
    tweet_text=fields.Str()

class SentimentScoreSchema(Schema):
    positive=fields.Float()
    negative=fields.Float()
    neutral=fields.Float()

class SentimentSchema(Schema):
    tweet_text=fields.Str()
    sentiment_score=fields.Nested(SentimentScoreSchema)
    detected_mood=fields.Str()


from langdetect import detect


class LanguageDetect:
    def __init__(self):
        pass

    def isEnglish(self,text):
        result=detect(text)
        if(result=='en'):
            return True
        else:
            return False


from re import M
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer



# response=[
#  {
#    "tweet_text": "Stats on Twitter World Cup",
#    "sentiment_score": {
#      "positive": 0.07268287241458893,
#      "neutral": 0.863078773021698,
#      "negative": 0.0642382949590683
#    },
#    "detected_mood": "NEUTRAL"
#  }
# ]

class SentimentAnalysis():
    def __init__(self):
        pass
    
    def analyze(self,text):
        sidObj=SentimentIntensityAnalyzer()
        sentimentDict=sidObj.polarity_scores(text)
        sentimentResponse={
            "tweet_text":text,
            "sentiment_score":{
                "positive":sentimentDict['pos'],
                "neutral":sentimentDict['neu'],
                "negative":sentimentDict['neg']
            },
            "detected_mood":""

        }
        if(sentimentDict['compound']>=0.05):
            sentimentResponse["detected_mood"]="POSITIVE"
        elif(sentimentDict['compound']<=-0.05):
            sentimentResponse["detected_mood"]="NEGATIVE"
        else:
            sentimentResponse["detected_mood"]="NEUTRAL"
        return sentimentResponse



app=Flask(__name__)

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

languageDetection=LanguageDetect()
def create_response(tweets):
    responseList=list()
    for tweet in tweets:
        isEnglish=languageDetection.isEnglish(tweet['tweet_text'])
        responseList.append(
            {
                "tweet_text":tweet['tweet_text'],
                "is_english": isEnglish  
            }
        )
    return responseList


# request=[{
#  "tweet_text":"hi how are you"   
# }]


# response=[{
#     "tweet_text":"sdfsdfsd",
#     "is_english": False
# }]

@app.route("/api/language-detection", methods=['POST'])
def language_detection():
    content=request.json
    print(content)
    requestSchema=TweetSchema(many=True)
    responseSchema=EnglishSchema(many=True)
    tweets=requestSchema.dump(content)
    print(tweets)
    print(type(tweets))
    responseList=create_response(tweets)
    return responseSchema.dump(responseList)



sentimentAnalyser=SentimentAnalysis()

# response=[
#  {
#    "tweet_text": "Stats on Twitter World Cup",
#    "sentiment_score": {
#      "positive": 0.07268287241458893,
#      "neutral": 0.863078773021698,
#      "negative": 0.0642382949590683
#    },
#    "detected_mood": "NEUTRAL"
#  }
# ]

def get_sentiment_for_all_tweet(tweets):
    scores=list()
    for tweet in tweets:
        score=sentimentAnalyser.analyze(tweet['tweet_text'])
        scores.append(score)
    return scores

@app.route("/api/sentiment-score", methods=['POST'])
def sentiment_score():
    content=request.json
    print(content)
    requestSchema=TweetSchema(many=True)
    responseSchema=SentimentSchema(many=True)
    print(request)
    tweets=requestSchema.dump(content)
    scores=get_sentiment_for_all_tweet(tweets)
    return responseSchema.dump(scores)




@app.route("/")
def hello_work():
    return "hellow,world"

app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
