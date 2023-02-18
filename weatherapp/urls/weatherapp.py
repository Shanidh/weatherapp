from django.urls import path
from ..apis import weatherapp


urlpatterns = [
    path("", weatherapp.LoginAPI.as_view(), name="login"),
    path("create", weatherapp.CreateAPI.as_view(), name="create"),
    path("logout", weatherapp.LogoutAPI.as_view(), name="logout"),
    path("weather", weatherapp.WeatherAPI.as_view(), name="weather"),
]