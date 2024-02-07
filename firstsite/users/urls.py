
from django.urls import path
from . import views

app_name='users'
urlpatterns = [
    path('', views.login_users, name="base"),
    path('login/', views.login_users, name="login"),
    path('logout/', views.logout_users, name="logout"),

]