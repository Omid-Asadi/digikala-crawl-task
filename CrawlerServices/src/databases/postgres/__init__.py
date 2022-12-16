from peewee import *
from datetime import datetime
from configure.settings import DB_PASS, DB_PORT, DB_USER, DB_HOST, DB_NAME


pg_db = PostgresqlDatabase(
    DB_NAME, user=DB_USER, password=DB_PASS,
    host=DB_HOST, port=DB_PORT
)


class BaseModel(Model):
    """ A base model that will use in our other models """
    created_time = DateTimeField(default=datetime.utcnow())
    modified_time = DateTimeField(default=datetime.utcnow())

    class Meta:
        database = pg_db

    def save(self, force_insert=False, only=None):
        self.modified_time = datetime.utcnow()
        return super().save(force_insert, only)
