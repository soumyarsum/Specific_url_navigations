from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def csk(request):
    return render(request, "csk.html")

def csk1(request):
    return HttpResponse("<center><h1>This is CSK Httpresponse page.</h1></center>")