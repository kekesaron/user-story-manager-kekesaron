from flask import *
from user_story_model import *
from build import *


app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")


@app.route('/story', methods=["GET"])
def story():
    return render_template("form.html")


@app.route('/story', methods=["POST"])
def add_story():
    columns = ['story_title', 'user_story', 'accept_criteria', 'business_value', 'estimation', 'status']
    data = [request.form[element] for element in columns]
    new_story = UserStory(
        story_title=data[0], user_story=data[1], accept_criteria=data[2], business_value=data[
            3], estimation=data[4], status=data[5])
    new_story.save()
    return "Applicant added"

if __name__ == "__main__":
    app.run(debug=True)
