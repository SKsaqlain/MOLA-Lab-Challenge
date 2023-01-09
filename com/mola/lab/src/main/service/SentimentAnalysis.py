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