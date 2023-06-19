from django.urls import path
from . import views


urlpatterns = [
    path("leaflet-map", views.leaflet_map, name="leaflet-map-page"),
]
