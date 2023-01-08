from flask import Flask
from com.mola.lab.src.main.controller.Language import langiage_api

app=Flask(__name__)
app.register_blueprint(langiage_api)


@app.route("/")
def hello_work():
    return "hellow,world"


app.run()

# def main():
#     print("hello work")


# if "__main__"==__name__:
#     main()