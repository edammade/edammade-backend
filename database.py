from mongoengine import connect
import json
from model import Account


def init_db():

    with open('settings.json') as json_file:
        json_data = json.load(json_file)
        db_data = json_data['database']
        connect(
            alias='default',
            db=db_data['db_name'],
            host=db_data['url'],
            port=db_data['port'],
            username=db_data['username'],
            password=db_data['password'],
            authentication_source=db_data['source']
        )
