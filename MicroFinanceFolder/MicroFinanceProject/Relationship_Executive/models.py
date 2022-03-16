from django.db import models
from Registration_Login.forms import User

class BaseInformatin(models.Model):
    customer = models.OneToOneField(User,on_delete=models.CASCADE)
    Father_Name = models.CharField(max_length=100)
    Current_Address = models.CharField(max_length=100)
    Pin_Code = models.IntegerField()
    city= models.CharField(max_length=100)
    Parmanet_Address = models.CharField(max_length=100)
    Pin_Code = models.IntegerField()
    city = models.CharField(max_length=100)
    Occupation = models.CharField(max_length=100)
    Annual_Income = models.FloatField()
    Income_certificat_number=models.CharField(max_length=100)
    Product_ID = models.CharField(max_length=100)
    Vehicle_Manufacturer = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    Vehicle_Color = models.CharField(max_length=100)
    
    Required_Loan_Amount=models.FloatField()
    Guarantor_Name = models.CharField(max_length=100)
    Profession = models.CharField(max_length=100)
    Contact_Number =models.IntegerField()
    Aadhar_Number =models.IntegerField()
    Pan_Card_Number = models.CharField(max_length=100)
    Address = models.CharField(max_length=200)


class BankDetails(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    Account_Holder_Name=models.CharField(max_length=100)
    Account_Number = models.IntegerField()
    Bank_Name = models.CharField(max_length=100)
    IFSC_Code = models.CharField(max_length=100)

class DocumentUpload(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="img/")
    sigh = models.ImageField(upload_to="img/")
    pan = models.ImageField(upload_to="img/")
    aadhar = models.ImageField(upload_to="img/")
    bank = models.ImageField(upload_to="img/")
    check1 = models.ImageField(upload_to="img/")
    salary = models.ImageField(upload_to="img/")
    itr = models.FileField(upload_to="img/")
    def __str__(self):
        return self.customer






