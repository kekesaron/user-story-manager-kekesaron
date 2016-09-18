from flask import *
from user_story_model import *
from build import *


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
        return redirect("http://127.0.0.1:5000/list")


@app.route('/list', methods=["GET", "POST"])
def list_stories():
    if request.method == 'GET':
        user_stories = UserStory.select()
        return render_template("list.html", user_stories=user_stories)
    else:
        return redirect("http://127.0.0.1:5000/story")


@app.route('/story/<story_id>/delete')
def delete_user_story(story_id):
    UserStory.delete().where(UserStory.id == story_id).execute()
    return redirect("http://127.0.0.1:5000/list")


@app.route('/story', methods=["GET"])
def story():
    title = "- Add new Story"
    return render_template("form.html", title=title)


@app.route('/story', methods=["POST"])
def add_story():
    columns = ['story_title', 'user_story', 'accept_criteria', 'business_value', 'estimation', 'status']
    data = [request.form[element] for element in columns]
    new_story = UserStory(
        story_title=data[0], user_story=data[1], accept_criteria=data[2], business_value=data[
            3], estimation=data[4], status=data[5])
    new_story.save()
    return redirect("http://127.0.0.1:5000/list")


@app.route('/story/<story_id>', methods=["GET", "POST"])
def update_story(story_id):
    user_story = UserStory.select().where(UserStory.id == story_id).first()
    if request.method == 'GET':
        title = "- Edit Story"
        return render_template("form.html", story_id=story_id, user_story=user_story, title=title)
    else:
        columns = ['story_title', 'user_story', 'accept_criteria', 'business_value', 'estimation', 'status']
        data = [request.form[element] for element in columns]
        user_story.story_title = data[0]
        user_story.user_story = data[1]
        user_story.accept_criteria = data[2]
        user_story.business_value = data[3]
        user_story.estimation = data[4]
        user_story.status = data[5]
        user_story.save()
        return redirect("http://127.0.0.1:5000/list")

if __name__ == "__main__":
    app.run(debug=True)
    connect_database()
