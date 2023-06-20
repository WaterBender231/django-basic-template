from django.urls import path
from .views import gee_demo


urlpatterns = [
    path("gee", gee_demo.as_view(), name="gee_demo-page"),
]
