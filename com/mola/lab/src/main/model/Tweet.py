from marshmallow import Schema, fields

class Tweet(object):
    def __init__(self,tweet_text):
        self.tweet_text=tweet_text

class TweetSchema(Schema):
    tweet_text=fields.Str()