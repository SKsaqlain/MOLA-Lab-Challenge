from marshmallow import Schema, fields


class Sentiment(object):
    def __init__(self,tweet_text,sentiment_score,detected_mood):
        self.tweet_text=tweet_text
        self.sentiment_score=sentiment_score
        self.detected_mood=detected_mood

class SentimentScoreSchema(Schema):
    positive=fields.Float()
    negative=fields.Float()
    neutral=fields.Float()

class SentimentSchema(Schema):
    tweet_text=fields.Str()
    sentiment_score=fields.Nested(SentimentScoreSchema)
    detected_mood=fields.Str()

