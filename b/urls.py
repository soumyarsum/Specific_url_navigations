from django.urls import path
from b.views import *

app_name = "b"
urlpatterns = [
    path("mi/", mi, name = "mi"),
    path("mi1/", mi1, name = "mi1"),
]