from django.shortcuts import render , HttpResponse

# Create your views here.

def display(request):
    return HttpResponse("hello , world !")

def display1(request):
    return HttpResponse("najad , 9562020207 ")

def show(request):
    return render(request,"show.html")

def show1(request):
    return render(request,"show1.html",{"data" : "najad"})


def show2(request):
    abc={
        "name" : "najad" ,
        "age"  : 25 ,
        "place": "kozhikode" 
    }

    return render(request,"show2.html",{"data" : abc})

def show3(request):
    return render(request,"home.html")




