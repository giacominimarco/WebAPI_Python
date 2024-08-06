from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('auth/', include('api_rest.urls'), name='api_rest_urls'),
    path('admin/', admin.site.urls),
]
