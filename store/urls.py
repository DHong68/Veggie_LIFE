from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('show/', views.show, name='show'),
    path('search/', views.search, name='search'),
    path('details/', views.details, name='details'),
]