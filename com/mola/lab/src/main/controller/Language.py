from com.mola.lab.src.main.model.English import EnglishSchema
from flask import Flask, jsonify ,request, Blueprint
import json
from com.mola.lab.src.main.model.Tweet import Tweet, TweetSchema
from com.mola.lab.src.main.model.English import English,EnglishSchema

app=Flask(__name__)

langiage_api = Blueprint('langiage_api', __name__)


response=[{
    "tweet_text":"sdfsdfsd",
    "is_english": False
}]

@langiage_api.route("/api/language-detection", methods=['POST'])
def language_detection():
    content=request.json
    print(content)
    requestSchema=TweetSchema(many=True)
    responseSchema=EnglishSchema(many=True)
    print(request)
    tweets=requestSchema.dump(content)
    # print(request.get_json())
    return responseSchema.dump(response)

