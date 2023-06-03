from django.urls import path
from a.views import *

app_name = "a"
urlpatterns = [
    path("csk/", csk, name="csk"),
    path("csk1/", csk1, name="csk1"),
]