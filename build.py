from user_story_model import *


def connect_database():
    db.connect()
    db.drop_tables([UserStory], safe=True)
    db.create_tables([UserStory], safe=True)
