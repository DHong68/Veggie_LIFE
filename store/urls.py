from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('details/', views.details, name='details'),
    # path('menu/', views.menu, name='menu'),
]