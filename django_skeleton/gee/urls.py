from django.urls import path
from .views import gee_demo, rapel_demo


urlpatterns = [
    path("gee", gee_demo.as_view(), name="gee_demo-page"),
    path("gee/rapel", rapel_demo.as_view(), name="gee_rapel-page")
]
