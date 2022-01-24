from django.urls import path
from . import views

app_name='search'

urlpatterns = [
 path('', views.check_vegan),
 path('result/', views.check_result,name='result'),

]