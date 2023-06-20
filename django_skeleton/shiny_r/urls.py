from django.urls import path
from . import views


urlpatterns = [
    path("shiny-app", views.shiny_app, name="shiny-app-page"),
]
