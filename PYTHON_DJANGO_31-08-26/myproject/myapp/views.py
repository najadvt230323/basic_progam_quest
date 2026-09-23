from django.shortcuts import render , HttpResponse ,redirect

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

from .forms import Stu_form

def insert_data1(request) :
    if request.method == "POST" :
        f=Stu_form(request.POST)
        if f.is_valid():
            f.save()
            return redirect("add")
            # return HttpResponse(f"student added successfully")
        else:
            # return HttpResponse(f"forms are not valid")    
            return render(request , "insert_data1.html" , {"data": f})

    else:
        f=Stu_form()
        return render(request , "insert_data1.html" , {"data": f})

# --------------------DATA FATCH USING DJANGO FORMS-----------------------------


def fetch_data1(request) :
    s=Student.objects.all()
    return render(request , "fetch_data1.html" , {"data": s})

# --------------------DATA DELETE USING DJANGO FORMS-----------------------------


def delete_data1(request,id_no) :
    s=Student.objects.get(id = id_no)
    s.delete()
    return redirect("/fetch_data1/")
    # return redirect("fetch")

    # return HttpResponse("student deleted successfully")


# --------------------DATA update USING DJANGO FORMS-----------------------------

from .forms import Stu_form

def update_data1(request,id_no) :
    s=Student.objects.get(id = id_no)

    if request.method == "POST" :
        f=Stu_form(request.POST , instance=s)
        if f.is_valid():
            f.save()
            return HttpResponse(f"student added successfully")
        else:
            return HttpResponse(f"forms are not valid")
            # return render(request , "insert_data1.html" , {"data": f})

    else:
        f=Stu_form(instance=s)
        return render(request , "insert_data1.html" , {"data": f})


# --------------------- DATA INSERT USING FORM CLASS --------------------------

from .forms import Stu_form_2

def insert_data_2(request) :
    if request.method == "POST" :
        f=Stu_form_2(request.POST)
        if f.is_valid():
            name = f.cleaned_data["name"]
            age = f.cleaned_data["age"]
            email = f.cleaned_data["email"]
            course = f.cleaned_data["course"]
            password = f.cleaned_data["password"]

            Student.objects.create(
                name = name ,
                age = age ,
                email = email ,
                course = course ,
                password = password    
            )

            return HttpResponse ("student added successfully")
        else :
            # return HttpResponse ("form is not valid")
            return render(request , "insert_data_2.html" , {"data": f})

    else :
        form_1 = Stu_form_2()
        return render(request , "insert_data_2.html" , {"data": form_1})


# -----------------------------------CRATE AUTH TABEL STUDENT -------------------------------------------------

from .models import Myuser

def stu_new(request) :
    if request.method == "POST" :
        a = request.POST.get('fname')
        b = request.POST.get('lname')
        c = request.POST.get('email')
        d = request.POST.get('uname')
        e = request.POST.get('pwd')
        f = request.POST.get('ph')

        Myuser.objects.create_user(
            username   = d ,
            password   = e ,
            email      = c ,
            first_name = a ,
            last_name = b ,
            phone = f ,
            is_staff = False ,
            is_superuser = False ,
            is_active = True
        )
        return HttpResponse("Register Successfully")
    return render(request , "stu_new_reg.html")

# --------------------------------------------------------------------------------------------------
        
from .forms import loginform
from django.contrib.auth import authenticate , login

def login_form(request) :
    if request.method == "POST" :
        unamae = request.POST.get("username")
        pwd = request.POST.get("password")
        user = authenticate(username=unamae , password=pwd)
        # print(user)

        if user is not None :

            if user.is_superuser == False and user.is_staff == False :
                login(request,user)
                return HttpResponse("WELCOME STUDENT USER")
            elif user.is_superuser == False and user.is_staff == True :
                login(request,user)
                return HttpResponse("WELCOME STAFF USER")
            else :
                login(request,user)
                return HttpResponse("WELCOME ADMIN USER")
        else :
            return HttpResponse("INVALID CREDENTIAL , TRY AGAIN")
       
    else :
        form = loginform()
        return render(request , "login.html" , {"data": form})
    
# -------------------------------------------------------------------------------------

from .forms import loginform
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required
def logout_form(request) :
    logout(request)

    return redirect("/login")
    # return HttpResponse("Logout Successful")

    # form = loginform()
    # return render(request , "login.html" , {"data": form})  ----------------> erorr


# -------------------------SESSION AND COOKIE-------------------------------------------

# -----------------------SESSION-----------------------

def set_session(request):
    if request.method == "POST" :
        request.session["username"] = request.POST.get("username")
        request.session["password"] = request.POST.get("password")
        return HttpResponse ("session is set")
    form = loginform()
    return render(request , "login.html" , {"data": form})

# ---------------------------

def get_session(request):
    username = request.session.get("username")
    password = request.session.get("password")
    if username and password :
        return HttpResponse (f"username = {username} , password = {password}")
    else :
        return HttpResponse("sessison is not exists")

# -----------------------------

def delete_session(request) :
    if request.session.exists("username") and request.session.exists("password") :
        return HttpResponse ("session is exists")
    else :
        del request.session["username"]
        del request.session["password"]
        return HttpResponse ("session is deleted")


# ------------------------------------------------------------------------------------------------------


# -----------------------COOKIES MANAGEMENT----------------------

def set_cookie(request):
    response = HttpResponse("Cookie created")
    response.set_cookie('name', 'sree')
    return response


def get_cookie(request):
    name = request.COOKIES.get('name')
    return HttpResponse(f"Name: {name}")


def update_cookie(request):
    response = HttpResponse("Cookie updated")
    response.set_cookie('name', 'Aswathi')
    return response


def delete_cookie(request):
    response = HttpResponse("Cookie deleted")
    response.delete_cookie('name')
    return response

# ============================================================================================






















