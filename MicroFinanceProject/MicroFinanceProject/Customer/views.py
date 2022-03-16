from django.shortcuts import render, redirect
from .models import Loan_Enquiry_Model
from django.contrib.auth.decorators import login_required
from Registration_Login.forms import User
from Operational_Executive.models import CibilSc
from Accounts_Head.models import Account_Head

def IndexView(request):
    template_name = 'index.html'
    context = {}
    return render(request, template_name, context)

@login_required(login_url='login')
def Mainhomepage(request):
    template_name = 'Customer/Dashboard/ApplyNow.html'
    context = {}
    return render(request, template_name, context)

@login_required(login_url = 'login')
def LoanEnquiry(request):
    if request.method =='POST':
        user_id = request.user.id
        Loan_Amount = request.POST.get("Loan_Amount")
        Tenure_of_Loan = request.POST.get("Tenure_of_Loan")
        Purpose_of_Loan = request.POST.get("Purpose_of_Loan")
        Pancard_No = request.POST.get("Pancard_No")
        Mobile_No = request.POST.get("Mobile_No")

        obj_model = Loan_Enquiry_Model(user_id = user_id,Pancard_No=Pancard_No, Loan_Amount = Loan_Amount,Mobile_No=Mobile_No ,Tenure_of_Loan = Tenure_of_Loan, Purpose_of_Loan=Purpose_of_Loan)
        obj_model.save()
        return redirect('ApplicationStatus')

    template_name = 'Customer/EnquiryForm/EnquiryForm.html'
    context = {}
    return render(request, template_name, context)

@login_required(login_url = 'login')
def ApplicationTable(request):

    current_user_id = request.user.id
    print(current_user_id)
    application_obj = Loan_Enquiry_Model.objects.get(user_id = current_user_id)

    template_name = 'Customer/Dashboard/tables.html'
    context = {'application_obj':application_obj}
    return render(request, template_name, context)

@login_required(login_url = 'login')
def EMICalculator(request):
    template_name = 'Customer/EMI Calculator/EMICalculator.html'
    context = {}
    return render(request, template_name, context)

def ApprovedLoanView(request):
    current_user_id = request.user.id
    model_obj = Loan_Enquiry_Model.objects.get(id = current_user_id)

    if request.method == 'POST':
        model_obj.loan_status = True
        model_obj.save()
        return redirect("ApplicationStatus")

    template_name = 'Customer/Dashboard/ApprovedLoan.html'
    context = {'model_obj': model_obj}
    return render(request, template_name, context)

@login_required(login_url='login')
def AgrementView(request):
    template_name = 'Customer/Dashboard/agrement.html'
    context = {}
    return render(request, template_name, context)


def show1(request):
    obj = User.objects.all()
    obj1 =  CibilSc.objects.all()
    template_name = 'myapp/show.html'
    context = {"obj":obj,"obj1":obj1}
    return render(request, template_name, context)

