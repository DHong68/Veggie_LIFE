from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('write/', views.write, name = 'write'),
    path('list/', views.list, name='list'),
    path('delete/<int:id>', views.delete, name = 'delete'),
    path('update/<int:id>/', views.update, name = 'update'),
    path('details', views.details, name='details'),
]