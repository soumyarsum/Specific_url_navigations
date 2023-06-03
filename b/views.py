from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mi(request):
    return render(request, "mi.html")

def mi1(request):
    return HttpResponce("<center><h1>This is Mi Httpresponse page.</h1></center>")