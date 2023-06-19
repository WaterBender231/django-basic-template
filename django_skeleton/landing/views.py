from django.shortcuts import render 
from django.http import HttpResponse
# Create your views here.


#landing page showing django connection templates

def landing_page(request):
    return render(request, "landing/index.html")

    #return HttpResponse("hi")


#http://globing.django.themesbrand.com/index-12.html