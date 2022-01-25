from django.db import models

# from user.models import Member

class Review(models.Model):
# member_id = models.ForeignKey(  // 아직 member 모델이 없어서 일단 주석
#   Member, on_delete = models.SET_NULL, null=True, db_column = 'member_id')
  id = models.IntegerField(primary_key=True)
  member_id = models.IntegerField()
  date = models.DateTimeField()
  store_name = models.CharField(max_length=50)
  title = models.CharField(max_length=50)
  body = models.TextField()

  class Meta:
    db_table = 'review'
    app_label = 'reviews'
    managed = False