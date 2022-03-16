from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Loan_Enquiry_Model(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    Loan_Amount = models.FloatField()
    Tenure_of_Loan = models.IntegerField()
    Purpose_of_Loan = models.TextField()
    Pancard_No = models.CharField(max_length = 50)
    Mobile_No = models.IntegerField()
    loan_status = models.BooleanField('Approved', default=False)