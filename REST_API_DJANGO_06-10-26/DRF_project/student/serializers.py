# serializers
# -----------------


from .models import Student
from rest_framework  import serializers

class Student_serializer(serializers.ModelSerializer) :
    class Meta:
        model=Student
        fields='__all__'


from django.contrib.auth.models import User 

class Register_serializer(serializers.ModelSerializer) :
    password = serializers.CharField(write_only = True)

    class Meta:
        model=User
        fields=['username' , 'email' , 'password']

    def create(self , validated_data) :

        user = User.objects.create_user(
            username= validated_data['username'] ,
            email= validated_data['email'] ,
            password= validated_data['password']
        )
        return user





