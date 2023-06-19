from django.urls import path
from . import views

urlpatterns = [
    path("plotly-globe", views.plotly_globe, name="plotly-graphs-page"),
]