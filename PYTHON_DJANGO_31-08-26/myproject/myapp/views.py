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

def show4(request):
    time=int(input("enter a time :"))
    return render(request,"show4.html",{"data" : time})

def show5(request,name,age):
    return render(request,"show5.html",{"name" : name , "age" :age})


# -------------------------------------------------------------------

from .models import Student

def insert_data(request) :
    Student.objects.create(
        name = "najad" , 
        age = 25 ,
        email = "najad@gmail.com" ,
        course = "java",
        password = "najad"
    )
    return HttpResponse("student added successfully")



def fetch_data(request) :
    s=Student.objects.all()
    return render(request , "fetch.html" , {"data": s})


def delete_data(request,id_no) :
    s=Student.objects.get(id = id_no)
    s.delete()
    return HttpResponse("student deleted successfully")

def update_data(request,id_no) :
    s=Student.objects.get(id = id_no)
    s.age = 30
    s.save()
    return HttpResponse("student update successfully")

def update_data(request,id_no,age) :
    s=Student.objects.get(id = id_no)
    s.age = age
    s.save()
    return HttpResponse(f"student {s.name} update successfully")


# ------------------------------------------------------------------------------------

# --------------------DATA INSERTION USING DJANGO FORMS-----------------------------

