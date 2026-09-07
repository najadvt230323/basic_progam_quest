from django.shortcuts import render , HttpResponse

# Create your views here.

def display(request):
    return HttpResponse("hello , world !")