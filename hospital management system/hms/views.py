from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login


# Create your views here.
def home(request):
    return render(request, "hms/home.html")

def cont(request):
    return render(request, "hms/contact.html")
def about(request):
    return render(request, "hms/about.html")

def user_login(request):
    if request.method=='POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            u=fm.cleaned_data['username']   
            p=fm.cleaned_data['password']
            user=authenticate(username=u,password=p)
            if user is not None:
                login(request,user)
                return redirect('/')
    else:
        fm=AuthenticationForm()
    return render(request, "hms/login.html",{'fm':fm})
