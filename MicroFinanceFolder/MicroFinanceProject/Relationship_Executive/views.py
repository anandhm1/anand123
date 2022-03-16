from django.shortcuts import render,redirect,HttpResponse
from . forms import BaseInformatin,BasicInformationForm,BasicInforBankForm,DocumentForm
from  django.contrib.auth.decorators import login_required
from Registration_Login.forms import User
from .models import BaseInformatin,BankDetails,DocumentUpload
from Operational_Executive.models import CibilSc
from Customer.models import Loan_Enquiry_Model
@login_required()
def baseiformview(request):
    form = BasicInformationForm()
    if request.method == 'POST':
        form = BasicInformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('back')
    tempalate_name = "Relationship_Executive/baseinfoform.html"
    context = {'form': form}
    return render(request,tempalate_name,context)
@login_required()
def bankformview(request):
    form = BasicInforBankForm()
    if request.method == 'POST':
        form = BasicInforBankForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("document")
    tempalate_name = "Relationship_Executive/baseinfoform.html"
    context = {'form':form}
    return render(request,tempalate_name,context)
@login_required()
def documentupload(request):
    form = DocumentForm()
    if request.method == 'POST':
        form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show1')
    tempalate_name = "Relationship_Executive/document.html"
    context = {'form':form}
    return render(request,tempalate_name,context)


def priView(request,id):
    obj1 = User.objects.all(id=id)
    obj2 = BaseInformatin.objects.filter(customer_id=id)
    obj3 = BankDetails.objects.filter(customer_id=id)
    obj4 = DocumentUpload.objects.filter(customer_id=id)
    template_name = "Relationship_Executive/priview.html"
    context = {"obj1":obj1,"obj2":obj2,"obj3":obj3,"obj4":obj4}
    return render(request,template_name,context)


def showview(request):
    obj = User.objects.all()
    obj1 = CibilSc.objects.all()
    obj3 =Loan_Enquiry_Model.objects.all()
    template_name= "myapp/show.html"
    context = {"obj":obj,"obj1":obj1,'obj3':obj3}
    return render(request, template_name, context)
