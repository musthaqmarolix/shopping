from django.http import HttpResponse

def home(request):
    return HttpResponse("welcome to my page")

def employee(request):
    return HttpResponse("Employee page")