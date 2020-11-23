from flask import Flask
from  in_memory_data import user_stories


app = Flask(__name__)


@app.route('/')
def hello_world():
    return user_stories[0]["title"]


if __name__ == '__main__':
    app.run()
