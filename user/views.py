from email import message
from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
# Create your views here.
def Register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            newUser = User()
            newUser.username=username
            newUser.set_password(password)
            newUser.save()
            login(request,newUser)
            messages.info(request,"Başarı ile kayıt oldunuz")
            return redirect("index")
    else:
        context={"form":form}
        return render(request,"register.html",context)
    """if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            newUser = User()
            newUser.username=username
            newUser.set_password(password)
            newUser.save()
            login(request,newUser)
            return redirect("index")
        else:
            return render(request,"register.html",context)
    else:
        form = RegisterForm()
        context={"form":form}
        return render(request,"register.html",context)"""
def Login(request):
    form = LoginForm(request.POST or None)
    context ={"form":form}
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user =authenticate(request,username=username,password=password)
        
        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return render(request,"login.html",context)
        else:
            messages.success(request,"Başarı ile giriş yaptınız")
            login(request,user)
            return redirect("index")
    return render(request,"login.html",context)
def Logout(request):
    logout(request)
    messages.success(request,"Başarılı bir şekilde çıkış yapıldı")
    return redirect("index")