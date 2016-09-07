from peewee import *
db = PostgresqlDatabase("user_story")


class BaseModel(Model):

    class Meta():
        database = db


class UserStory(BaseModel):
    story_title = CharField()
    user_story = CharField()
    accept_criteria = CharField()
    business_value = IntegerField()
    estimation = FloatField()
    status = CharField()
