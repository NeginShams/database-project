
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('db_app/', include('db_app.urls')),
    path('admin/', admin.site.urls),
]
