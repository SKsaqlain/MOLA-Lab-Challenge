from faulthandler import is_enabled
from marshmallow import Schema, fields

class English(object):
    def __init__(self,tweet_text,is_english):
        self.tweet_text=tweet_text
        self.is_english=is_english

class EnglishSchema(Schema):
    tweet_text=fields.Str()
    is_english=fields.Bool()
