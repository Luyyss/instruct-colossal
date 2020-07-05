import os
from flask import Flask
from config import Config, DevelopmentConfig

config = Config()
# print(os.environ['APP_SETTINGS'])

app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_object(DevelopmentConfig())

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()