from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('submit/', views.submit, name='submit'),
    path('master/', views.master, name='master'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
]