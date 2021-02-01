from django.shortcuts import redirect
from .forms import Orderform
from .filters import bookflightFilter
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from .forms import SignUpForm
from .models import CustomUser
from .filters import bookflightFilter
from django.http import HttpResponse

from django.views.generic import View
from django.shortcuts import render
from django.views.generic.base import TemplateView



# import model in views.html by from.models import name model & * import all
from.models import *

# Create your views here.
   
def home(request):
    showdatab = Bookflight.objects.all()
    serchfilter=bookflightFilter(request.GET,queryset=Bookflight.objects.all())
    conttext={'showdatab':showdatab,'serchfilter':serchfilter}
    return render(request, 'SAFR/home.html', conttext) 
    
def userlogin(request):
    if request.method =="POST":
                
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None:
          login(request,user)
          return redirect('home')   
    return render(request,'SAFR/login.html')
def signUp(request):
          
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'SAFR/signUp.html', { 'form' : form })

def visa(request):
    visas = Visa.objects.all()
    return render(request, 'SAFR/visa.html', {'visas': visas}) 
    
def Creatorder(request):
    form = Orderform()
    if request.method == 'POST':
        form=Orderform(request.POST)
        if form.is_valid():
           form.save()
           return redirect('/')
    conttext={'form':form}
    return render(request, 'SAFR/creatorder.html',conttext)

#def userLogout(request):
          #logout(request)
          #return render('login')
          

          