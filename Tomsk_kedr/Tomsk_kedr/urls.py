from django.contrib import admin
from django.urls import path
from api.urls import urlpaterns as api_urls


urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += api_urls