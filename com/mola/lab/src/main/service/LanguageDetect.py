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

