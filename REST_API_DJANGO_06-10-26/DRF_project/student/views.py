from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from  .serializers import Student_serializer
from .models import Student




# Create your views here.

@api_view(['get'])

def student_list(request) :
    stud = Student.objects.all()

    outputdata = Student_serializer(
        stud , 
        many = True
    )
    return Response(outputdata.data)



