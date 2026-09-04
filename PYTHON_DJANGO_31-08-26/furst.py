
# cd .\PYTHON_DJANGO_31-08-26\
# cmd
# 1.env creaction--------------- py -m venv env
# 2.activate -env -------------- env\Scripts\activate
# 3.install django-------------- pip install django

# 4.project folder creation----- django-admin startproject myproject

# django-admin --version

# 5.cd project folder----------- cd myproject
# 6.app creation---------------- py manage.py startapp myapp

# 7.run------------------------- py manage.py runserver

# 2,5,7

# 8.admin folder creation------  python manage.py makemigrations

# 8.admin folder creation------  python manage.py migrate

# 8.admin folder creation------  python manage.py createsuperuser



'''

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
September 01, 2026 - 12:45:33
Django version 6.1, using settings 'myproject.settings'
Starting WSGI development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/6.1/howto/deployment/

'''

# ---------------------------------------------------------------------------------------------------------------------------


# from django.shortcuts import render , HttpResponse


# def display(request):
#     return HttpResponse("hello , world !")

# ---------------------------

# def show(request):
#     return render(request,"show.html")

# ---------------------------

# def show1(request):
#     return render(request,"show1.html",{"data" : "najad"})


# def show2(request):
#     abc={
#         "name" : "najad" ,
#         "age"  : 25 ,
#         "place": "kozhikode" 
#     }

#     return render(request,"show2.html",{"data" : abc})

# -------------------------------------------

# def show3(request):
#     return render(request,"home.html")


# -------------------------------------------------------------------------------------

'''
<body>
    <header style="align-items: center; background-color: aqua; text-align: center;"> navigation bar </header>

    {% block content %}

    {% endblock %}

    <footer style="align-items: center; background-color: aqua; text-align: center;">quest</footer>

</body>

'''

'''
{% extends 'base.html' %}

{% block content %}

<h1>home page</h1>
<h2>my first html page</h2>
<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequuntur illum, necessitatibus quis neque facere ea
    reiciendis perferendis sequi vero modi animi aliquid laborum, reprehenderit laboriosam voluptatibus qui quo!
    Reiciendis, distinctio.</p>

{% endblock %}
'''


