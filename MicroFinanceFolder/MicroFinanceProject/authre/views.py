from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout

def loginViewRE(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        user = authenticate(username=un,password=pw)
        print(type(user))
        if user is not None:
            if un == 'anand':
                login(request,user)
                return redirect('reshow')
            elif un == 'oe':
                login(request, user)
                return redirect("show1")
            elif un == 'shubhamopr':
                login(request, user)
                return redirect('opr_dashboard')
            elif un == 'shubhamacc':
                login(request, user)
                return redirect('acc_dashboard')
            else:
                login(request,user)
                return redirect('index')
    template_name = "authre/login.html"
    context = {}
    return render(request,template_name,context)

def logoutViewRE(request):
    logout(request)
    return redirect('index')