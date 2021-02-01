from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
 
from .models import CustomUser
 
#from django.contrib.auth.models import User

class Orderform(forms.ModelForm):

    class Meta:
        model = Ordertrip
        fields = "__all__"
class SignUpForm(UserCreationForm):
   
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('username', 'first_name','password1','password2','company_name', 'phone','address','email')

