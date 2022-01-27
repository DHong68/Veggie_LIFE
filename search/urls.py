from django.urls import path
from . import views

app_name='search'

urlpatterns = [
 path('', views.check_vegan, name="home"),
 path('result/', views.check_result,name='result'),

]