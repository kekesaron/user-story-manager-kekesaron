from user_story_model import *

db.connect()
db.drop_tables([UserStory], safe=True)
db.create_tables([UserStory], safe=True)
