from django.urls import path

from user.views import UserCreateView

app_name = "user"

urlpatterns = [
    path("register/", UserCreateView.as_view(), name="register"),
]
