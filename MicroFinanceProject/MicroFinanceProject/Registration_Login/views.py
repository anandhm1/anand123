from django.shortcuts import render, HttpResponse, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def LogInView(request):
    if request.method=='POST':

        un=request.POST.get('username')
        pw=request.POST.get('password')

        user=authenticate(username=un, password=pw)

        if user is not None:
            login(request, user)
            return redirect('Mainhomepage')

    template_name='Registration_Login/LoginForm.html'
    context={}
    return render(request, template_name, context)

def SignUpView(request):
    obj_form=RegistrationForm

    if request.method=='POST':
        obj_form=RegistrationForm(request.POST)
        if obj_form.is_valid():
            obj_form.save()
            return redirect('login')

    template_name='Registration_Login/SignUpForm.html'
    context={'obj_form':obj_form}
    return render(request, template_name, context)

def LogOutView(request):
    logout(request)
    return redirect('index')