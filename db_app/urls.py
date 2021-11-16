from django.urls import path

from . import views

urlpatterns = [
    path('home', views.homepage, name='home'),
    path('register', views.register_page, name='register'),
    path('register_user', views.register_user, name='register_user'),
    path('user_list', views.user_list, name='user_list'),
    path('details', views.details, name='details'),
    path('edit', views.edit, name='edit'),
    path('edit_status', views.edit_status, name='edit_status'),
]