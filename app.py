from flask import Flask, render_template
from in_memory_data import user_stories

app = Flask(__name__)


@app.route('/')
def index():
    table_headers = ["Id", "Story Title", "User Story", "Acceptance criteria", "Business Value", "Estimation", "Status"]
    user_story_keys = ["id", "title", "story", "criteria", "business", "estimation", "status"]
    return render_template("index.html", table_headers=table_headers, user_stories=user_stories,
                           user_story_keys=user_story_keys)


if __name__ == '__main__':
    app.run()
