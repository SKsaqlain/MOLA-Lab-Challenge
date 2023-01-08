from marshmallow import Schema, fields


class Sentiment(object):
    def __init__(self,tweet_text,sentiment_score,detected_mode):
        self.tweet_text=tweet_text
        self.sentiment_score=sentiment_score
        self.detected_mode=detected_mode

class SentimentScoreSchema(Schema):
    positive=fields.Float()
    negative=fields.Float()
    neutra=fields.Float()

class SentimentSchema(Schema):
    tweet_text=fields.Str()
    sentiment_score=fields.Nested(SentimentScoreSchema)
    detected_mode=fields.Str()

