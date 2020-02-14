from django.db import models
from application.models.vendor import vendor    #importing vendor to implement foreign key
from application.models.user import user    #importing user to implement foreign key

class bill(models.Model):   #creating bill table
    id=models.AutoField(auto_created=True, primary_key=True)    #implementing primary key
    vendor=models.ForeignKey(vendor,on_delete=models.CASCADE) #implementing foreign key
    bill_date=models.DateField()
    items = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    tax = models.CharField(max_length=100)
    total = models.CharField(max_length=100)
    user=models.ForeignKey(user,on_delete=models.CASCADE)      #implementing foreign key
    class Meta:
        db_table="bill"
