from django.db import models
from django.db.models.fields import CharField, TextField

class Store(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    gu = models.CharField(max_length=10)
    address = models.TextField()
    menu = models.TextField()

    class Meta:
        db_table = 'store'
        app_label = 'store'
        managed = False
