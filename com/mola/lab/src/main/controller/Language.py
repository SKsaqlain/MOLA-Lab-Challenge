from numpy import isneginf
from com.mola.lab.src.main.model.English import EnglishSchema
from flask import Flask, jsonify ,request, Blueprint
import json
from com.mola.lab.src.main.model.Tweet import Tweet, TweetSchema
from com.mola.lab.src.main.model.English import English,EnglishSchema

from com.mola.lab.src.main.service.LanguageDetect import LanguageDetect

app=Flask(__name__)
languageDetection=LanguageDetect()

langiage_api = Blueprint('langiage_api', __name__)




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

@langiage_api.route("/api/language-detection", methods=['POST'])
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

