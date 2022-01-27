from django.contrib import admin
from django.urls import path,include
from user import views as userviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',userviews.home),
    path('reviews/', include('reviews.urls')),  
    path('store/', include('store.urls')),
    path('user/', include('user.urls')),
    
  
   
    
] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
