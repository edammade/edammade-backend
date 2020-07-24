from mongoengine import connect
import json
from model import Account
import sys


def init_db():
    argument = sys.argv
    del argument[0]

    with open('settings.json') as json_file:
        json_data = json.load(json_file)
        db_data = json_data['database']
        connect(
            alias='default',
            db=db_data['db_name'],
            host=db_data['url'],
            port=db_data['port'],
            username=argument[0],
            password=argument[1],
            authentication_source=db_data['source']
        )
