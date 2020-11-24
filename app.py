from flask import Flask, render_template, request, redirect, url_for
import user_story

app = Flask(__name__)


@app.route('/')
def index():
    headers = user_story.user_story_headers
    user_stories = user_story.test_user_stories
    display_format_function = user_story.get_display_value

    return render_template("index.html", headers=headers, user_stories=user_stories,
                           format_function=display_format_function)


@app.route('/add', methods=["GET"])
def add_user_story_get():
    return render_template("user_story_form.html", user_story_to_edit=None)


@app.route('/add', methods=["POST"])
def add_user_story_post():
    form_data = dict(request.form)

    new_id = user_story.get_new_id()
    form_data["Id"] = new_id
    form_data["Status"] = "Planning"

    user_story.test_user_stories.append(form_data)

    return redirect(url_for("index"))


@app.route('/edit/<user_story_id>', methods=["GET"])
def edit_user_story_get(user_story_id):
    user_story_id = int(user_story_id)
    user_story_to_edit = user_story.get_user_story_by_id(user_story_id)

    if user_story_to_edit is None:
        return redirect(url_for("index"))

    return render_template("user_story_form.html", user_story_to_edit=user_story_to_edit)


@app.route('/edit/<user_story_id>', methods=["POST"])
def edit_user_story_post(user_story_id):
    user_story_id = int(user_story_id)
    form_data = dict(request.form)
    form_data["Id"] = user_story_id

    user_story.update_user_story(form_data)

    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run()
