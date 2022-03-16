from django.db import models
from Operational_Head.models import LoanSaction

class Account_Head(models.Model):
    loan_id = models.OneToOneField(LoanSaction,on_delete = models.CASCADE)
    sanction_amt = models.FloatField()
    rate_of_interest = models.FloatField()
    loan_tenure = models.IntegerField()
    total_amt = models.FloatField()
    is_customer_responsed = models.BooleanField('proceed',default = False)
    is_emi_details_filled = models.BooleanField('Yes',default = False)
    user_id = models.IntegerField()
    #is_loan_details_filled = models.BooleanField('Yes',default = False)

    def __str__(self):
        return f'{self.loan_id}---- {self.id} {self.sanction_amt} {self.rate_of_interest} {self.is_customer_responsed} {self.is_emi_details_filled} '

class Emi_Model(models.Model):
    account_head = models.OneToOneField(Account_Head,on_delete = models.CASCADE)
    mothly_emi_amt = models.FloatField()
    interest = models.FloatField()
    gst = models.FloatField()
    total_amt = models.FloatField()
    due_date = models.DateField()
    last_payment_status = models.CharField(max_length = 200)
    customer_id = models.IntegerField()
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length=200)
    sanction_amt = models.FloatField()

    def __str__(self):
        return f'{self.mothly_emi_amt} {self.interest} {self.gst} {self.total_amt} {self.due_date} {self.last_payment_status}  {self.customer_id} {self.first_name}{self.last_name}{self.sanction_amt} {self.customer_id}'