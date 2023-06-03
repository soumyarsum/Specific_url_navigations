from django.shortcuts import render

# Create your views here.
def india(request):
    return render(request, "india.html")

def india1(request):
    return HttpResponce("<center><h1>This is BCCI Httpresponse page.</h1></center>")