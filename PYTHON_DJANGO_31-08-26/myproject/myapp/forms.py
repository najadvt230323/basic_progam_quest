from django import forms
from .models import Student
import re

class Stu_form(forms.ModelForm) :
    class Meta :
        model = Student
        fields = "__all__"

# ----------------------------------------------------

    def clean_age(self):
        age_1 = self.cleaned_data["age"]

        if age_1 > 0 :
                return age_1

        else :
            raise forms.ValidationError(
                "enter a valid Age."
            )

# -------------------------------------------------------

    def clean_email(self):
            email_1 = self.cleaned_data["email"]
    
            pattern_1 = r'^[a-z][a-z0-9]*@gmail\.com$'
    
            if not re.match(pattern_1,email_1) :
                raise forms.ValidationError(
                    "enter a valid gmail address."
                )
            return email_1


# ----------------------------------- USING FORM CLASS --------------------------------


class Stu_form_2(forms.Model) :
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    age = forms.IntegerField()
    email = forms.EmailField()
    course = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    