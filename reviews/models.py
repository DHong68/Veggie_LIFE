from django.db import models
from user.models import User

class Review(models.Model):
  id = models.IntegerField(primary_key=True)
  member_id = models.ForeignKey(
    User, related_name="review", on_delete=models.DO_NOTHING, db_column="member_id"
  )
  date = models.DateTimeField()
  store_name = models.CharField(max_length=50)
  title = models.CharField(max_length=50)
  body = models.TextField()
  file = models.FileField()

  class Meta:
    db_table = 'review'
    app_label = 'reviews'
    managed = False