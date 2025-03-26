from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

from user.views import UserCreateView, ManageUserView

app_name = "user"

urlpatterns = [
    path("register/", UserCreateView.as_view(), name="register"),
    path("login/", ObtainAuthToken.as_view(), name="login"),
    path("me/", ManageUserView.as_view(), name="manage"),
]
