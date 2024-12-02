from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('auth_service.urls')),
    path('restaurant/',include('restaurant_service.urls')),
]
