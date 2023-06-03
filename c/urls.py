from django.urls import path
from c.views import *

app_name = "c"
urlpatterns = [
    path("india/", india, name="india"),
    path("india1", india1, name="india1"),
]
