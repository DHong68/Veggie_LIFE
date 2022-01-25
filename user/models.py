from django.db import models


class User(models.Model):
    
    user_id = models.CharField(max_length=30, null = False, unique=True)
    password = models.CharField(max_length=50, null = False)
    re_password = models.CharField(max_length=50, null = False)
    email = models.CharField(max_length=50, null = False)
    name = models.CharField(max_length=50, null = False)
    veg_type = models.CharField(max_length=30, null = False)

    class Meta:
        db_table = 'user'
        app_label = 'user'
        managed = False