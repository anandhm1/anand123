from django.shortcuts import render,redirect,get_object_or_404
from .models import Account_Head,Emi_Model
from Operational_Head.models import LoanSaction,Customer
from .forms import Account_Head_Form,Emi_Model_Form
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from Customer.models import Loan_Enquiry_Model
#For PDF Generation

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.core.mail import EmailMessage


login_required(login_url ='staff_login')
def acc_headform(request,id):
    obj = LoanSaction.objects.get(id=id )
    cust = obj.id
    san_amt = obj.sanction_amt
    user_id = obj.user.id
    print(user_id)
    if request.method == 'POST':
        obj.is_loan_details_filled = True
        obj.save()
        rate_of_interest = request.POST.get("rate_of_interest")
        loan_tenure = request.POST.get('loan_tenure')
        total_amt = request.POST.get('total_amt')
        c = Account_Head(rate_of_interest=rate_of_interest,loan_tenure=loan_tenure,total_amt=total_amt,loan_id_id= cust,sanction_amt =san_amt,user_id=user_id )
        c.save()
        return redirect('loanee_data')
    context = {'obj':obj}
    template_name = 'Accounts_Head/account_head_form.html'
    return render(request,template_name,context)

@login_required(login_url ='staff_login')
def show(request):
    obj = LoanSaction.objects.all()
    template_name = 'Accounts_Head/show.html'
    context = {'obj':obj}
    return render(request,template_name,context)

@login_required(login_url ='staff_login')
def account_head_data (request):
    obj = Account_Head.objects.all()
    template_name = 'Accounts_Head/account_head_data.html'
    context = {'obj':obj}
    return render(request,template_name,context)

@login_required(login_url ='staff_login')
def emiview(request,id):
    print(id)
    obj = Account_Head.objects.get(id=id)
    cid = obj.loan_id.user.id
    fname = obj.loan_id.user.first_name
    lname = obj.loan_id.user.last_name
    san_amt = obj.loan_id.sanction_amt


    if request.method == 'POST':
        obj.is_emi_details_filled = True
        obj.save()
        mothly_emi_amt = request.POST.get('mothly_emi_amt')
        interest = request.POST.get('interest')
        gst = request.POST.get('gst')
        total_amt = request.POST.get('total_amt')
        due_date = request.POST.get('due_date')
        last_payment_status = request.POST.get('last_payment_status')
        s = Emi_Model(mothly_emi_amt = mothly_emi_amt,interest=interest,gst=gst,total_amt=total_amt,due_date=due_date,
                      last_payment_status=last_payment_status,account_head_id=id,customer_id=cid,first_name=fname,last_name=lname,
                      sanction_amt=san_amt)
        s.save()
        return redirect('loan_cust_list')
    template_name = 'Accounts_Head/emi.html'
    context = {'obj':obj}
    return render(request,template_name,context)

@login_required(login_url ='staff_login')
def dummy(request,id):
    obj = Account_Head.objects.get(user_id = id)
    obj1 = LoanSaction.objects.all()
    obj2 = id
    if request.method == 'POST':
        obj = Account_Head.objects.get(user_id=id)
        obj.is_customer_responsed = True
        obj.save()
        return redirect('ApplicationStatus')
    template_name = 'Accounts_Head/dummy.html'
    context = {'obj1':obj1,'obj2':obj2,'obj':obj}
    return render (request,template_name,context)

@login_required(login_url ='staff_login')
def loanee_customersview(request):
    obj = Emi_Model.objects.all()
    print('*********',obj)
    context = {'obj':obj}
    template_name = 'Accounts_Head/loanee_customers.html'
    return render(request,template_name,context)

#For PDF Generation
#pip install xhtml2pdf
@login_required(login_url='staff_login')
def emi_invoice_render_pdf_view(request,id):
    customer =  Emi_Model.objects.get(pk=id)
    template_path = 'Accounts_Head/pdfgenerator.html'
    context = {'obj': customer}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = ' filename="report.pdf"'
    template = get_template(template_path)# we will get a object of template
    html = template.render(context)
    print(html,'****') #we will get entire template
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


@login_required(login_url='staff_login')
def loan_details_email(request):
    content = 'hello'
    email = EmailMessage(
        'Loan Details',
        'Loan Disbursed',
        "soitkarshubham555@gmail.com",
        ['shubhamsoitkar555@gmail.com']
    )
    email.fail_silently = True
    email.attach('invoice.pdf',content,)
    email.send()
    return redirect('email_sent_response')

@login_required(login_url='staff_login')
def email_response_view(request):
    return render(request,'Accounts_Head/email_response.html')

@login_required(login_url='staff_login')
def dashboardview(request):
    template_name = 'Accounts_Head/dashboard/dashboard.html'
    return render(request,template_name)

def customer_response_change_view(request,id):
    current_user_id = id
    model_obj = Loan_Enquiry_Model.objects.get(user_id=current_user_id)
    model_obj.loan_status = True
    model_obj.save()
    return redirect('loanee_data')