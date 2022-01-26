from django.db import models
from django.db.models.fields import CharField, TextField

class Store(models.Model):
    name = CharField(max_length=100)
    type = CharField(max_length=10)
    phone = CharField(max_length=20)
    gu = CharField(max_length=10)
    address = TextField()
    menu = TextField()

    def menu_as_list(self):
        return self.menu.split(',')

    class Meta:
        db_table = 'store'
        app_label = 'store'
        managed = False
