from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail,send_mass_mail
# Create your views here.
from app.forms import *
from app.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def fun_register(request):
    userform=UserForm()
    profileform=ProfileForm()
    if request.method=='POST' and request.FILES:
        UD=UserForm(request.POST)
        PD=ProfileForm(request.POST,request.FILES)
        if UD.is_valid() and PD.is_valid():
            us=UD.save(commit=False)
            pw=UD.cleaned_data['password']
            us.set_password(pw)
            us.save()
            ps=PD.save(commit=False)
            ps.user=us
            ps.save()
            send_mail('Registration',
            'Thanks For Registration',
            'manikanndan.n15@gmail.com',
            [us.email],fail_silently=False)
            return HttpResponse('Registration is SuccessFull')

    d={'uf':userform,'pf':profileform}
    return render(request,'register.html',d)

def fun_home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        return render(request,'home.html',context={'username':username})
    return render(request,'home.html')

def fun_login(request):
    if request.method=='POST':
        un=request.POST['username']
        pw=request.POST['password']
        user=authenticate(username=un,password=pw)
        if user and user.is_active:
            login(request,user)
            request.session['username']=un
            return HttpResponseRedirect(reverse('fun_home'))
        else:
            return HttpResponse('please enter correct user details')

    return render(request,'user_login.html')

@login_required
def fun_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('fun_home'))

@login_required
def fun_profile(request):
    username=request.session.get('username')
    user=User.objects.get(username=username)
    profile=Profile.objects.get(user=user)
    d={'user':user,'profile':profile}
    return render(request,'profile.html',d)

@login_required
def fun_changepassword(request):
    if request.method=='POST':
        username=request.session['username']
        #oldpw=request.POST['oldpw']
        newpw=request.POST['newpw']
        user=User.objects.filter(username=username)
        #user1=User.objects.get(password=oldpw)
        if user:
            user.set_password(newpw)
            user.save()
            return HttpResponse('Password Changed SuccessFull')
        else:
            return HttpResponse('Please provide correct password')
    return render(request,'changepassword.html')

def fun_forgotpassword(request):
    if request.method=='POST':
        email=request.POST['email']
        pw=request.POST['newpw']
        user=User.objects.filter(email=email)
        if user:
            user[0].set_password(pw)
            user[0].save()
            return HttpResponse('Password Reset Done Successfully')
        else:
            return HttpResponse('Please provide correct details')
    return render(request,'forgotpassword.html')