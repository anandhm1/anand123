from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    customer_id = models.IntegerField(primary_key = True)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length=100)
    personal_details = models.CharField(max_length = 300)
    occupational_details = models.CharField(max_length=300)
    cibil = models.IntegerField()
    is_loan_sanctioned = models.BooleanField('Sanctioned',default=False)

    def __str__(self):
        return f'{self.customer_id} {self.first_name} {self.last_name} {self.is_loan_sanctioned}'

class LoanSaction(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='b')
    sanction_amt = models.FloatField()
    is_loan_details_filled = models.BooleanField('Yes', default=False)


    def __str__(self):
        return f'{self.customer} {self.sanction_amt}'




