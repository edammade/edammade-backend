from datetime import datetime
from mongoengine import Document
from mongoengine.fields import (
    DateTimeField, StringField, EmailField
)


class Account(Document):
  meta = {'collection': 'account'}
  email = EmailField()
  username = StringField()
  password = StringField()
  update_date = DateTimeField(default=datetime.now)
  last_login_date = DateTimeField()
  user_admin = StringField()

