from django.urls import path
from django.contrib.auth import urls as auth_urls
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("record/<int:pk>", views.customer_record, name="record"),
    ]   