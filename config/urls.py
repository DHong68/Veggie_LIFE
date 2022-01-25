from django.contrib import admin
from django.urls import path,include
from user import views as userviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',userviews.home),
    path('reviews/', include('reviews.urls')),  
    path('search/', include('search.urls')),
    path('store/', include('store.urls')),
    path('user/', include('user.urls')),
    
  
   
    
]
