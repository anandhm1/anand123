from django.shortcuts import render,redirect
from Registration_Login.forms import User
from .models import CibilSc
from Customer.models import Loan_Enquiry_Model
from Operational_Executive.models import CibilSc

def check(request,id):
    obj = User.objects.get(id=id)

    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        cibil = request.POST.get('cibil')
        status = request.POST.get('status')
        reg = CibilSc(customer_id=customer_id, cibil=cibil, status=status)
        reg.save()




        return redirect("show1")
    template_name ="Operational_Executive/cibil.html"
    context ={'obj':obj,}
    return render(request, template_name, context)

def show1(request):
    obj = User.objects.all()
    obj1 = CibilSc.objects.all()
    obj3 = Loan_Enquiry_Model.objects.all()

    template_name ="Operational_Executive/show.html"
    context ={'obj':obj, 'obj1':obj1,'obj3':obj3}
    return render(request, template_name, context)