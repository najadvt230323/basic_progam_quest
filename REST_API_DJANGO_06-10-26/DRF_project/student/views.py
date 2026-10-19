# views.py
# ===========


from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from  .serializers import Student_serializer
from .models import Student
from rest_framework import status

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated



# Create your views here.

@api_view(['get'])
@permission_classes([IsAuthenticated])
def student_list(request) :
    stud = Student.objects.all()

    outputdata = Student_serializer(
        stud , 
        many = True
    )
    return Response(outputdata.data)

@api_view(['post'])

def student_insert(request) :

    seri = Student_serializer(data = request.data)

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



@api_view(['get'])

def student_list_1(request , pk) :

    try :
        stud = Student.objects.get(id=pk)

    except Student.DoesNotExist :
        return Response(
            {"error" : "student not found"} ,
            status = status.HTTP_400_BAD_REQUEST
        )
    seri = Student_serializer(stud)

    return Response(seri.data)


    
@api_view(['put'])

def student_update(request , pk) :

    try :
        stud = Student.objects.get(id=pk)

    except Student.DoesNotExist :
        return Response(
            {"error" : "student not found"} ,
            status = status.HTTP_400_BAD_REQUEST
        )
    seri = Student_serializer(stud , data = request.data)

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

@api_view(['patch'])

def student_update_1(request , pk) :

    try :
        stud = Student.objects.get(id=pk)

    except Student.DoesNotExist :
        return Response(
            {"error" : "student not found"} ,
            status = status.HTTP_400_BAD_REQUEST
        )
    seri = Student_serializer(stud , data = request.data  , partial = True)

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



@api_view(['DELETE'])

def student_delete(request , pk) :

    try :
        stud = Student.objects.get(id=pk)

    except Student.DoesNotExist :
        return Response(
            {"error" : "student not found"} ,
            status = status.HTTP_400_BAD_REQUEST
        )

    stud.delete()

    return Response (
        {"message" : "student delete successfully"} ,
        status = status.HTTP_201_CREATED
    )
# ------------------------------------------------------------------------------------

from .serializers import Register_serializer

@api_view(['post'])

def student_register(request) :

    seri = Register_serializer(data = request.data)

    if seri.is_valid() :
        seri.save()

        return Response(
            {"message" : "user registered successfully"} ,
        )
    
    return Response(
        seri.errors ,
        status = status.HTTP_400_BAD_REQUEST
    )

# --------------------------------------------------------------------
# olgout
# ----------

from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['post'])
def logout(request):
    try:
        refresh_token_1 = request.data['refresh']

        tocen_1 = RefreshToken(refresh_token_1)

        tocen_1.blacklist()

        return Response (
            {"message" : "Logout successfully"} ,
            status = status.HTTP_205_RESET_CONTENT
        )

    except Exception :
        return Response (
            {"message" : "Invalid refresh token"} ,
            status = status.HTTP_400_BAD_REQUEST
        )

