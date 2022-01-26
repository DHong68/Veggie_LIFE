from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('delete/', views.delete, name='delete'),
    path('mypage/', views.mypage, name='mypage'),
    # path('mypage/<str:user_id>/', views.mypage, name='mypage'),
    path('update/<str:user_id>', views.update, name='update'),


]