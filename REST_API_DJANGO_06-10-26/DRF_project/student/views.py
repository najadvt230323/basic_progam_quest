from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from  .serializers import Student_serializer
from .models import Student
from rest_framework import status




# Create your views here.

@api_view(['get'])

def student_list(request) :
    stud = Student.objects.all()

    outputdata = Student_serializer(
        stud , 
        many = True
    )
    return Response(outputdata.data)

@api_view(['post'])

def student_insert(request) :

    seri = Student_serializer(
        data = request.data     
    )

    if seri.is_valid() :
        seri.save()

        return Response(
            seri.data ,
            status = status.HTTP_201_CREATED
        )
    
    return Response(
        seri.errors ,
        status = status.HTTP_400_BAD_REQUEST
    )





