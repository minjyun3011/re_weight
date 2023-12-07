import os 
import datetime
import logging
from playhouse.db_url import connect
from dotenv import load_dotenv
from peewee import Model, IntegerField, CharField, FloatField, TimestampField

load_dotenv()

# logger = logging.getLogger("peewee")
# logger.addHandler(logging.StreamHandler())
# logger.setLevel(logging.DEBUG)

db = connect(os.environ.get("DATABASE"))
if not db.connect():
    print("接続NG")
    exit()

class Weight(Model):
    """Weight Model"""

    id = IntegerField(primary_key=True)
    name = CharField()
    weight = FloatField()
    pub_date = TimestampField(default=datetime.datetime.now)

    class Meta:
        database = db
        table_name = "weights"

db.create_tables([Weight])
