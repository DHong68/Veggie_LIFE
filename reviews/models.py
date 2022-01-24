from django.db import models

from user.models import Member

class Review(models.Model):
  member_id = models.ForeignKey(
    Member, on_delete = models.SET_NULL, null=True, db_column = 'member_id')
  date = models.DateTimeField()
  store_name = models.CharField(max_length=50)
  title = models.CharField(max_length=50)
  body = models.TextField()

  class Meta:
    db_talbe = 'review'
    managed = False