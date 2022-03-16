from django.shortcuts import render,redirect
from .models import Customer,LoanSaction
from .forms import CustomerForm,LoanSanctionForm
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Operational_Executive.models import CibilSc


@login_required(login_url='staff_login')
def showdata(request):
    userobj = User.objects.all()
    cibilobj = CibilSc.objects.all()
    context = {'userobj':userobj,'cibilobj':cibilobj}
    template_name = 'Operational_Head/showdata.html'
    return render(request,template_name,context)

@login_required(login_url='staff_login')
def sanctionloan(request,id):
    obj = User.objects.get(id=id )

    if request.method == 'POST':
        obj = CibilSc.objects.get(customer_id = id)
        obj.is_loan_sanctioned = True
        obj.save()
        amt = request.POST.get('amt')
        s = LoanSaction(sanction_amt = amt,user_id= id)
        s.save()
        return redirect('approved')
    context = {'obj':obj}
    template_name = 'Operational_Head/sanction.html'
    return render(request,template_name,context)
@login_required(login_url='staff_login')
def approved(request):
    obj = LoanSaction.objects.all()
    context = {'obj':obj}
    template_name = 'Operational_Head/approved.html'
    return render(request, template_name, context)

@login_required(login_url='staff_login')
def opr_head_dashboard_view(request):
    return render (request,'Operational_Head/dashboard/dashboard.html')