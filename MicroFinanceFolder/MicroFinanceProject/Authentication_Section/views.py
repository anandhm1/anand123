from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate

def staff_loginview(request):
    template_name ='Authentication_Section/LoginForm.html'
    if request.method == 'POST':
        un = request.POST.get('username')
        ps = request.POST.get('password')
        user = authenticate(username=un,password=ps)
        if user is not None:
            print(user)
            if un == 'shubhamopr':
                print('****',user)
                login(request,user)
                return redirect('opr_dashboard')
            elif un == 'shubhamacc':
                login(request,user)
                return redirect('acc_dashboard')
    context = {}
    return render(request,template_name,context)

def logoutview(request):
    logout(request)
    return redirect('index')
