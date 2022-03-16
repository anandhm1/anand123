from django.db import models
from Registration_Login.forms import User


class CibilSc(models.Model):
    customer = models.OneToOneField(User,on_delete=models.CASCADE)
    cibil = models.IntegerField()
    status = models.CharField(max_length=100,default="pending")
    is_loan_sanctioned = models.BooleanField('Sanctioned', default=False)


    def __str__(self):
        return self.customer

