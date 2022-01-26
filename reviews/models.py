from django.db import models

from user.models import User

class Review(models.Model):
  member_id = models.ForeignKey(  
    User, on_delete = models.SET_NULL, null=True, db_column = 'member_id')
  date = models.DateTimeField()
  store_name = models.CharField(max_length=50)
  title = models.CharField(max_length=50)
  body = models.TextField()
  file = models.FileField(upload_to='', blank = True)

  class Meta:
    db_table = 'review'
    app_label = 'reviews'
    managed = False