from django.shortcuts import render

# Create your views here.

def shiny_app(request):
    return render(request, "shiny_r/shiny_r.html")
